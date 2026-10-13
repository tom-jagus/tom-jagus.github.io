"""Build checks for the custom Hugo shell, selection rules, and draft isolation.

Run with: mise exec -- python -m unittest discover -s tests -v
"""

import hashlib
import os
from pathlib import Path
import re
import shutil
import struct
import subprocess
import tempfile
import unittest
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]


class Document(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.elements = []
        self.text = path.read_text()
        self.feed(self.text)

    def handle_starttag(self, tag, attributes):
        self.elements.append((tag, dict(attributes)))

    def find(self, tag=None, **attributes):
        return [attrs for name, attrs in self.elements
                if (tag is None or name == tag)
                and all(attrs.get(key) == value for key, value in attributes.items())]


class SiteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory(prefix="hugo-template-tests-")
        cls.addClassCleanup(cls.temp.cleanup)
        cls.folder = Path(cls.temp.name)
        cls.production = cls.build(ROOT, "production")

        cls.source = cls.folder / "site"
        for directory in ("archetypes", "config", "layouts", "assets", "content", "static/site"):
            shutil.copytree(ROOT / directory, cls.source / directory)
        cls.entry("writing/no-headings", "No headings", "2020-01-01", draft=True,
                  extra="toc: true\n", body="This sample has no usable contents headings.")
        cls.review = cls.build(cls.source, "review", drafts=True)

        for collection in ("work", "writing"):
            index = cls.source / "content" / collection / "_index.md"
            index.write_text(index.read_text().replace("draft: true", "draft: false"))
        for day in (1, 2, 3):
            cls.entry(f"writing/published-{day}", f"Published article {day}",
                      f"2020-01-0{day}", extra="toc: true\n",
                      body="## A heading\n\nSome body text.\n\n## Another heading\n\nMore text.")
            cls.entry(f"videos/published-{day}", f"Published video {day}", f"2020-01-0{day}",
                      extra='watch_url: "https://example.org/watch"\nthumbnail: "thumbnail.svg"\nformat: "livestream-recording"\n')
            image = cls.source / "content" / "videos" / f"published-{day}" / "thumbnail.svg"
            image.write_text('<svg xmlns="http://www.w3.org/2000/svg" width="16" height="9"><rect width="16" height="9"/></svg>')
        for project in ("one", "two", "unselected"):
            extra = 'status: "In progress"\ngithub_url: "https://github.com/example/project"\n'
            if project == "one":
                extra = 'status: "Planned"\ngithub_url: "https://github.com/example/project"\nimage: "diagram.svg"\nimage_alt: "Fixture project diagram"\n'
            elif project == "unselected":
                extra = 'status: "Experimental"\n'
            cls.entry(f"work/project-{project}", f"Project {project}", "2020-01-01", extra=extra)
        (cls.source / "content/work/project-one/diagram.svg").write_text(
            '<svg xmlns="http://www.w3.org/2000/svg" width="640" height="360"><rect width="640" height="360"/></svg>')
        cls.entry("writing/future", "Future fixture", "2099-01-01")
        cls.entry("writing/expired", "Expired fixture", "1999-01-01",
                  extra="expiryDate: 2000-01-01\n")
        home = cls.source / "content" / "_index.md"
        home.write_text(home.read_text().replace("  - /work/website-rewrite", "  - /work/project-two\n  - /work/project-one\n  - /work/missing"))
        params = cls.source / "config/_default/params.toml"
        settings = params.read_text()
        for platform in ("youtube", "github", "x", "linkedin"):
            settings = settings.replace(f'  {platform} = ""', f'  {platform} = "https://example.org/{platform}"')
        params.write_text(settings)
        cls.published = cls.build(cls.source, "published", base="https://tom.jagus.me/review-path/")

        # Simulate approval of the page drafts only inside a temporary copy.
        cls.launch_source = cls.folder / "launch-site"
        shutil.copytree(cls.source, cls.launch_source)
        for name in ("about", "contact", "services"):
            page = cls.launch_source / "content" / f"{name}.md"
            page.write_text(page.read_text().replace("draft: true", "draft: false"))
        cls.routed = cls.build(cls.launch_source, "routed", base="https://tom.jagus.me/review-path/")

    @classmethod
    def entry(cls, route, title, date, draft=False, extra="", body="Private test fixture."):
        file = cls.source / "content" / route / "index.md"
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text(f'---\ntitle: "{title}"\ndescription: "Temporary test fixture."\ndate: {date}\ndraft: {str(draft).lower()}\n{extra}---\n\n{body}\n')

    @classmethod
    def build(cls, source, name, drafts=False, base="https://tom.jagus.me/"):
        destination = cls.folder / name
        env = os.environ.copy()
        env["HUGO_CACHEDIR"] = str(cls.folder / "cache")
        env["HUGO_RESOURCEDIR"] = str(cls.folder / "resources")
        command = ["hugo", "--source", str(source), "--destination", str(destination),
                   "--baseURL", base, "--noBuildLock", "--minify", "--panicOnWarning",
                   "--buildFuture=false", "--buildExpired=false",
                   f"--buildDrafts={str(drafts).lower()}", "--environment", "development" if drafts else "production"]
        result = subprocess.run(command, env=env, capture_output=True, text=True)
        if result.returncode:
            raise AssertionError(result.stdout + result.stderr)
        return destination

    def test_default_archetype_creates_yaml_drafts(self):
        source = self.folder / "archetype-site"
        shutil.copytree(self.source, source)
        env = os.environ.copy()
        env["HUGO_CACHEDIR"] = str(self.folder / "cache")
        result = subprocess.run(
            ["hugo", "new", "content", "writing/archetype-sample/index.md",
             "--source", str(source), "--noBuildLock"],
            env=env, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        content = (source / "content/writing/archetype-sample/index.md").read_text()
        self.assertTrue(content.startswith('---\ntitle: "Archetype Sample"\n'))
        self.assertIn('description: ""\ndraft: true\n---', content)
        self.assertNotIn("date:", content)

    def test_production_omits_drafts_empty_collections_and_legacy_content(self):
        home = Document(self.production / "index.html")
        self.assertEqual(sorted(path.relative_to(self.production).as_posix()
                                for path in self.production.rglob("*.html")), ["404.html", "index.html"])
        for collection in ("work", "writing", "videos"):
            self.assertFalse(home.find(id=collection))
            self.assertFalse((self.production / collection).exists())
        for route in ("about", "contact", "services", "shared"):
            self.assertFalse((self.production / route).exists())
        self.assertTrue(home.find("a", href="mailto:contact@jagus.me", **{"class": "button"}))
        self.assertNotIn("Sample service descriptions", home.text)
        self.assertTrue(home.find(id="contact"))
        self.assertTrue(home.find("a", href="/#contact"))
        self.assertNotIn("Layout sample", home.text)
        self.assertNotIn("blowfish", home.text.lower())
        self.assertEqual((self.production / "favicon.ico").read_bytes(), (ROOT / "static/site/favicon.ico").read_bytes())
        self.assertEqual(len(re.findall(r'<li>', home.text[home.text.index('aria-label="Service areas"'):].split('</ul>', 1)[0])), 5)

    def test_review_pages_and_homepage_contact_routing(self):
        home = Document(self.review / "index.html")
        self.assertTrue(home.find("a", href="/about/"))
        self.assertTrue(home.find("a", href="/services/"))
        self.assertTrue(home.find("a", href="/contact/", **{"class": "button"}))
        self.assertIn("Contact me", home.text)
        for route, title in (("about", "About me"), ("contact", "Contact"), ("services", "Services")):
            page = Document(self.review / route / "index.html")
            article_class = "page-layout article-layout services-layout article-layout--toc" if route == "services" else "page-layout"
            self.assertTrue(page.find("article", **{"class": article_class}))
            self.assertEqual(len(page.find("h1")), 1)
            self.assertIn(title, page.text)
            self.assertIn("Sample", page.text)
            self.assertTrue(page.find("a", href=f"/{route}/", **{"aria-current": "page"}))
        contact = Document(self.review / "contact/index.html")
        self.assertTrue(contact.find("a", href="mailto:contact@jagus.me", **{"class": "button"}))
        self.assertFalse(contact.find("a", href="/contact/", **{"class": "button"}))
        for route in ("about", "services"):
            self.assertTrue(Document(self.review / route / "index.html").find("a", href="/contact/", **{"class": "button"}))
        self.assertFalse((self.review / "shared").exists())

    def test_services_have_explanations_and_working_jump_links(self):
        page = Document(self.review / "services/index.html")
        links = [attrs for attrs in page.find("a")
                 if urlsplit(attrs.get("href", "")).path == "/services/"
                 and urlsplit(attrs.get("href", "")).fragment]
        self.assertEqual(len(links), 5)
        self.assertTrue(page.find("details", **{"class": "contents"}))
        self.assertTrue(page.find("nav", **{"aria-label": "Services"}))
        self.assertFalse(page.find("nav", **{"class": "service-navigation"}))
        self.assertEqual(len(page.find("h3")), 15)
        home = Document(self.production / "index.html").text
        summary = home[home.index('aria-label="Service areas"'):].split('</ul>', 1)[0]
        for link in links:
            identifier = urlsplit(link["href"]).fragment
            self.assertTrue(page.find("h2", id=identifier))
            title = re.search(rf'<h2 id=[\"\']?{re.escape(identifier)}[\"\']?>([^<]+)</h2>', page.text).group(1)
            self.assertIn(f"<li>{title}</li>", summary)
        self.assertIn("Unattended operation still needs maintenance", page.text)
        self.assertIn("Production integrations and automated actions require a separate assessment", page.text)

    def test_page_routes_work_after_approval_under_a_path_prefix(self):
        home = Document(self.routed / "index.html")
        for route in ("about", "services", "contact"):
            self.assertTrue(home.find("a", href=f"/review-path/{route}/"))
            self.assertTrue((self.routed / route / "index.html").is_file())
        self.assertTrue(home.find("a", href="/review-path/contact/", **{"class": "button"}))
        self.assertFalse(home.find("a", href="/review-path/#contact"))
        self.assertFalse((self.routed / "shared").exists())
        sitemap = (self.routed / "sitemap.xml").read_text()
        for route in ("about", "services", "contact"):
            self.assertIn(f"https://tom.jagus.me/review-path/{route}/", sitemap)

    def test_review_has_generated_toc_and_no_duplicate_ids(self):
        page = Document(self.review / "writing/publishing-workflow/index.html")
        self.assertTrue(page.find("details", **{"class": "contents"}))
        self.assertTrue(page.find("nav", id="TableOfContents", **{"aria-label": "Article contents"}))
        self.assertIn("Sample date", page.text)
        ids = [attrs["id"] for _, attrs in page.elements if "id" in attrs]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(len(page.find("h1")), 1)
        for attributes in page.find("a"):
            href = attributes.get("href", "")
            if href.startswith("#"):
                self.assertIn(unquote(href[1:]), ids)
        self.assertTrue(page.find("pre", tabindex="0"))
        self.assertLess(page.text.index('class=contents'), page.text.index('class=article-content'))
        self.assertTrue((self.review / "writing/publishing-workflow/workflow.svg").is_file())
        for route in ("writing/layout-note", "writing/no-headings"):
            self.assertFalse(Document(self.review / route / "index.html").find("details", **{"class": "contents"}))

    def test_rebuild_removes_stale_drafts_and_resources(self):
        output = self.build(self.source, "reused-output", drafts=True)
        self.assertTrue((output / "writing/publishing-workflow/index.html").exists())
        self.assertTrue((output / "videos/layout-sample/thumbnail.svg").exists())
        self.build(self.source, "reused-output")
        self.assertFalse((output / "writing/publishing-workflow/index.html").exists())
        self.assertFalse((output / "writing/publishing-workflow/workflow.svg").exists())
        self.assertFalse((output / "videos/layout-sample/thumbnail.svg").exists())
        for route in ("about", "contact", "services"):
            self.assertFalse((output / route).exists())

    def test_internal_videos_publish_only_referenced_resources(self):
        for output in (self.review, self.published):
            self.assertFalse((output / "videos/index.html").exists())
            self.assertFalse(list((output / "videos").rglob("*.html")))
        self.assertTrue((self.review / "videos/layout-sample/thumbnail.svg").exists())
        self.assertTrue((self.published / "videos/published-3/thumbnail.svg").exists())
        self.assertTrue((self.published / "videos/published-2/thumbnail.svg").exists())
        self.assertFalse((self.published / "videos/published-1/thumbnail.svg").exists())
        self.assertFalse((self.published / "videos/layout-sample").exists())

    def test_homepage_selection_and_publication_filters(self):
        home = Document(self.published / "index.html").text
        self.assertLess(home.index("Project two"), home.index("Project one"))
        self.assertNotIn("Project unselected", home)
        self.assertIn("Published article 3", home)
        self.assertIn("Published article 2", home)
        self.assertNotIn("Published article 1", home)
        self.assertIn("Published video 3", home)
        self.assertIn("Published video 2", home)
        self.assertNotIn("Published video 1", home)
        for slug in ("future", "expired", "no-headings", "publishing-workflow", "layout-note"):
            self.assertFalse((self.published / "writing" / slug).exists())
        self.assertIn("Livestream recording", home)
        self.assertTrue(Document(self.published / "index.html").find("a", href="/review-path/writing/"))

    def test_footer_renders_only_configured_links_in_order(self):
        for output in (self.production, self.review):
            self.assertFalse(Document(output / "index.html").find("a", **{"class": "social-link"}))
        links = Document(self.published / "index.html").find("a", **{"class": "social-link"})
        self.assertEqual([link["href"] for link in links],
                         ["https://example.org/youtube", "https://example.org/github",
                          "https://example.org/x", "https://example.org/linkedin", "/review-path/index.xml"])

    def test_feeds_and_sitemap_exclude_internal_and_unpublished_pages(self):
        for output in (self.production, self.review):
            self.assertEqual(ET.parse(output / "index.xml").findall(".//item"), [])
            locations = [node.text for node in ET.parse(output / "sitemap.xml").iter()
                         if node.tag.endswith("}loc")]
            self.assertEqual(locations, ["https://tom.jagus.me/"])
        feed = ET.parse(self.published / "index.xml")
        self.assertEqual(len(feed.findall(".//item")), 6)
        for file in ("index.xml", "sitemap.xml"):
            text = (self.published / file).read_text()
            for excluded in ("/videos/", "publishing-workflow", "layout-note", "/future/", "/expired/"):
                self.assertNotIn(excluded, text)

    def test_metadata_assets_integrity_and_subpath_links(self):
        for output, prefix in ((self.production, ""), (self.review, ""), (self.published, "/review-path"), (self.routed, "/review-path")):
            for file in output.rglob("*.html"):
                document = Document(file)
                self.assertTrue(document.find("meta", name="description"))
                self.assertTrue(document.find("meta", name="robots", content="noindex, nofollow"))
                self.assertTrue(document.find("link", rel="canonical"))
                icons = document.find("link", rel="icon")
                self.assertEqual([(icon["href"], icon["type"], icon["sizes"]) for icon in icons],
                                 [(prefix + "/favicon.ico", "image/x-icon", "16x16 32x32 48x48"),
                                  (prefix + "/favicon.svg", "image/svg+xml", "any")])
                for tag, attributes in document.elements:
                    address = attributes.get("src") or (attributes.get("href") if tag == "link" and attributes.get("rel") in ("stylesheet", "icon") else None)
                    if not address:
                        continue
                    path = urlsplit(address).path
                    self.assertTrue(path.startswith(prefix + "/"), address)
                    asset = output / path.removeprefix(prefix + "/")
                    self.assertTrue(asset.is_file(), str(asset))
                    if "integrity" in attributes:
                        import base64
                        checksum = base64.b64encode(hashlib.sha256(asset.read_bytes()).digest()).decode()
                        self.assertEqual(attributes["integrity"], "sha256-" + checksum)
                ids = [attrs['id'] for _, attrs in document.elements if 'id' in attrs]
                self.assertEqual(len(ids), len(set(ids)))
            self.assertEqual((output / "wordmark.svg").read_bytes(), (ROOT / "static/site/wordmark.svg").read_bytes())
            self.assertEqual((output / "avatar.png").read_bytes(), (ROOT / "static/site/avatar.png").read_bytes())

    def test_favicon_preserves_wordmark_strokes_and_ico_sizes(self):
        namespace = {"svg": "http://www.w3.org/2000/svg"}
        favicon = ET.parse(ROOT / "static/site/favicon.svg").getroot()
        wordmark = ET.parse(ROOT / "static/site/wordmark.svg").getroot()
        group = favicon.find("svg:g", namespace)
        original = wordmark.find("svg:g", namespace)
        self.assertEqual(favicon.get("viewBox"), "0 0 48 48")
        self.assertEqual(favicon.find("svg:rect", namespace).get("fill"), "#1E1E2E")
        for attribute in ("fill", "stroke-width", "stroke-linecap"):
            self.assertEqual(group.get(attribute), original.get(attribute))
        self.assertEqual([path.attrib for path in group], [path.attrib for path in original])
        data = (ROOT / "static/site/favicon.ico").read_bytes()
        self.assertEqual(struct.unpack_from("<HHH", data), (0, 1, 3))
        sizes = []
        for index in range(3):
            width, height, _, reserved, _, _, length, offset = struct.unpack_from("<BBBBHHII", data, 6 + index * 16)
            self.assertEqual(reserved, 0)
            self.assertGreater(length, 0)
            self.assertGreaterEqual(offset, 54)
            self.assertLessEqual(offset + length, len(data))
            sizes.append((width, height))
        self.assertEqual(sizes, [(48, 48), (32, 32), (16, 16)])
        for output in (self.production, self.review, self.published, self.routed):
            for name in ("favicon.svg", "favicon.ico"):
                self.assertEqual((output / name).read_bytes(), (ROOT / "static/site" / name).read_bytes())

    def test_work_index_images_stages_and_repository_links(self):
        index = Document(self.published / "work/index.html")
        self.assertTrue(index.find("ul", **{"class": "project-list"}))
        self.assertEqual(len(index.find("li", **{"class": "work-entry"})), 3)
        self.assertTrue(index.find("img", src="/review-path/work/project-one/diagram.svg", alt="Fixture project diagram"))
        defaults = index.find("img", src="/review-path/project-default.svg")
        self.assertEqual(len(defaults), 2)
        for image in defaults:
            self.assertIn("alt", image)
            self.assertIn(image["alt"], ("", None))
        repository_class = "text-link meta project-repository"
        self.assertEqual(len(index.find("a", **{"class": repository_class})), 2)
        for name, tone in (("one", "blue"), ("two", "peach"), ("unselected", "neutral")):
            stage_class = f"project-stage project-stage--{tone}"
            self.assertTrue(index.find("p", **{"class": stage_class}))
            page = Document(self.published / f"work/project-{name}/index.html")
            self.assertTrue(page.find("p", **{"class": stage_class}))
            self.assertEqual(len(page.find("a", **{"class": repository_class})), int(name != "unselected"))
            if name != "unselected":
                self.assertLess(page.text.index('id=article-title'), page.text.index('class="text-link meta project-repository"'))
                self.assertLess(page.text.index('class="text-link meta project-repository"'), page.text.index('class=lede'))
        self.assertNotIn('class=project-image', Document(self.published / "index.html").text)

    def test_project_stage_tones_and_missing_metadata(self):
        source = self.folder / "stage-site"
        shutil.copytree(self.source, source)
        page = source / "content/work/project-two/index.md"
        original = page.read_text()
        for stage, tone in (("Completed", "green"), ("Maintained", "teal"), ("Paused", "yellow"), ("Archived", "neutral")):
            page.write_text(original.replace('status: "In progress"', f'status: "{stage}"'))
            output = self.build(source, f"stage-{stage.lower()}")
            for route in ("work/index.html", "work/project-two/index.html"):
                document = Document(output / route)
                self.assertTrue(document.find("p", **{"class": f"project-stage project-stage--{tone}"}))
                self.assertIn(f"<strong>{stage}</strong>", document.text)
        page.write_text(original.replace('status: "In progress"\n', "").replace('github_url: "https://github.com/example/project"\n', ""))
        output = self.build(source, "stage-absent")
        document = Document(output / "work/project-two/index.html")
        self.assertNotIn("project-stage--", document.text)
        self.assertFalse(document.find("a", **{"class": "text-link meta project-repository"}))

    def test_project_images_require_valid_bundle_metadata(self):
        source = self.folder / "invalid-image-site"
        shutil.copytree(self.source, source)
        page = source / "content/work/project-one/index.md"
        original = page.read_text()
        page.write_text(original.replace('image: "diagram.svg"', 'image: "missing.svg"'))
        with self.assertRaisesRegex(AssertionError, "not a bundle resource"):
            self.build(source, "missing-project-image")
        page.write_text(original.replace('image_alt: "Fixture project diagram"\n', ""))
        with self.assertRaisesRegex(AssertionError, "image needs image_alt"):
            self.build(source, "missing-project-image-alt")

    def test_complete_mocha_palette_and_unchanged_color_roles(self):
        colors = {
            "rosewater": "f5e0dc", "flamingo": "f2cdcd", "pink": "f5c2e7", "mauve": "cba6f7",
            "red": "f38ba8", "maroon": "eba0ac", "peach": "fab387", "yellow": "f9e2af",
            "green": "a6e3a1", "teal": "94e2d5", "sky": "89dceb", "sapphire": "74c7ec",
            "blue": "89b4fa", "lavender": "b4befe", "text": "cdd6f4", "subtext1": "bac2de",
            "subtext0": "a6adc8", "overlay2": "9399b2", "overlay1": "7f849c", "overlay0": "6c7086",
            "surface2": "585b70", "surface1": "45475a", "surface0": "313244", "base": "1e1e2e",
            "mantle": "181825", "crust": "11111b",
        }
        css = (ROOT / "assets/css/site.css").read_text()
        for name, value in colors.items():
            self.assertIn(f"--{name}: #{value};", css)
        self.assertIn("--surface: var(--surface0);", css)
        self.assertIn("--muted: var(--subtext0);", css)

    def test_all_internal_html_links_resolve(self):
        for output, prefix in ((self.production, ""), (self.review, ""), (self.published, "/review-path"), (self.routed, "/review-path")):
            for file in output.rglob("*.html"):
                for attributes in Document(file).find("a"):
                    link = urlsplit(attributes.get("href", ""))
                    if link.scheme or link.netloc:
                        continue
                    if link.path:
                        self.assertTrue(link.path.startswith(prefix + "/"), link.path)
                        target = output / link.path.removeprefix(prefix + "/")
                        if target.is_dir():
                            target = target / "index.html"
                    else:
                        target = file
                    self.assertTrue(target.is_file(), str(target))
                    if link.fragment:
                        self.assertTrue(Document(target).find(id=unquote(link.fragment)), link.fragment)


if __name__ == "__main__":
    unittest.main()

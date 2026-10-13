# Local tooling and review builds

The rewrite uses ordinary Hugo Extended 0.167.0. `mise.toml` and `.github/workflows/hugo.yml` pin the same version. CI checks both pins and the downloaded edition. Building the custom layouts does not need Blowfish, Dart Sass, Node, or the brand repository.

## Install

With [mise](https://mise.jdx.dev/) available, run these commands from the repository root:

```bash
mise install hugo-extended
mise exec -- hugo version
```

The output should identify `v0.167.0` and `+extended`, without `+withdeploy`. There are no theme dependencies or Git submodules to initialize.

## Preview the templates

```bash
mise exec -- hugo server \
  --buildDrafts \
  --renderToMemory \
  --noBuildLock \
  --bind 127.0.0.1 \
  --port 1313
```

Open `http://127.0.0.1:1313/`. Review `/about/`, `/contact/`, `/services/`, `/work/`, `/work/website-rewrite/`, `/writing/`, `/writing/layout-note/`, and `/writing/publishing-workflow/` on that server. Stop it with Ctrl+C. The new pages and collection entries are labelled draft/sample material, not approved launch copy. Their dates and examples do not establish a publishing history. Keep this preview local.

Article and Services TOCs share the sticky right column at wide widths and collapse above the body on narrow screens. Services lists only its five offers, not their subsections. Both TOCs use native details navigation and stay open without JavaScript. The homepage cursor starts blinking only after its pause control is available; reduced motion and JavaScript-disabled browsing leave it still.

The custom Hugo pages are the current layout preview. Lists span the homepage container. Reading titles and paragraphs align with its left edge, with paragraphs kept at roughly 60 characters and figures/code allowed wider. Without a TOC, there is no reserved sidebar. About, Contact, and Services now have dedicated layouts and draft sample copy. Work now uses image-and-copy rows, with an optional bundle image or shared abstract default. Index entries and project pages display the same stage box from `status`, with repository links near titles. These changes still need Tom's visual review.

In draft preview, the homepage's About me and Explore services links point to the separate pages. Contact me opens `/contact/`; Email me on that page opens the email client.

## Production-content check

```bash
mise exec -- hugo \
  --minify \
  --noBuildLock \
  --panicOnWarning \
  --buildDrafts=false \
  --buildFuture=false \
  --buildExpired=false
```

Output goes to ignored `build/public/`, and generated resources go to `build/resources/`. Hugo cleans the destination when rebuilding, including stale draft output. Do not commit generated output. Root-level `public/`, `resources/`, and the Hugo lock file are also ignored as a guard against alternate build commands. A build is not publication.

The current production output contains the approved homepage introduction and shared service/contact copy, without draft collections or their navigation links. The expanded About, Contact, and Services sample pages remain drafts and are excluded. Internal `content/shared/` sources supply the existing service/contact introductions without generating routes. When the Contact draft is excluded, the header falls back to the homepage invitation and its button retains the direct Email me action, avoiding a broken link. All generated pages request no indexing, and `robots.txt` disallows crawling during review. Neither measure is access control.

## Content during conversion

- `content/` uses the accepted [Markdown/frontmatter structure](design/content.md). Do not add layout shortcodes.
- The old theme, archived content, generated trees, unused assets, and standalone static preview have been removed. Original content remains in Git history; the untracked preview has a verified external backup. See the [old URL inventory and recovery instructions](design/old-urls.md) before planning aliases or redirects.
- `archetypes/default.md` creates YAML drafts with `title`, `description`, and `draft`. Fill in the description and add date/collection-specific fields as needed; the default does not invent a publication date.
- Leave sample pages and bundles as `draft: true`. When a collection has real launch material, review its entries and change its index from draft as well.
- The homepage's `selected_work` list controls project order. Writing and internal videos select the latest two entries by `date`.
- Work-index custom `image` files must exist in their project bundle and have `image_alt`. Without an image, the index uses the decorative `project-default.svg`. Homepage project cards remain text-only.
- Project `status` text supplies the stage box on the index and detail page. Known stages receive the tints documented in the content contract; custom stages stay neutral. Missing status/repository metadata is omitted.
- All 26 Catppuccin Mocha colors are CSS custom properties in `:root`, for example `var(--green)` and `var(--surface1)`. Existing color roles stay unchanged.
- Video entries have no public HTML routes. Only referenced thumbnails are published, and videos are excluded from RSS and the sitemap.
- `content/shared/contact.md` and `content/shared/services.md` own the reusable Markdown-enabled `intro` fields. The shared Contact title is the invitation heading, separate from the Contact page H1. Homepage service names come from the shared Services H2 headings; tests keep them consistent with the full page.
- About, Contact, and Services Markdown bodies hold the expanded copy. The Services page generates its jump links from those headings and has optional `contact_heading`/`contact_intro` fields for its service-specific invitation.
- The shared collection renders no pages or assets and appears in no public listing. Keep it non-draft so homepage introductions remain available independently of the expanded page drafts.
- Exact social URLs are still unconfirmed. Their configuration is empty, so no placeholder profile links are rendered.

See [asset sources](design/assets.md) for the copied brand assets and fonts. The build publishes only `static/site/`, not the old static collection.

## Repository layout

```text
.github/workflows/   Build-only review CI
archetypes/          YAML content starter
assets/              CSS and JavaScript source
config/_default/     Hugo settings and navigation
content/             Markdown pages, bundles, and internal shared copy
docs/                Development, design, and project context
layouts/             Custom Hugo templates
static/site/         Brand assets and licensed fonts
tests/               Temporary-build checks
mise.toml            Exact Hugo Extended pin
.gitignore           Generated output and cache exclusions
```

`build/` is created locally when needed and is not repository source.

## Tests

```bash
mise exec -- python -m unittest discover -s tests -v
```

Python 3.11 or newer is needed for the tooling/CI checks. The build tests use the standard library and temporary directories. They check YAML draft creation, draft/future/expired exclusion, stale-output cleanup, homepage selection, internal video resources, generated TOC links, standalone-page routing, service jump links, project images/stages/repositories, the full Mocha palette, feeds, metadata, asset integrity, subpath URLs, and internal links. They do not replace browser or assistive-technology checks.

## GitHub Actions

The workflow builds on pushes to `main` or `feat/website-rewrite`, pull requests targeting `main`, and manual runs. It verifies the exact ordinary Extended archive's SHA-256, runs the template tests, and uploads a `hugo-review-<commit>` artifact retained for seven days.

There is no submodule checkout, Pages setup, deployment job, or Pages write permission. Output goes to the runner's temporary directory. Keep this workflow build-only until publication is separately authorized. Unpushed workflow edits do not change the remote deployment setup.

Review artifacts are not private storage. Keep draft rendering disabled in CI and confidential material out of the repository.

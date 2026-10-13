# Local development and deployment

The site uses ordinary Hugo Extended 0.167.0. `mise.toml` and `.github/workflows/hugo.yml` pin the same version. CI verifies the download checksum, edition, and local pin. Building the site does not need Blowfish, Dart Sass, Node, or the brand repository.

## Install

With [mise](https://mise.jdx.dev/) available, run these commands from the repository root:

```bash
mise install hugo-extended
mise exec -- hugo version
```

The output should identify `v0.167.0` and `+extended`, without `+withdeploy`. There are no theme dependencies or Git submodules.

## Preview

To preview production content:

```bash
mise exec -- hugo server --renderToMemory --noBuildLock --bind 127.0.0.1 --port 1313
```

Open `http://127.0.0.1:1313/`. Home, About, Services, and Contact are approved for inclusion. To also review the unpublished Work, Writing, and Video samples, add `--buildDrafts`. Keep that preview local. Draft status controls generated output, not access to Markdown in a public repository.

Shared page headers show a draft review notice in Mocha red when applicable, followed by the description in peach and the page title. Published pages omit the notice. Reach out links open Contact; only Contact has an Email me button with a mailto link.

Article and Services contents lists use a sticky right column on wide screens and a collapsible block above the body on narrow screens. Services lists its five offers. Without JavaScript, the contents stay open and ordinary navigation remains available. The homepage cursor has a pause toggle and stays still with reduced motion or without JavaScript.

## Check production output

```bash
mise exec -- hugo \
  --minify \
  --noBuildLock \
  --panicOnWarning \
  --buildDrafts=false \
  --buildFuture=false \
  --buildExpired=false
```

Output goes to ignored `build/public/`, with generated resources in `build/resources/`. Hugo cleans the destination when rebuilding, including stale draft output. Do not commit generated HTML. A local build is not publication.

The initial production site contains Home, About, Services, Contact, and the 404 page. Work, Writing, and Videos remain draft-only. Search indexing is enabled, and `robots.txt` allows crawling and links to the sitemap. Draft pages retain noindex metadata when previewed.

Before publishing a change, inspect the generated routes, follow the affected links, check images and metadata, and review the pages at mobile and desktop widths. The automated test suite has been removed at Tom's request. CI checks the Hugo toolchain and fails the build on warnings, but does not replace link, accessibility, or browser review.

## Content updates

- Use the [Markdown/frontmatter structure](design/content.md). Do not add layout shortcodes.
- The default archetype creates YAML drafts without an invented publication date. Fill in the description and any collection-specific fields.
- Keep samples as `draft: true`. Publish real entries and their collection indexes together when reviewed.
- Homepage `selected_work` controls project order. Writing and internal videos select the latest two published entries by date.
- Work images must be bundle resources with `image_alt`. Without an image, the index uses a decorative abstract diagram. Homepage project cards remain text-only.
- Project `status` supplies the stage box. Missing status and repository links are omitted.
- Videos have no public HTML routes. Only referenced thumbnails are published, and videos stay out of RSS and the sitemap.
- Shared service/contact introductions live in non-rendering `content/shared/` sources. Services has its own `intro` for its opening and engagement explanation.
- `config/_default/params.toml` holds contact details, supplied social URLs, asset names, and the indexing setting.
- The site publishes only `static/site/`. The existing desktop and mobile backgrounds remain unchanged.
- Historical content remains in Git. No legacy redirects will be added for this launch; see the [old URL inventory](design/old-urls.md).

See [asset sources and regeneration](design/assets.md) for the avatar, sharing image, favicon, and fonts.

## GitHub Actions

The workflow builds on pushes to `main` and `feat/website-rewrite`, pull requests targeting `main`, and manual runs. Every build excludes drafts, future entries, and expired entries, and uses `https://tom.jagus.me/` as its base URL.

Non-production branches and pull requests upload a `hugo-review-<commit>` artifact retained for seven days. Pushes to `main`, and manual runs on `main`, upload a Pages artifact and deploy it through the `github-pages` environment. Pull requests never deploy. Only the deploy job has Pages write and OIDC permissions.

Main-branch runs are not canceled automatically, and deployment jobs share the `pages` concurrency group. The workflow does not install Python test dependencies or run the removed test suite; its toolchain check uses Python 3.11 or newer already available on the runner.

GitHub Pages must use GitHub Actions as its source, with `tom.jagus.me` as the custom domain and HTTPS enabled. Those settings were verified during the local launch audit. The updated workflow still needs a successful GitHub-hosted run after an explicitly authorized push or merge. Editing this file does not publish the website.

Review artifacts and public source are not private storage. Keep confidential material out of the repository.

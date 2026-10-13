# Progress and next action

## Current state

The custom Hugo templates, including the latest Services TOC and Work/project-metadata changes, are implemented locally and ready for Tom's review. Repository cleanup is complete; only active source, tooling, tests, brand assets, licensed fonts, and useful documentation remain. The [definition](definition.md), [layout brief](../design/layout.md), and [content contract](../design/content.md) remain authoritative. Hugo is ordinary Extended 0.167.0, pinned locally and in CI.

The rewrite is on `feat/website-rewrite`. This source snapshot includes the toolchain, custom templates, draft Markdown samples, assets, tests, documentation, and removal of legacy/generated files. The standalone design preview and local validation artifacts are excluded. Tom approved the implementation, cleanup, website-favicon exception, and a local commit. No tag, push, or deployment is authorized. Use Git history and status for the current commit and working-tree state; further edits or Git actions need their own approval.

Implemented locally:

- `layouts/` contains the shared metadata/header/menu/footer, homepage, reading template, dedicated About/Contact/Services and Work-index layouts, a Writing/basic index fallback, 404, RSS, sitemap, and robots templates. `assets/css/site.css` and `assets/js/site.js` adapt the approved preview.
- The homepage reads Markdown copy, curated work, latest writing, and the internal video collection. Empty collections and unavailable destinations are omitted. Social links remain absent until their exact URLs are confirmed.
- The reading template generates one optional TOC, sticky on the desktop right and collapsible below the title on narrow screens. Reading titles and paragraphs now align with the homepage container's left edge. Lists span its full width; paragraphs retain roughly a 60-character measure, and figures/code use the content area's full width. No sidebar is reserved without a TOC. Services shares that contents component and responsive layout, listing only its five H2 offers rather than repeated subsections. The contact invitation stays full-width. The cursor has a working pause toggle and stays still with reduced motion or without JavaScript.
- Blowfish, submodule declarations, the empty module configuration, obsolete images/fonts/favicons, old generated trees, and the working-tree legacy archive are removed. All 43 archived content files matched the original `content/` tree at `4292a28` and remain recoverable from Git history. The [old URL inventory](../design/old-urls.md) records 47 HTML routes, 12 RSS routes, and recovery instructions.
- The untracked static design study has a verified 12-file backup outside the repository, recorded in that inventory. All seven retained brand/font assets matched their preview copies. Current layout review uses Hugo rather than a duplicate static prototype.
- Draft About/Contact/Services pages and project/writing/video bundles support local review. Services explains all five offers with jump links, contributions, possible outputs, and boundaries. The homepage's Contact me action opens the separate Contact page, where Email me opens the email client.
- Non-rendering `content/shared/` Markdown sources own the existing short service/contact introductions, keeping them available when the expanded page drafts are excluded. Production retains the original homepage invitation and direct email fallback. Work now has full-width image-and-copy rows. Bundle images require alt text; entries without an `image` field use a shared decorative abstract diagram. Index entries and project pages share stage boxes from `status`, with repository links near their titles. Missing metadata is omitted and custom stages remain neutral. Project write-ups reuse the reading layout; Writing retains its full-width list.
- The favicon uses the original three wordmark strokes on a rounded Mocha Base square, under Tom's approved website-specific exception. Every HTML page links an SVG and a 16/32/48px ICO fallback with subpath-safe URLs. The external brand guidance and full header wordmark are unchanged.
- CSS exposes all 26 Catppuccin Mocha colors while preserving existing color roles. The original avatar, fonts, and font license are unchanged. Tom will supply a smaller avatar at the end; font optimization is deferred.

Output goes to ignored `build/public/` and `build/resources/`. Destination cleanup prevents old draft output surviving a production rebuild. Root-level generated output and the Hugo lock file are ignored too. The default archetype now creates YAML drafts without an invented publication date. The favicon pass adds delivery assets, head links, and tests without changing editorial content, CSS/JavaScript, CI, the Hugo pin, or existing identity assets.

The working-tree workflow is build-only, runs the template tests, and uploads ordinary production-content review artifacts. All site pages request no indexing during review. The remote deployment workflow remains unchanged because nothing has been pushed. See [development commands](../development.md) and [asset sources](../design/assets.md).

## Validation

Production and draft builds passed with warnings treated as failures. Eighteen repeatable Python build tests passed for YAML draft creation, publication filters, stale-output cleanup, selection order, generated TOC links, internal video routes/resources, RSS/sitemap exclusions, metadata, asset integrity, confirmed-link ordering, standalone page/contact routing, all five service jump links, project image validation/fallbacks, stage tints and missing metadata, nearby repository links, the full Mocha palette, favicon geometry/ICO sizes and publication, subpath URLs, and internal links. Tests simulate approving the new page drafts only in a temporary copy. JavaScript syntax, workflow linting, and whitespace checks passed. The cleanup previously preserved build output byte-for-byte. The Services/Work pass added the project illustration and layout changes; the favicon pass adds two static icon assets and head links. The preview backup and complete URL inventory remain the recovery references.

The Services/Work pass's Chromium checks passed at 1440, 768, 390, and 320px across nine routes: Home, About, Contact, Services, Work, a project write-up, Writing, and articles with/without a TOC. Checks covered alignment and paragraph measure, image loading, desktop/mobile TOCs, all five service anchor offsets, full-width Services contact panel, project image stacking/stages/repository links, menu focus/scroll-lock regression, cursor pause, reduced motion, JavaScript-disabled browsing, print, and forced colors. All nine routes passed 200% text enlargement at 320px and automated Axe WCAG A/AA checks. Six desktop/mobile screenshots were inspected. The favicon pass verified SVG/ICO links and image decoding across six HTML routes in Chromium, and inspected 16/32/48px previews on light and dark backgrounds. The broader layout checks were not repeated for this head-only change. Browser scripts and screenshots are temporary; do not depend on `/tmp` surviving.

GitHub-hosted CI, assistive-technology testing, and other browser engines have not been run. These checks do not establish launch readiness with final content.

## Remaining work and inputs

- Review Services' side TOC and the Work index/project stage boxes, default image, and nearby repository links. Review the Writing index with real material.
- Replace the new page samples with reviewed personal/service/contact copy before changing their draft status.
- Select real launch projects, writing, and videos. Replace or omit the private samples; do not invent a portfolio or publishing history.
- Confirm exact YouTube, GitHub, LinkedIn, and X URLs, the livestream platform, and manual announcement fields/expiry behavior. No stream notices or automatic live claims are implemented.
- Review the recorded old URLs, including `/blog/`, and choose useful alias/redirect destinations before launch. No redirects were added during cleanup.
- Review the new favicon at browser-tab size, final social icon/share artwork, accessibility with assistive technology, and live DNS/Pages settings. Restore indexing and enable deployment only during separately authorized launch work.

## Next action

Tom should review `/services/`, `/work/`, and `/work/website-rewrite/` through the local draft server, and check the new favicon in the browser tab. Further source changes, tags, pushes, or deployment require separate approval.

# Launch preparation and next action

## Current state

The local source is prepared for an initial release of Home, About, Services, and Contact. Those pages have `draft: false`, published pages allow search indexing, and Contact provides the only Email me button. Reach out links elsewhere lead to Contact. Shared page headers display draft notices in red above the descriptions and titles when previewing unpublished material.

Work and Writing have prepared index introductions, but their indexes and sample entries remain drafts. Video samples remain unpublished too. The production homepage omits these collections and their navigation destinations. Real content creation is deferred, as Tom requested.

Tom supplied a smaller `avatar.jpg` and the YouTube, GitHub, X, and LinkedIn URLs. Configuration now points to the JPEG. The sharing image is a 1200 by 630 JPEG with the same circular avatar crop centered on Mocha Base, linked through Open Graph and Twitter card metadata. The favicon, fonts, and site backgrounds are unchanged. Tom rejected and removed the root-level background experiments.

The automated test suite has been removed at Tom's request. The pinned Hugo toolchain check and production build remain in CI, with warnings treated as failures. The workflow deploys only on pushes to `main` or manual runs on `main`. Pull requests and the rewrite branch build production-content review artifacts without deploying.

No legacy aliases or redirects will be added. Tom reports that the previous website had no traffic and accepts that removed URLs will return 404. The [old URL inventory](../design/old-urls.md) remains available for history and recovery, not as outstanding launch work.

The initial-message warning was removed at Tom's request. This is a website-specific change from the external brand kit's contact guidance; the brand repository has not been edited. The limited, human-led AI offer and confidentiality boundaries for client work remain intact.

## Validation

Local production, draft, and subpath builds passed with warnings treated as failures. One-off checks verified the five HTML routes in production, draft exclusion and sample-resource omission, working internal links and CSS asset references, indexing behavior, canonical/share URLs, sharing image and avatar delivery, the four supplied social links, empty initial RSS, sitemap entries, unique IDs, and stylesheet/script integrity. These checks were not added as a replacement test suite.

Workflow linting with actionlint 1.7.12, JavaScript syntax, and whitespace checks passed. The sharing image was inspected visually. Chromium checks passed across the four launch routes at 1440, 768, 390, and 320 pixels, with no horizontal overflow, image failures, or browser errors. All four routes passed 200% text enlargement at 320 pixels. Mobile-menu opening, Escape, focus restoration, scroll locking, reduced motion, and JavaScript-disabled navigation passed.

During the preceding launch audit, GitHub Pages was configured for GitHub Actions, `tom.jagus.me`, and enforced HTTPS; DNS and the live HTTPS response worked. Tom reports that email delivery is tested and working. The updated workflow has not run on GitHub, and no new deployment has occurred. Other browser engines, screen readers, and live sharing-platform previews remain unverified.

## Next action

Launch preparation is complete locally on `feat/website-rewrite`. Tom authorized committing the remaining changes without a tag or push. Use Git history and status to verify the current commit and working tree. Publication still requires separate authorization for the necessary Git actions. The old remote website remains unchanged until a deployment succeeds.

After an authorized release, check the live pages, navigation, email action, social links, favicon, robots file, sitemap, and sharing image. Work, Writing, Videos, and livestream notices are later content work, not prerequisites for this release.

The [definition](definition.md), [content contract](../design/content.md), [layout brief](../design/layout.md), and [development guide](../development.md) describe the accepted scope and implementation.

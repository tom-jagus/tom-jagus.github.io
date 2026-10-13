# Progress and action plan

## Current state

Design and content decisions are settled enough to begin the first custom Hugo conversion unit. Tom accepted the homepage/article styling, content folders and YAML fields, `github_url`, optional project images, and a desktop-right/mobile-collapsible TOC. The agreed target is ordinary Hugo Extended 0.167.0, to be pinned exactly locally and in CI, not `extended_withdeploy`. See the [project definition](definition.md), [layout brief](../design/layout.md), and [content structure](../design/content.md) for the authoritative choices.

The branch is `feat/website-rewrite`; HEAD remains `822e079`, the starting `main` commit. `design-preview/` and `docs/` are untracked. Nothing from the rewrite has been committed, pushed, or deployed. The isolated [static preview](../../design-preview/README.md) has the approved colors, bold lavender titles, infinite cursor blink with reduced-motion fallback, sticky header, mobile menu, background blur, and solid footer. Its article still has an inline TOC. The newly accepted responsive TOC has not been implemented.

The production Hugo site is unchanged. Configuration still selects Blowfish, and `.github/workflows/hugo.yml` still pins Hugo 0.128.0, deploys on `main` pushes, and permits manual runs. Hugo is not available in the current shell, and no custom Hugo layouts have been created. `.gitmodules` still declares the theme and legacy `public` submodule. Existing content has theme shortcodes and outdated service wording. The target Hugo version and content folders are decisions, not completed migration work.

Only the documentation update is authorized at this handoff. Earlier preview-edit approvals do not grant Hugo source/configuration edits or carry into a new session. Obtain explicit authority for the next conversion unit. Git actions and publication require their own authorization.

## Remaining inputs and checks

- Select real projects, writing, and videos ready for launch. Omit empty collections and navigation destinations.
- Confirm the exact YouTube, GitHub, LinkedIn, and X profile URLs and the livestream platform.
- Define manual stream announcement fields and expiry behavior without implying automatic live detection.
- Review remaining page layouts during implementation, using the approved homepage/article and accepted content structure.
- Make Hugo Extended 0.167.0 available locally and update the CI pin under implementation approval.
- Resolve the continuous cursor's missing pause/hide control before publication. Reduced-motion support exists but is not a general pause control.
- Recheck responsive layout and cursor behavior after the latest manual CSS changes.
- Verify live DNS and Pages settings for the confirmed domain before launch.

## Proposed action plan

1. Agree the source/configuration edit scope, make Hugo Extended 0.167.0 available locally, and pin the same version in CI. Keep deployment inactive during review.
2. Build the shared shell, homepage, and article templates from the approved preview, with generated responsive TOC behavior. Use clearly labeled private drafts for validation, not invented launch content.
3. Build and review the remaining page templates, migrate to the accepted content structure, and remove Blowfish dependencies. Inventory old URLs, including `/blog/`, and preserve useful links.
4. Select launch content and adapt approved brand copy. Include only projects and publications ready for public use; omit empty collections and navigation destinations.
5. Simplify the build and deployment setup. Remove the obsolete theme and `public` submodule arrangements, pin the required tooling, and add pull-request build checks without production deployment. Review manual deployment behavior so the rewrite cannot go live accidentally.
6. Validate the site locally and in CI. Check internal links, drafts, metadata, old URLs, keyboard use, contrast, mobile reflow, and text enlargement. Document local authoring and build commands.
7. Review the completed site with Tom. Merge and publish only under separate authorization, then check the live domain and deployment.

## Preview validation

Earlier Chromium checks rendered both pages at 1440, 768, 390, and 320px. They passed for page-wide overflow, loaded fonts/images, 44px targets, 200% text enlargement at 320px, skip-link behavior, mobile-menu keyboard handling and scroll lock, sticky-header anchor offsets, and background blur. Color, principal contrast, local references, duplicate IDs, unchanged brand/font copies, footer order, reduced-motion, JavaScript-disabled navigation, direct-file preview, and article print/forced-color checks passed. Desktop and mobile screenshots were inspected.

Tom subsequently changed the cursor to infinite blinking and the article H1 to bold, then confirmed that the result looks good. Current CSS inspection verifies both changes and the reduced-motion override. Browser checks have not been rerun after these edits; the previous bounded-cursor assertions no longer apply. A pause/hide control, assistive-technology testing, and final content checks remain before publication.

## Next action

In the next session, read the linked definition, layout, and content documents, inspect `design-preview/index.html`, `article.html`, `styles.css`, and `preview.js`, then verify Git state. Do not rely on temporary test scripts or screenshots under `/tmp` surviving.

Obtain explicit source/configuration edit approval for the first Hugo conversion unit. Start with the pinned toolchain, shared shell, homepage, and article templates, including the accepted responsive TOC. Remaining launch inputs do not block this unit. Do not reopen settled choices or choose a newer Hugo version merely because one exists; surface any material compatibility or security conflict first.

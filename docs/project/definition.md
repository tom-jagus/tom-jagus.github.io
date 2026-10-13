# Website rewrite

## Purpose

Rebuild Tom Jagus's personal website to reflect the current brand identity, replacing its outdated layout, content, and assets. The site should connect Tom's perspective, projects, writing, and consulting without implying work or experience that does not yet exist.

## Agreed requirements

- Keep the website in this GitHub repository and host it on GitHub Pages.
- Use custom layouts with [Hugo Extended 0.167.0](https://github.com/gohugoio/hugo/releases/tag/v0.167.0), pinned exactly in local tooling and GitHub Actions. Use ordinary Extended, not `extended_withdeploy`; GitHub Actions publishes the artifacts.
- Store editorial content in Markdown plus frontmatter. Keep templates, configuration, and assets separate.
- Generate static HTML through GitHub Actions on push.
- Use `https://tom.jagus.me` as the production domain.
- Use the brand identity at `~/src/default/brand-identity` as the reference for messaging, services, visual rules, and supplied assets.
- Plan a full rewrite rather than incremental changes to the existing Blowfish presentation.
- Prepare the work on a separate branch before implementation.

## Agreed approach

Maintain a small set of custom layouts with plain CSS. Remove Blowfish entirely, including its editorial shortcodes and theme-specific settings. The plain-CSS approach does not need a separate Dart Sass installation. Upgrade Hugo deliberately after build checks, rather than track an unpinned latest release.

The accepted [content structure](../design/content.md) owns folders, minimal YAML frontmatter, curated homepage projects, automatically selected recent writing/videos, and shared service/contact introductions. Projects use a flat `github_url` field and optional image metadata. Writing has an optional generated TOC, sticky on the right at wide widths and collapsible above the body on narrow screens.

Use the supplied wordmark, illustrated avatar, JetBrains Mono, and Catppuccin Mocha color roles. Design a responsive, dark-first site with minimal JavaScript. The brand's visual reference guides appearance but does not prescribe the page layout.

Use the personal-introduction homepage with selected work, latest writing, recent videos, a service introduction, and contact invitation. The separate pages are About, Work, Writing, Services, and Contact. Work lists project write-ups; Writing lists articles and notes. Services presents the five current offers on one page. Omit empty collections and navigation destinations at launch.

Use a visible Contact link styled like the other header navigation links and contextual invitations elsewhere, without heavy sales prompts on every page. Put confirmed social profile links in the footer with SVG icons and text labels. Start with video thumbnails and external watch links, plus conditional, manually maintained stream announcements. Automatic live detection and a dedicated player page are deferred.

The accepted [layout brief](../design/layout.md) owns page structure, URL conventions, video and stream presentation, contact placement, and visual defaults. It records the accepted avatar-first introduction, heading colors, sticky transparent-to-blurred header, mobile navigation overlay, scroll-dependent background blur, and solid footer. Use the reviewed homepage and article designs as the basis for other page types, and verify their behavior with final content.

Deploy build artifacts rather than commit generated HTML. Keep selected brand assets in this repository with their source recorded, without making deployment depend on the brand repository.

The initial release contains Home, About, Services, and Contact. Keep Work, Writing, and Video samples unpublished until real content is reviewed. Search indexing is enabled for published pages. Do not preserve legacy URLs for this release, as Tom requested. The automated test suite is removed; retain the pinned toolchain, warning-failing production build, and manual output/browser review.

Use Reach out links to Contact and an Email me button only on Contact. Omit the initial-message warning at Tom's request. Social sharing uses the circular avatar on a 1200 by 630 Mocha background.

## Boundaries

- Apply the existing brand rather than redesign it.
- Follow its claim and confidentiality boundaries, including the limited, human-led AI offer.
- Do not invent projects, testimonials, outcomes, or a publishing history.
- A CMS, database, application backend, and full light theme are not needed for the first release.
- Creating project documents does not authorize implementation, commits, or publication.

## Completion criteria

- The reviewed site content and assets match the current brand.
- Routine content updates require Markdown edits, not template changes.
- The site works on mobile and with keyboard navigation, readable contrast, and enlarged text.
- Production builds exclude drafts and have no broken internal links.
- Metadata, canonical URLs, sitemap, and RSS where relevant are checked. Legacy URL removal is intentional.
- GitHub Actions builds and deploys the reviewed site to GitHub Pages.

See [progress and action plan](progress.md) for the current state and next steps.

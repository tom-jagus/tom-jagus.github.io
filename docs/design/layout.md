# Website layout brief

## Status and references

Tom approved the static homepage and article designs, including continuous cursor blinking and a bold article title. Tom also accepted a desktop-right/mobile-collapsible article TOC. The Hugo reading template now implements that TOC. The original static design study is archived outside the repository; Hugo's draft server is the current preview. Tom also accepted full-width list layouts and left-aligned reading content, retaining a readable paragraph measure rather than full-width long paragraphs. Home, About, Services, and Contact are approved for the initial release. Services uses the article-style side TOC, and Work has an image-led index with stage boxes and repository links near titles. Work and Writing retain unpublished samples for later content work. Dimensions below are reviewed starting points, not fixed acceptance values.

The [project definition](../project/definition.md) owns scope and technology. Use `~/src/default/brand-identity/docs/brand/` for identity, messaging, services, visual usage, and asset handoff. Consult `docs/kits/channels.md` in that repository for website guidance. Its `samples/identity.html` is a visual reference, not a required layout or the source of current copy.

The [content structure](content.md) records the accepted folders, frontmatter, optional project images, and responsive TOC behavior.

## Site structure

The site balances personal perspective, public work, writing, and consulting. Use these pages and paths:

| Page | Path | Purpose and layout |
| --- | --- | --- |
| Home | `/` | Personal introduction followed by selected material and contact routes. |
| About | `/about/` | A personal essay with a readable paragraph measure and the avatar near the opening. Cover perspective, background, exploration, and client work without repeating the homepage introduction. |
| Work | `/work/` | Full-width entries with a bundle image or shared abstract default, title, nearby repository link, short description, and a labelled stage box. Stack image and copy on narrow screens. |
| Project | `/work/project-name/` | Use the reading layout, with a repository link directly below the title and the same labelled stage box as the index. Explain the problem, constraints, contribution, choices, results, and limitations where relevant. |
| Writing | `/writing/` | A simple list of articles and notes with descriptions and dates. Use the label Writing, not Articles or Blog. |
| Article | `/writing/article-title/` | A readable article with a description above the title, relevant date, and narrow body column. Keep dates out of URLs. |
| Services | `/services/` | One page with the service introduction and five current offers. List the offers in the same desktop-right/mobile-collapsible TOC as articles, excluding H3 subsections. Keep the final contact invitation full-width. |
| Contact | `/contact/` | A short personal invitation and an Email me button that opens the email client. No form or initial-message warning. |

Project pages describe projects. Writing explores subjects and lessons, with links to related projects rather than duplicate write-ups. Do not add index filters until content volume warrants them.

For writing with `toc: true`, generate the contents from Markdown headings. On wide screens, use a restrained sticky right-hand column, offset below the header, without reducing the reading width. On narrow screens, use a collapsible contents block above the body. Omit the TOC by default, and do not render an empty contents list. Project pages may also have contents navigation where useful. Images, diagrams, and code can extend wider than prose. Match the homepage's outer container and left alignment for reading titles and body content, with paragraphs around 60–65 characters wide. Without a TOC, reserve no sidebar and allow figures/code to use the full container. List headings and entries span the full container. Do not force every project into identical headings.

The intended structure includes Work and Writing, but do not launch empty pages or navigation destinations. Publish those collections when they have reviewed entries. Tom chose not to preserve legacy URLs; the [old URL inventory](old-urls.md) remains a historical reference.

## Shared header and footer

Use the complete supplied SVG wordmark as the home link, not an icon combined with recreated text. Use the wordmark at 196px full-canvas width as in the reviewed preview. The header contains About, Work, Writing, Services, and Contact, all as ordinary navigation links. Reserve filled buttons for actions such as Email me. No separate Home item is needed. Use a full-width sticky header that starts transparent and gains a Mantle-tinted blur over the first part of scrolling. Keep its contents within the page width and offset anchor destinations below it. On narrow screens, use a full-screen translucent, blurred navigation overlay with right-aligned links and a top close button. Support Escape, contained keyboard focus, focus restoration, close-on-selection, and background scroll locking. Keep ordinary navigation visible when JavaScript is unavailable.

Use a solid, full-width Mantle footer with its contents constrained to the page width. The footer contains the name, brand line, confirmed profile links in the order YouTube, GitHub, X, LinkedIn, RSS when available, and copyright text. Do not add a separate footer Contact link or prototype explanations. Use small SVG platform icons alongside visible text labels. Keep their colors consistent with the site and their emphasis secondary. Provide comfortable targets and visible keyboard focus. Open links in the same tab by default.

Do not use icon-only social navigation, a floating social bar, or a full set of profile links in the introduction. Add contextual links where useful, including repositories on project pages and the YouTube channel below videos. The Contact page can have an Elsewhere list; email remains the primary contact route.

## Homepage

Use the personal-introduction layout with selected work, in this order:

1. Shared header.
2. Conditional stream announcement, only when there is a confirmed event to show. Omit it until the notice fields and expiry behavior are agreed.
3. Introduction with the brand line "Designing better ways of working.", the approved written introduction, and circular avatar. Keep prose left aligned, not justified. Center the avatar first, with a bold lavender headline below it. Add a small decorative full-block cursor at the end. It blinks continuously on a 1.2-second cycle; reduced motion keeps it still. Keep the bio left aligned within a centered reading column and center the introduction links. Reviewed portrait sizes are 260px on wide screens, 220px at intermediate widths, and 176px on narrow screens. Use About me and Explore my work links where their destinations exist.
4. Selected work, initially up to two restrained text-only project cards with explicit links. Custom or shared default project images belong on the Work index, not these homepage cards.
5. Latest writing, as a short list rather than a card grid.
6. Recent videos, initially up to two thumbnail entries.
7. Work with me, with a heading spanning the section. Below it, align the introduction and service-list columns at the same starting height. Include an Explore services link in the final site.
8. The general contact invitation in a blue-tinted panel with a blue Reach out button linking to Contact and Mantle button text. On wide screens, put the invitation on the left and the button on the right. Stack on narrow screens. Do not display the email address or an initial-message warning in this panel.
9. Shared footer.

Omit collections without publishable content. Do not add placeholders to imply a portfolio, publication history, or schedule. Keep the professional title in service-related contexts rather than leading every page with it.

## Videos and livestreams

Videos have their own homepage section rather than appearing under Writing. Show a thumbnail, title, short description, format label, and watch link. Distinguish edited videos from livestream recordings. Link to More videos on YouTube; no dedicated video archive is needed initially. A relevant video may also appear on a project or article page without requiring a duplicate article.

Use thumbnails and external links on the homepage, not multiple embedded players. In the Hugo implementation, each video has its own Markdown file with frontmatter for title, description, publication date, thumbnail, external URL, and format. The homepage selects the latest published entries automatically; adding a video must not require editing homepage Markdown. Treat videos as an internal content collection without public `/videos/` index or individual video routes. Control feed and other listing inclusion explicitly. The current Hugo video bundles use labelled drafts for private layout review. Automatic channel synchronization is not part of the initial scope.

Use a conditional announcement rather than a permanent livestream section:

- Upcoming events show a confirmed topic, date, timezone, and stream link.
- A verified live event can show its title and a Watch live link.
- Selected completed streams appear in Recent videos as livestream recordings.

Start with manually maintained announcements and links. A schedule alone must never produce a Live now claim. Static builds cannot establish current live status, and manual notices need removal when the event ends. Choose the exact notice fields and expiry behavior before implementation.

Automatic live detection and a dedicated `/live/` page are deferred options, not initial requirements. If added later, use a click-to-load player, external watch link, and useful offline state. Do not autoplay or insert a large player into the homepage. The livestream platform remains unconfirmed.

## Contact emphasis

Keep Contact visible in the header. Use Reach out for actions that open Contact. Only Contact has an Email me button with a mailto link to `contact@jagus.me`. If Contact is excluded from a build, omit its navigation link and contextual invitations rather than display a direct-email fallback.

Place the general invitation near the end of Home and About. Services gets the service-specific invitation after the offers. Project pages may include a relevant invitation; articles should use a quiet discussion invitation rather than a sales panel. Avoid repeated, heavy sales prompts.

Do not promise response times, availability, or social messaging without confirmation.

## Visual and accessibility defaults

- Use the supplied wordmark, circular illustrated avatar, JetBrains Mono, and established Catppuccin Mocha color roles. CSS now exposes all 26 Mocha colors; existing `--surface` and `--muted` roles alias Surface0 and Subtext0. Availability does not make every accent a default. Do not recreate the wordmark. Tom approved a website-specific exception for a favicon using the original three strokes. Keep their geometry, spacing, rounded caps, and colors. The favicon uses a rounded Mocha Base background for light/dark tab contrast; the full header wordmark remains unchanged. This exception does not authorize other standalone-icon uses.
- Start around 1,040px overall width and 60 characters for reading text, within the brand's 45–65 character range. Test 16–18px body text with generous line spacing and a real long article.
- On Home, use a bold lavender headline. Reserve mauve for the Selected work, Latest writing, Recent videos, and Work with me section headings. Work-card titles follow their panel accent; writing and video titles use normal text color. Keep the contact heading, panel tint, and button blue.
- In articles, use bold lavender for H1 and mauve for H2 headings. Use teal for H3–H6, distinct from H2. Blockquotes have blue text with a matching blue-tinted background and border. Keep body text in its normal role. These website-specific color choices do not assign meanings to service colors.
- Reserve Mantle panels with subtle tint and uniform borders for deliberate emphasis. Start around 13px corner radii. Do not color-code services or add top stripes.
- Use underlined text links and filled buttons for important actions. The contact action uses blue; lavender remains the default button color. Static cards should look static and contain clearly labeled links.
- Use a fixed, full-viewport background inspired by the YouTube banner's geometry, shared across pages. Use broad rounded paths and boxes, primarily blue with restrained teal/lavender/peach accents, and low contrast. Keep the central reading area quieter, and use a simpler mobile composition. The artwork contains no banner lettering and does not stretch over the document height. This replaces the earlier introduction-only decoration. On Home, gradually blend into modestly blurred artwork over the first 300px of scrolling; other pages start blurred. Keep foreground content sharp. With reduced motion, leave the artwork blurred and avoid gradual header interpolation. Avoid glow, busy imagery, animated typing text, carousels, parallax, and scroll-reveal animation. The headline's decorative cursor does not reveal or replace the text.
- Continuous cursor blinking needs a pause or hide control before publication. The Hugo homepage now has a keyboard-operable pause toggle and keeps the cursor still without JavaScript or with reduced motion. The archived static study had only a reduced-motion fallback; it is not the current implementation.
- Stack columns before text becomes cramped. Check keyboard navigation, visible focus, 44px button targets, 320px reflow, 200% text enlargement, 4.5:1 text contrast, and 3:1 meaningful control/focus contrast. A full light theme is not required.

## Publishing and later work

Shared page headers show draft review notices in Mocha red above the peach descriptions, followed by the page titles. Published pages omit the notices. The homepage keeps its own introduction layout.

The avatar is the supplied JPEG displayed with the existing circular CSS crop. Social sharing uses the same crop as a circle centered on a 1200 by 630 Mocha background; see [asset sources](assets.md).

Social profile URLs are supplied in site configuration. Work, Writing, and Videos remain unpublished until they have real reviewed entries. The livestream platform and announcement behavior remain undecided; do not display notices until they are agreed. Further implementation requires its own approval.

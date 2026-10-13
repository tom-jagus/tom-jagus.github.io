# Content and frontmatter structure

## Status

Tom accepted the folder structure, simple YAML frontmatter, homepage selection rules, shared introductions, and separation of editorial content from presentation. The custom homepage/article templates now use this contract. The old Blowfish content and duplicate/generated files have been removed from the working tree. Original content remains in Git history; see the [old URL inventory and recovery instructions](old-urls.md).

The homepage selection rules, `github_url`, internal video collection, and responsive generated TOC are implemented. Services now lists only its five H2 offers in the same responsive side TOC. The Work index supports bundle images with a shared abstract fallback; index entries and project pages share stage boxes and repository links near titles. These layout changes await visual review. Launch copy and old-link handling are still outstanding.

## Accepted folders

```text
content/
├── _index.md
├── about.md
├── services.md
├── contact.md
├── shared/
│   ├── _index.md
│   ├── services.md
│   └── contact.md
├── work/
│   ├── _index.md
│   └── project-name/
│       ├── index.md
│       └── diagram.png
├── writing/
│   ├── _index.md
│   └── article-title/
│       ├── index.md
│       └── illustration.png
└── videos/
    ├── _index.md
    └── video-name/
        ├── index.md
        └── thumbnail.jpg
```

Project, writing, and video entries use page bundles so their assets stay with their Markdown. Asset filenames above are examples, not required files. Folder names determine public page paths without dates. Videos are the exception, an internal collection with no public index or individual routes.

The homepage Markdown body holds its introduction. Services remains one page with the five offers as sections. Index Markdown bodies hold their collection introductions.

About, Contact, and Services now have dedicated layouts and draft sample bodies. Work/Writing indexes and sample bundles also remain drafts for local review. Change a collection index from draft only when it has reviewed launch entries.

Internal `shared/services.md` and `shared/contact.md` keep the reusable introductions available independently of those page drafts. Their collection cascades `build.render: never`, `build.list: never`, and `build.publishResources: false`, so it generates no routes, feed items, or assets. These sources remain non-draft and hold the existing approved short copy.

## Accepted frontmatter

Every editorial entry has `title`, `description`, and `draft` in YAML. Start unpublished entries with `draft: true`. Use `layout` only when a page needs a dedicated template. The Markdown body contains the substantive content, without layout shortcodes. Use `aliases` only to preserve confirmed useful old URLs.

| Content | Additional fields |
| --- | --- |
| Projects | `date` for first publication, `status` for the displayed stage, and a flat `github_url` when a public repository exists. Optional `image`; provide `image_alt` when using a custom bundle image. Do not use a nested `links` list. |
| Writing | `date` for first publication. Optional `lastmod` for substantive updates and `toc` to enable a generated contents list. |
| Videos | `date`, `watch_url`, `thumbnail`, and `format`. Use `video` or `livestream-recording` for the format. A body is not needed initially. |
| Shared service/contact copy | A Markdown-enabled `intro` field for short copy reused by other templates. Shared Services H2 headings supply homepage offer names; the shared Contact title supplies the invitation heading. |
| Services page | Optional `contact_heading` and Markdown-enabled `contact_intro` for the service-specific invitation. |
| Review samples | Optional `review_note` to explain that the draft uses sample copy. It is displayed only when `draft: true`. |

Hugo's native `url` overrides the generated page address; do not use it for an external GitHub or video link. Video entries use the accepted `watch_url` field. Projects use `github_url`, supplied when a public repository exists.

## Accepted selection and shared configuration

- Homepage `selected_work` lists project page paths in the desired order. No project-level featured flag or ranking field is needed.
- Latest writing and Recent videos each select up to two published entries automatically, newest publication date first. Adding an entry does not require a homepage edit.
- Omit empty collections and their navigation destinations. Do not use review samples as launch content.
- Configure the internal video collection to keep entries/assets available to templates without generating public pages. Exclude it explicitly from feeds and unrelated listings.
- Reuse service/contact `intro` fields rather than duplicate their short copy in homepage Markdown.
- Keep identity assets, email address, social URLs, navigation configuration, and default metadata outside editorial Markdown. Keep colors, typography, and section layout in CSS/templates.

## Accepted images and table of contents

### Project images

Tom requested a universal project image for the Work index, replacing the earlier no-placeholder rule. A custom `image` resolves relative to its page bundle and requires a non-empty `image_alt`. Missing files or alt text fail the build. Without `image`, the index uses `static/site/project-default.svg`, a decorative abstract diagram with empty alt text, not a project screenshot. Keep homepage work cards text-only. Images in a write-up remain ordinary Markdown images and do not require a frontmatter image.

The existing `status` field supplies the same labelled stage box on the index and project page. Planned uses blue, In progress peach, Complete/Completed green, Maintained teal, Paused yellow, and Archived a neutral tint. Other text is retained with neutral styling; these are presentation conventions, not a required status vocabulary. Missing status or repository links are omitted rather than invented.

### Table of contents

Use Hugo's generated `.TableOfContents` when `toc: true`, rather than maintain a separate list of links. The default is off, with authors enabling it when useful.

Services always generates its contents from H2 offers only, excluding the repeated H3 contribution/output/boundary headings. It shares the article contents component and responsive behavior.

On wide screens, put the TOC in a restrained sticky right-hand column, offset below the header, while preserving the reading width. On narrower screens, move it above the article body as a collapsible contents block. Short entries omit it by default. Do not render a TOC when no usable headings exist.

Reading titles and paragraphs align with the homepage container's left edge. Paragraphs stay around 60 characters wide; figures and code can use the content area's full width. No sidebar is reserved without a TOC. List headings and rows span the full container.

The Hugo reading template now implements the TOC arrangement using one generated contents list. With JavaScript, the native details block starts closed on narrow screens and open on wide screens; without JavaScript it stays open. The original static study is archived outside the repository; use Hugo's draft server for current review.

See the [layout brief](layout.md) for visual choices and [project progress](../project/progress.md) for implementation status and remaining inputs.

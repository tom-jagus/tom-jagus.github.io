# Content and frontmatter structure

## Status

Tom accepted the folder structure, simple YAML frontmatter, homepage selection rules, shared introductions, and separation of editorial content from presentation. This is the contract for the future custom Hugo templates, not the current implementation. Remove Blowfish and its editorial shortcodes/settings during conversion.

Tom also accepted `github_url`, optional project images, and the responsive TOC arrangement below. These choices are settled, but have not been implemented in Hugo.

## Accepted folders

```text
content/
├── _index.md
├── about.md
├── services.md
├── contact.md
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

## Accepted frontmatter

Every editorial entry has `title`, `description`, and `draft` in YAML. Start unpublished entries with `draft: true`. Use `layout` only when a page needs a dedicated template. The Markdown body contains the substantive content, without layout shortcodes. Use `aliases` only to preserve confirmed useful old URLs.

| Content | Additional fields |
| --- | --- |
| Projects | `date` for first publication, `status`, and a flat `github_url` when a public repository exists. Optional `image` and `image_alt`. Do not use a nested `links` list. |
| Writing | `date` for first publication. Optional `lastmod` for substantive updates and `toc` to enable a generated contents list. |
| Videos | `date`, `watch_url`, `thumbnail`, and `format`. Use `video` or `livestream-recording` for the format. A body is not needed initially. |
| Services and Contact | A Markdown-enabled `intro` field for short copy reused by other templates. |

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

Use optional `image` and `image_alt` fields. Resolve the image relative to its page bundle. Use it on the Work index when available; omit the image area when absent, without a generic placeholder. Keep the approved homepage work cards text-only. Images in a write-up can remain ordinary Markdown images and do not require a frontmatter image.

### Table of contents

Use Hugo's generated `.TableOfContents` when `toc: true`, rather than maintain a separate list of links. The default is off, with authors enabling it when useful.

On wide screens, put the TOC in a restrained sticky right-hand column, offset below the header, while preserving the reading width. On narrower screens, move it above the article body as a collapsible contents block. Short entries omit it by default. Do not render a TOC when no usable headings exist.

This accepted arrangement replaces the inline TOC in the future Hugo layout. The static preview still has its original inline TOC; do not mistake design approval for completed implementation.

See the [layout brief](layout.md) for visual choices and [project progress](../project/progress.md) for implementation status and remaining inputs.

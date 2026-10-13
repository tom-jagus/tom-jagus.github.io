---
title: "Choosing a simpler publishing workflow"
description: "Private article layout sample about separating content, design, and publishing. Not a published article."
date: 2026-01-01
lastmod: 2026-01-02
draft: true
toc: true
---

This is draft text for reviewing typography and page structure. It is not a published article or an account of completed work. Dates are illustrative.

## Start with the publishing task

A personal website needs to explain who someone is and make their work easy to find. Its publishing process should make a small correction easy, too. Changing a paragraph should not require understanding the entire design.

Before choosing a framework, it helps to describe the ordinary task. Write a piece, preview it, review the result, and publish it. The interesting question is where that process needs support and where another tool would simply add a step.

For a site built from files, version control provides a record of changes. A static site generator turns those files into pages. Neither choice removes the need to check that the words, links, and images make sense to a reader.

> Changing the content should not mean rebuilding the design.

This is a design aim, not a guarantee. A new kind of content can still need a new layout. The aim is to make routine writing independent of that work.

## Keep content and presentation separate

Markdown can hold the prose. A small amount of frontmatter can describe a title, summary, date, and publication state. Templates decide how those fields appear, while CSS controls their visual treatment.

That separation gives each change a clear home:

- Edit the Markdown when the explanation needs to change.
- Edit a template when a page needs different structure.
- Edit shared styles when spacing or typography needs adjustment.
- Keep images and other assets separate, with meaningful filenames and alternative text where needed.

A frontmatter field is useful when the site actually uses it. A long list of unused settings makes a new article harder to start without improving the result.

```markdown
---
title: "A clearer publishing workflow"
description: "Notes on content and presentation."
draft: true
---

## Start with the task

Write the explanation before styling the page.
```

The `draft` field makes publication intent explicit. It still needs a production build that respects it. A field without the corresponding behavior does not protect unpublished work.

![Illustrative flow from Markdown through static generation to GitHub Pages.](workflow.svg "Private layout diagram. This does not describe a completed deployment.")

## Keep enough context to continue

The source files show what exists. They do not always explain why it exists or which choices are still open. A short project definition and a current progress note can preserve that information without becoming a record of every edit.

Useful context answers concrete questions. What is the site for? Which choices have been accepted? What remains uncertain? What would be a sensible next action?

For example, deciding to use Markdown is different from deciding how video entries should work. One establishes the authoring format. The other needs fields, links, and a layout that the generator can use.

### Leave room for the unknown

An open question should stay open until there is enough information to resolve it. A sample video title can help review a card layout, but it should not become a claim that the video exists. Likewise, a scheduled stream does not establish that someone is currently live.

Labels matter during review. They let a reader distinguish approved copy from a draft and a real project from a layout example. Before publication, the remaining examples need to be replaced or removed.

## Check the result where it matters

A successful build confirms that the generator produced output. It does not establish that the site is readable, accessible, or accurate. Those need checks against the rendered pages and their actual content.

1. Read a long page at a comfortable text size. Check whether the line length makes it easy to follow.
2. Use the navigation without a mouse. Links should have visible focus and understandable names.
3. Try a narrow viewport and enlarged text. Paragraphs should reflow; wider code examples can have their own scrolling region.
4. Follow internal links and confirm that drafts do not appear in the production output.

The smallest useful publishing system is the one that supports these tasks without requiring unrelated maintenance. The site can grow when a new need becomes clear.

### Smaller headings

This section checks the teal treatment for headings below H2.

#### A fourth-level heading

The generated contents can include this level when it helps the reader.

##### A fifth-level heading

Small headings remain part of the prose without making the contents list too long.

###### A sixth-level heading

All heading levels should remain readable at narrow widths and enlarged text sizes.

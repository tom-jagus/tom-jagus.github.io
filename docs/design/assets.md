# Website asset sources

The custom templates publish `static/site/`. The build does not depend on the brand repository or an external font/asset service.

| Repository file | Source |
| --- | --- |
| `static/site/wordmark.svg` | Unchanged `~/src/default/brand-identity/assets/wordmark/tom-jagus-colour.svg`, retained from the approved design study. |
| `static/site/avatar.jpg` | JPEG replacement supplied by Tom, 1086 by 1448 pixels and approximately 112 KB. It replaces the original PNG. The circular crop remains CSS with `object-position: 50% 5%`. |
| `static/site/social-share.jpg` | 1200 by 630 JPEG generated from the supplied avatar. The website's square crop is masked to a 560-pixel circle and centered on Mocha Base. Open Graph and Twitter card metadata use this image. |
| `static/site/background.svg` and `background-mobile.svg` | Decorative compositions created for the approved design study, inspired by the brand's YouTube banner. Retained unchanged; they contain no banner lettering. |
| `static/site/fonts/JetBrainsMono-Regular.ttf` and `JetBrainsMono-Bold.ttf` | Unchanged design-study copies of the former `static/fonts/` files at commit `4292a28`. The unused font variants and duplicate collection were removed. |
| `static/site/fonts/OFL.txt` | Matching JetBrains Mono copyright notice and SIL OFL 1.1 license, retained unchanged from the study's copy of the installed font package license. |
| Inline social SVGs in `layouts/_partials/social-icon.html` | Preview layout illustrations, with a simple RSS icon added for the feed. Confirm final platform artwork before publication. |
| `static/site/project-default.svg` | New decorative workflow/component diagram in Mocha colors, requested as the universal Work-index fallback. It is not a screenshot, a supplied identity asset, or evidence of a completed project. |
| `static/site/favicon.svg` | Original three accent paths from the wordmark, centered on a rounded Mocha Base square. Geometry, spacing, rounded caps, and Peach → Teal → Lavender order are unchanged. Tom approved this website-specific exception; it does not replace the full header wordmark or authorize general icon use. |
| `static/site/favicon.ico` | 16px, 32px, and 48px fallback images rasterized from the favicon SVG with `rsvg-convert` and assembled with ImageMagick. Both formats are linked from every HTML page, including subpath builds. |

`assets/css/site.css` and `assets/js/site.js` adapt the approved preview styles and interactions for Hugo. Stylesheet asset URLs are relative to the generated CSS directory so deployment under a path prefix also works. Hugo minifies and fingerprints both files.

The SVGs in draft article/video bundles are new, labelled private layout examples. They are not brand delivery assets or evidence of completed publishing work. Production builds omit those bundles and resources.

The obsolete static collection, old image assets, and generated copies have been removed. The untracked design study was archived outside the repository after verifying all seven retained asset files against it; see [recovery instructions](old-urls.md#historical-content-and-design-recovery). No old favicon is carried into the rewrite. The new favicon is implemented under Tom's approved website exception; the external brand guidance has not been edited. The avatar now uses Tom's smaller JPEG, and the sharing image derives from it. Font files and site backgrounds are unchanged. Tom rejected and removed the root-level background experiments.

## Sharing image maintenance

Regenerate the stored image with ImageMagick from the repository root. The 1086-pixel square begins 18 pixels below the top, matching the website's 5% vertical position within the 362 pixels removed by the square crop. No portrait pixels are stretched or enlarged.

```bash
folder=$(mktemp -d)
magick static/site/avatar.jpg -crop 1086x1086+0+18 +repage -resize 560x560 "$folder/crop.png"
magick -size 560x560 xc:black -fill white -draw 'circle 279.5,279.5 279.5,0' "$folder/mask.png"
magick "$folder/crop.png" "$folder/mask.png" -alpha off -compose CopyOpacity -composite "$folder/circle.png"
magick -size 1200x630 'xc:#1E1E2E' "$folder/circle.png" -gravity center -compose Over -composite -strip -quality 90 static/site/social-share.jpg
rm -r -- "$folder"
```

This command assumes the current portrait dimensions. If the source dimensions or website crop change, adjust the crop and check the result before replacing the sharing image. The site build publishes the stored JPEG and does not require ImageMagick.

## Favicon maintenance

The SVG is the source. Rasterizers are only needed to regenerate the stored ICO, not to build the site:

```bash
folder=$(mktemp -d)
for size in 16 32 48; do
  rsvg-convert --width "$size" --height "$size" static/site/favicon.svg -o "$folder/$size.png"
done
magick "$folder/48.png" "$folder/32.png" "$folder/16.png" static/site/favicon.ico
rm -r -- "$folder"
```

The dark square keeps the pastel strokes legible on light browser tabs without recoloring them. No app manifest or unrelated icon variants are added.

The font license applies to the fonts. It does not grant reuse rights to the personal brand assets or the repository as a whole. Follow the brand's `docs/brand/asset-handoff.md` and `visual-usage.md` for identity asset use.

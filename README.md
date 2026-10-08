# AltaCoco Home — website

Static site built from `AltaCoco_Home_website_copy.md`. Plain HTML, CSS, and a small amount of JavaScript — no build step, no dependencies.

## Run locally

From this `site` folder, start any static file server and open the address it prints:

```bash
cd ~/Documents/altacoco/site
python3 -m http.server 8080
# then open http://localhost:8080
```

(Opening `index.html` directly by double-clicking also works, but a local server matches how the site behaves once hosted.)

## Pages

| File | Page |
|---|---|
| `index.html` | Home |
| `about.html` | About |
| `services.html` | Services (anchors: `#sourcing`, `#styling`, `#planning`, `#procurement`, `#research`) |
| `lookbook.html` | Lookbook — 4 concepts, each labeled Editorial Concept / Design Study |
| `editors-choice.html` | Editor's Choice — 13 category filters, 10 placeholder picks |
| `editors-choice/deep-sectional-family-living.html` | Product post template (the example post from the brief) |
| `journal.html` | Journal — all suggested article titles listed, one live article |
| `journal/how-deep-should-a-sofa-be.html` | Sample article |
| `contact.html` | Contact form |
| `faq.html` | FAQ |
| `privacy.html`, `terms.html` | Placeholder legal pages |

Shared files: `assets/styles.css` (all styling) and `assets/site.js` (mobile nav, category filter, contact form).

## Adding real photos

Every image slot is wired to a filename in `images/` (the hero photo is in; the rest show placeholders). Open `images/SHOT-LIST.md` — it lists all 37
filenames, the size and ratio each needs, where it appears, what it should show, and suggested search terms.
Save a photo with the matching filename and it replaces the placeholder automatically; add them a few at a time. Then run `images/optimize-images.sh` to shrink
oversized files (macOS, nothing to install).

## Editing content (Editor's Choice, Journal, page copy)

The HTML is generated from the Python sources in `_source/`:

- `_source/products.py` — the 12 Editor's Choice products (brand, product, price, dimensions, materials, retailer URL, and the editorial sections). `CHECKED` is the price-verification date shown on every post.
- `_source/articles.py` — the 14 Journal articles.
- `_source/picks.py` — the Unsplash photo picks (regenerates `images/PHOTO-PICKS.md` and `download-photos.sh`).
- `_source/build.py` — page copy and templates for every page.

To change anything, edit the relevant file and run from the `site` folder:

```bash
python3 _source/build.py
```

It rewrites all the `.html` files in place. (Set `OUT` at the top of `build.py` to the `site` folder path if you move things.)
Editing the `.html` files directly also works for small copy changes, but the next build will overwrite them.

## Before launch (from section 17 of the brief)

- Contact form: it currently opens the visitor's email app addressed to `cs@altacoco.com` with the fields filled in. Swap in a form service (Formspree, Netlify Forms, Basin, etc.) in `assets/site.js` — see the comment there.
- Re-check Editor's Choice prices periodically and update `CHECKED` in `_source/products.py`.
- Replace Privacy and Terms placeholder text with reviewed policies.
- Add social links to the footer if wanted.
- Fonts load from Google Fonts (Fraunces + Inter). To self-host, download them and update the `@font-face` / `<link>` in each page.

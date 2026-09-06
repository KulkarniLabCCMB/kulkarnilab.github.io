# BiomE Lab website

Static site for the Biodiversity Genomics & Evolution (BiomE) Lab,
CSIR-Centre for Cellular and Molecular Biology, Hyderabad.

No WordPress, no database, no plugins to update. Just files. GitHub serves them
for free and there is nothing that can be hacked or that will silently break.

---

## Putting it on GitHub

You only do this once.

1. **Make the repository.** On github.com, click **New repository**. Name it
   `sskspider.github.io` if you want the free `sskspider.github.io` address, or
   anything else (say `biome-lab`) if you are keeping the sskspider.com domain.
   Make it **Public**. Do not add a README — this folder already has one.

2. **Upload the files.** On the empty repository page click
   **uploading an existing file**, then drag in *the contents of this folder* —
   all the `.html` files plus the `assets`, `data` and `_tools` folders. Click
   **Commit changes**.

   The upload box sometimes skips files whose names start with a dot. If
   `.nojekyll` does not appear in the repository afterwards, use
   **Add file → Create new file**, type `.nojekyll` as the name, leave it empty
   and commit. Without it GitHub tries to run Jekyll and ignores the `_tools`
   folder.

3. **Turn on Pages.** Repository **Settings → Pages**. Under *Source* choose
   **Deploy from a branch**, branch `main`, folder `/ (root)`. Save. A minute
   later the site is live.

4. **Point sskspider.com at it.** Still in Settings → Pages, type
   `sskspider.com` into *Custom domain* and save. Then at your domain registrar
   set these DNS records:

   | Type  | Name  | Value                  |
   |-------|-------|------------------------|
   | A     | @     | 185.199.108.153        |
   | A     | @     | 185.199.109.153        |
   | A     | @     | 185.199.110.153        |
   | A     | @     | 185.199.111.153        |
   | CNAME | www   | `sskspider.github.io.` |

   Replace `sskspider` in the CNAME value with your GitHub username if it
   differs. DNS takes anywhere from ten minutes to a day. Once it resolves,
   tick **Enforce HTTPS** on the Pages settings page.

5. **Keep the old site up** until the new one resolves, then retire it. Do not
   cancel WordPress hosting before HTTPS is working here.

---

## Editing the site

Everything that changes often lives in `data/`. You can edit those files
directly on github.com — open the file, click the pencil icon, change it,
click **Commit changes**. The site updates in about a minute.

| To change | Edit |
|---|---|
| Lab news | `data/news.js` |
| Members and alumni | `data/people.js` |
| Ongoing projects | `data/projects.js` |
| Publications | `data/publications.js` |
| Page text (research, join, contact…) | the matching `.html` file |
| Colours, fonts, spacing | the `:root` block at the top of `assets/css/style.css` |

Each data file starts with a comment explaining its fields. The general shape:
copy the entry at the top, change the values, leave the commas and braces alone.

**Posting news** — add this at the top of the list in `data/news.js`:

```js
{
  date: "October 2026", sort: 202610,
  body: "Welcome <strong>Name</strong> to the lab."
},
```

`sort` is the year and month as a number, and it is what keeps the order right.
Two items in the same month can use `202610.2` and `202610.1`.

**Adding a paper** — add this at the top of the list in `data/publications.js`:

```js
{
  n: 43, year: 2026, status: "",
  authors: "<b>Siddharth Kulkarni</b>*, <u>Lab Member</u>, Coauthor",
  title: "Title of the paper",
  venue: "Journal Name", detail: "12(3): 45–67",
  tags: ["genomics", "acari"], url: "https://doi.org/…"
},
```

`<b>` marks you, `<u>` marks a lab member, and both are explained in the
legend on the page. `status` can be `"submitted"`, `"preprint"` or `"in press"`.
Tags drive the filter buttons; use the ones already in the file.

Most of the older papers have `url: ""` because I did not want to guess DOIs.
Filling them in from your Scholar profile is a good hour's work for a student
and makes every title clickable.

---

## Photos

Portraits go in `assets/img/people/`, named to match the `photo:` field in
`data/people.js` — for example `photo: "pratik-khopkar.jpg"`. If a photo is
missing, the card shows the person's initials instead, so the site never looks
broken while you collect them.

Field and lab photographs go in `assets/img/lab/`. Each folder has a short
README with sizing advice.

See the checklist at the end of this file for what is worth gathering.

---

## Files

```
index.html            Home — richness cladogram, the Tetrapulmonata split, news
research.html         Four research threads, richness table, projects, tools
people.html           PI, current members, students, alumni
publications.html     All papers, filterable and searchable; books
news.html             Full news archive
spiderindia.html      Community science
join.html             PhD position and postdoctoral routes
students.html         Dissertations, internships and summer projects
contact.html          Address, email, profiles
404.html              Shown for bad links

assets/css/style.css  All styling; design tokens at the top
assets/js/site.js     Navigation, cladogram, list rendering
assets/img/           Photos, favicon, social sharing card
assets/img/logo/      Logo files and how to use them
data/*.js             The content that changes
_tools/               Optional page generator — see below
CNAME                 Tells GitHub which domain to serve
.nojekyll             Tells GitHub not to run Jekyll
sitemap.xml           For search engines; add new pages here too
```

### The optional generator

The header, navigation and footer are repeated in every `.html` file. That is
deliberate: it means the pages are plain HTML anyone can open and edit.

If you ever need to change something on *every* page — add a nav item, change
the footer address — edit `_tools/pages.py` (page content) or `_tools/build.py`
(the shared shell) and run:

```
cd _tools && python3 build.py
```

That rewrites the eight HTML pages. You never have to use it; editing the HTML
by hand works just as well.

---

## Design notes

Everything on the site is built around one idea: lineages of equal age ending up
wildly unequal in richness.

- **The logo** is two sister lineages leaving the same node. One ends in a single
  tip, in ochre; the other fans into eight, in teal. Same age, different fate —
  and eight tips for eight legs. Files and usage notes are in
  `assets/img/logo/README.md`.
- **The home page cladogram** carries a bar for each lineage showing approximate
  described species on a logarithmic scale. Horseshoe crabs get four; spiders get
  fifty-three thousand. Hovering or tapping a tip gives the count and what the lab
  has done there. Counts, notes and geometry all live in `_tools/pages.py` under
  `TIPS` — change a number there and the tree, the note and the richness table on
  the research page all update.
- There are two versions of the tree in the page, a wide one and a compact one for
  phones; CSS shows whichever fits. Both come from the same function.
- **The rule above each section heading** is the logo's argument in miniature: one
  stem, one branch that stops, one branch that keeps splitting. It is the only
  ornament on the site.
- **Ochre means depauperate.** It marks the lone lineage in the logo and the small
  lineages in the Tetrapulmonata bar. Teal is for everything interactive. Keeping
  those two meanings separate is what stops the palette becoming decoration.
- Type is Fraunces for headings and IBM Plex Sans for text, both from Google Fonts.
- Everything works without JavaScript except the filters and the tree interaction,
  and everything works down to phone width.

---

## Checklist of things only you can supply

- [ ] A portrait of yourself, and one of each lab member.
- [ ] Confirm roles and start dates in `data/people.js` — several were inferred
      from your CV and the old site's news page.
- [ ] The topic of the PM Early Career Research Grant, in `data/projects.js`.
- [ ] A few field and lab photographs for `assets/img/lab/`.
- [ ] DOIs for the older publications.
- [ ] Whether the open PhD position is still open — the old site gives a
      deadline of 14 April 2026, which has passed.
- [ ] Check the species counts in `_tools/pages.py` under `TIPS`. They are
      approximate figures a systematist will notice; spiders follow the World
      Spider Catalog, the rest are round numbers.
- [ ] Confirm the six project ideas on the students page are ones you would
      actually supervise, and swap in your own.

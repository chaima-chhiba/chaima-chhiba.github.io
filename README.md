# chaima-chhiba.github.io

Static portfolio (HTML/CSS/vanilla JS) for GitHub Pages.

## Deploy
1. Create a repo named exactly `chaima-chhiba.github.io`.
2. Copy these files to the repo root (`index.html`, `404.html`, `about/`, `projects/`, `experience/`, `assets/`), push to `main`.
3. Settings → Pages → Deploy from branch → `main` / root.

Paths are root-relative (`/assets/...`), which is correct for a user site at the domain root.

## Fill in before publishing
- Email: replace `ADD_EMAIL@example.com` in every page.
- CV: add `assets/Chaima-Chhiba-CV.pdf`.
- Project GitHub links: replace `[ADD GITHUB LINK]` in `projects/index.html`.
- EdTrust final-year internship details: replace `[ADD DETAILS]` in `experience/index.html`.

`gen.py` is optional: it regenerates the pages if you prefer editing content in one place (`python3 gen.py`).

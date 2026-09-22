# ottermade.github.io

Static site for Ottermade. Pages are markdown files in `content/<lang>/<slug>.md` (front matter: title, description, updated, gumroad); `build.py` renders them into `_site/`, and the GitHub Actions workflow deploys `_site/` to GitHub Pages on every push to `main`.

Local build: `pip install markdown && python build.py`, then open `_site/index.html`.

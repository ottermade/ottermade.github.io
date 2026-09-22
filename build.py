"""Build the Ottermade site: content/<lang>/<slug>.md -> _site/<lang>/<slug>/index.html (+ home page).

Front matter (first lines, `key: value`, ended by a blank line): title, description, lang (default = folder),
gumroad (optional link shown as the call to action), updated (YYYY-MM-DD).
Run: python build.py   (needs: pip install markdown)
"""
from __future__ import annotations
import html, re, shutil
from pathlib import Path
import markdown

ROOT = Path(__file__).resolve().parent
CONTENT, OUT = ROOT / "content", ROOT / "_site"
SITE_NAME = "Ottermade"
BASE_URL = "https://ottermade.github.io"  # change when a custom domain is attached

CSS = """
:root{--bg:#fbfbf9;--ink:#1f2933;--accent:#b04a3c;--muted:#7b8794;--line:#d9dde3}
@media(prefers-color-scheme:dark){:root{--bg:#1f2933;--ink:#e4e7eb;--accent:#f4a38f;--muted:#9aa5b1;--line:#3e4c59}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:18px/1.6 "Noto Sans CJK SC","PingFang SC","Microsoft YaHei","Segoe UI",system-ui,sans-serif}
header,main,footer{max-width:42em;margin:0 auto;padding:0 16px}header{padding-top:20px;display:flex;justify-content:space-between;align-items:baseline;border-bottom:1px solid var(--line)}
header a{color:var(--ink);text-decoration:none;font-weight:700}header nav a{font-weight:400;color:var(--muted);margin-left:14px}
h1{font-size:1.9em;line-height:1.2;margin:.8em 0 .4em}h2{font-size:1.3em;margin-top:1.6em;border-bottom:1px solid var(--line);padding-bottom:.2em}
a{color:var(--accent)}p.lead{font-size:1.1em;color:var(--muted)}
.cta{display:inline-block;background:var(--accent);color:#fff;padding:10px 18px;border-radius:8px;text-decoration:none;font-weight:700;margin:6px 8px 6px 0}
.cta.secondary{background:transparent;color:var(--accent);border:2px solid var(--accent)}
footer{color:var(--muted);font-size:.85em;padding:30px 16px 40px;border-top:1px solid var(--line);margin-top:40px}
ul.pages{list-style:none;padding:0}ul.pages li{margin:.6em 0}
"""

PAGE = """<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} · {site}</title><meta name="description" content="{description}"><link rel="canonical" href="{url}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{description}"><meta property="og:url" content="{url}"><meta property="og:type" content="article">
<style>{css}</style></head><body>
<header><a href="/">{site}</a><nav>{nav}</nav></header>
<main>{body}</main>
<footer>{site} · <a href="/">home</a>{updated}</footer></body></html>"""


def front_matter(text: str) -> tuple[dict, str]:
    meta = {}
    lines = text.splitlines()
    i = 0
    while i < len(lines) and re.match(r"^[a-z_]+:\s*.+", lines[i]):
        k, v = lines[i].split(":", 1); meta[k.strip()] = v.strip(); i += 1
    return meta, "\n".join(lines[i:]).lstrip("\n")


def render(md_path: Path, lang: str, nav: str) -> tuple[str, dict]:
    meta, body_md = front_matter(md_path.read_text(encoding="utf-8"))
    body = markdown.markdown(body_md, extensions=["extra", "sane_lists"])
    slug = md_path.stem
    url = f"{BASE_URL}/{lang}/{slug}/"
    updated = f" · bijgewerkt {meta['updated']}" if lang == "nl" and meta.get("updated") else (f" · updated {meta['updated']}" if meta.get("updated") else "")
    page = PAGE.format(lang=lang, title=html.escape(meta.get("title", slug)), site=SITE_NAME,
                       description=html.escape(meta.get("description", "")), url=url, css=CSS, nav=nav, body=body, updated=updated)
    return page, {"title": meta.get("title", slug), "description": meta.get("description", ""), "url": f"/{lang}/{slug}/", "lang": lang}


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    pages = []
    langs = sorted(p.name for p in CONTENT.iterdir() if p.is_dir())
    nav = " ".join(f'<a href="/{l}/">{l.upper()}</a>' for l in langs)
    for lang in langs:
        for md in sorted((CONTENT / lang).glob("*.md")):
            page, info = render(md, lang, nav)
            dest = OUT / lang / md.stem / "index.html"
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(page, encoding="utf-8")
            pages.append(info)
        items = "".join(f'<li><a href="{p["url"]}">{html.escape(p["title"])}</a><br><span style="color:var(--muted)">{html.escape(p["description"])}</span></li>' for p in pages if p["lang"] == lang)
        (OUT / lang / "index.html").write_text(PAGE.format(lang=lang, title=lang.upper(), site=SITE_NAME, description=SITE_NAME, url=f"{BASE_URL}/{lang}/", css=CSS, nav=nav, body=f"<h1>{SITE_NAME}</h1><ul class=\"pages\">{items}</ul>", updated=""), encoding="utf-8")
    items = "".join(f'<li><a href="{p["url"]}">{html.escape(p["title"])}</a> <span style="color:var(--muted)">({p["lang"].upper()})</span></li>' for p in pages)
    (OUT / "index.html").write_text(PAGE.format(lang="en", title=SITE_NAME, site=SITE_NAME, description="Digital study decks, templates and tools.", url=BASE_URL + "/", css=CSS, nav=nav, body=f"<h1>{SITE_NAME}</h1><p class=\"lead\">Digital study decks, templates and tools.</p><ul class=\"pages\">{items}</ul>", updated=""), encoding="utf-8")
    (OUT / ".nojekyll").write_text("")
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {BASE_URL}/sitemap.xml\n")
    (OUT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + "".join(f"<url><loc>{BASE_URL}{p['url']}</loc></url>" for p in pages) + "</urlset>")
    print(f"built {len(pages)} page(s) into {OUT}")


if __name__ == "__main__":
    main()

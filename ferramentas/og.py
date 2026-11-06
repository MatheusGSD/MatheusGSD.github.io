# Gera public/og.png (1200x630), a imagem de compartilhamento das páginas do site.
# Uso: python ferramentas/og.py
from pathlib import Path
from playwright.sync_api import sync_playwright

RAIZ = Path(__file__).resolve().parent.parent
NM = RAIZ / "node_modules"
F_ARCHIVO = (NM / "@fontsource-variable/archivo/files/archivo-latin-wdth-normal.woff2").as_uri()
F_SANS = (NM / "@fontsource-variable/source-sans-3/files/source-sans-3-latin-wght-normal.woff2").as_uri()
F_MONO = (NM / "@fontsource/ibm-plex-mono/files/ibm-plex-mono-latin-500-normal.woff2").as_uri()

HTML = f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face {{ font-family: A; src: url({F_ARCHIVO}) format("woff2"); font-weight: 100 900; font-stretch: 62% 125%; }}
@font-face {{ font-family: S; src: url({F_SANS}) format("woff2"); font-weight: 200 900; }}
@font-face {{ font-family: M; src: url({F_MONO}) format("woff2"); font-weight: 500; }}
html, body {{ margin: 0; width: 1200px; height: 630px; overflow: hidden; background: #f6f7f9; color: #14171c; }}
.c {{ box-sizing: border-box; height: 630px; padding: 72px 84px; display: grid; grid-template-rows: auto auto 1fr auto; gap: 26px;
     border-left: 18px solid #0f8a7e; }}
h1 {{ margin: 0; font: 850 118px/0.92 A; font-stretch: 72%; letter-spacing: -.015em; }}
p {{ margin: 0; font: 400 34px/1.35 S; color: #4a505b; max-width: 960px; }}
.pe {{ display: flex; justify-content: space-between; align-items: end; font: 500 24px/1 M; letter-spacing: .06em; text-transform: uppercase; color: #6f7682; }}
.pe b {{ color: #0f8a7e; font-weight: 500; }}
</style></head><body><div class="c">
<h1>Matheus<br>Dalmolin</h1>
<p>Painéis e análises com dados públicos, e o método por trás dos números.</p>
<span></span>
<div class="pe"><b>dalmolin.dev</b><span>projetos · textos</span></div>
</div></body></html>"""


def main():
    tmp = RAIZ / "ferramentas" / "_og.html"
    tmp.write_text(HTML, encoding="utf-8")
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1200, "height": 630}, device_scale_factor=1)
        pg.goto(tmp.as_uri())
        pg.wait_for_timeout(400)
        pg.screenshot(path=str(RAIZ / "public" / "og.png"))
        b.close()
    tmp.unlink()
    print("public/og.png")


if __name__ == "__main__":
    main()

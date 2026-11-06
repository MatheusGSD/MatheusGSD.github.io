# Conferência do site gerado (dist/): capturas em 1280 e 390 px, claro e escuro; erros de console; rolagem lateral;
# links internos quebrados. Uso: npm run build && python ferramentas/confere.py
import http.server
import re
import socketserver
import threading
from functools import partial
from pathlib import Path
from playwright.sync_api import sync_playwright

RAIZ = Path(__file__).resolve().parent.parent
DIST = RAIZ / "dist"
SAIDA = RAIZ / "ferramentas" / "_capturas"
PAGINAS = ["/", "/projetos/", "/textos/", "/sobre/", "/textos/swing-simples-segundo-turno/", "/textos/enchente-e-voto/", "/nao-existe/"]
PORTA = 4329


class Silencioso(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def send_error(self, code, message=None, explain=None):
        # imita o GitHub Pages: 404 serve o 404.html
        if code == 404 and (DIST / "404.html").exists():
            corpo = (DIST / "404.html").read_bytes()
            self.send_response(404)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(corpo)))
            self.end_headers()
            self.wfile.write(corpo)
            return
        super().send_error(code, message, explain)


def main():
    SAIDA.mkdir(exist_ok=True)
    srv = socketserver.TCPServer(("127.0.0.1", PORTA), partial(Silencioso, directory=str(DIST)))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    base = f"http://127.0.0.1:{PORTA}"
    problemas = []
    internos = set()
    with sync_playwright() as p:
        b = p.chromium.launch()
        for larg, alt in ((1280, 900), (390, 844)):
            for tema in ("light", "dark"):
                ctx = b.new_context(viewport={"width": larg, "height": alt}, color_scheme=tema)
                pg = ctx.new_page()
                erros = []
                pg.on("console", lambda m: m.type == "error" and erros.append(m.text))
                pg.on("pageerror", lambda e: erros.append(str(e)))
                for caminho in PAGINAS:
                    erros.clear()
                    pg.goto(base + caminho, wait_until="networkidle")
                    lat = pg.evaluate("document.documentElement.scrollWidth - innerWidth")
                    # imagens loading="lazy" + decoding="async" saem em branco na captura de página inteira:
                    # carrega e decodifica todas antes
                    pg.evaluate("""Promise.all([...document.images].map(i => { i.loading = 'eager';
                        return (i.complete ? Promise.resolve() : new Promise(r => { i.onload = i.onerror = r; }))
                          .then(() => i.decode().catch(() => 0)); }))""")
                    nome = (caminho.strip("/").replace("/", "_") or "inicio")
                    pg.screenshot(path=str(SAIDA / f"{nome}_{larg}_{tema}.png"), full_page=True)
                    for h in pg.eval_on_selector_all("a[href]", "as => as.map(a => a.getAttribute('href'))"):
                        if h.startswith("/") and not h.startswith("//"):
                            internos.add(h.split("#")[0])
                    erros_reais = [e for e in erros if caminho != "/nao-existe/" or "404" not in e]
                    if lat > 0 or erros_reais:
                        problemas.append((caminho, larg, tema, lat, erros_reais))
                ctx.close()
        b.close()
    srv.shutdown()
    quebrados = []
    for h in sorted(internos):
        alvo = DIST / h.lstrip("/")
        if not (alvo.is_file() or (alvo / "index.html").is_file()):
            quebrados.append(h)
    print("páginas:", len(PAGINAS), "× 4 visões; capturas em", SAIDA)
    print("problemas (rolagem lateral / erros de console):", problemas or "nenhum")
    print("links internos:", len(internos), "quebrados:", quebrados or "nenhum")


if __name__ == "__main__":
    main()

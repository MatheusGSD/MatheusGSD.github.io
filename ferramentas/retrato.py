# Gera src/retrato.json, o retrato em ASCII da ficha do Sobre, com uma versão para cada tema.
# Uso: python ferramentas/retrato.py [foto]   (padrão: ferramentas/_foto/retrato.png, fora do git: só a arte é publicada)
# Precisa de torch e transformers: o fundo da foto é recortado com o modelo segformer_b2_clothes (~110 MB, baixado
# do Hugging Face na 1ª vez), senão céu e paisagem viram ruído e o rosto some.
import argparse
import json
from pathlib import Path
import numpy as np
from PIL import Image, ImageFilter, ImageOps

RAIZ = Path(__file__).resolve().parent.parent
SAIDA = RAIZ / "src" / "retrato.json"
FOTO = RAIZ / "ferramentas" / "_foto" / "retrato.png"
MODELO = "mattmdjaga/segformer_b2_clothes"
ESCALA = " .:-=+*#%@"  # do vazio ao cheio
COLUNAS = 60
CELULA = 0.6 / 1.2  # largura do caractere em IBM Plex Mono / line-height de .arte no global.css
GAMA = 0.7  # < 1 clareia as sombras: com luz lateral, metade do rosto vira um bloco cheio
PISO = 0.12  # densidade mínima na pessoa, para a silhueta aparecer mesmo nas partes claras


def silhueta(foto):
    """Máscara da pessoa: tudo o que o modelo não classifica como fundo."""
    import torch
    from transformers import AutoModelForSemanticSegmentation

    mod = AutoModelForSemanticSegmentation.from_pretrained(MODELO, use_safetensors=True)
    # o pré-processamento do SegformerImageProcessor, feito à mão para não exigir torchvision
    x = np.asarray(foto.convert("RGB").resize((512, 512), Image.BILINEAR), dtype=np.float32) / 255
    x = (x - [0.485, 0.456, 0.406]) / [0.229, 0.224, 0.225]
    with torch.no_grad():
        log = mod(pixel_values=torch.from_numpy(x.transpose(2, 0, 1)[None].astype(np.float32))).logits
    log = torch.nn.functional.interpolate(log, size=foto.size[::-1], mode="bilinear", align_corners=False)
    pessoa = log.argmax(1)[0].numpy() != mod.config.label2id["Background"]
    return Image.fromarray(pessoa.astype(np.uint8) * 255).filter(ImageFilter.MinFilter(5))  # tira a franja do fundo


def reduzir(img):
    larg, alt = img.size
    return img.resize((COLUNAS, round(COLUNAS * alt / larg * CELULA)), Image.LANCZOS)


def em_caracteres(densidade):
    """Cada pixel (0 = vazio, 255 = cheio) vira um caractere da escala."""
    larg, alt = densidade.size
    px = densidade.tobytes()
    linhas = (px[i:i + larg] for i in range(0, larg * alt, larg))
    return "\n".join("".join(ESCALA[v * len(ESCALA) // 256] for v in l).rstrip() for l in linhas)


def main():
    ap = argparse.ArgumentParser(description="Gera o retrato em ASCII da ficha do Sobre.")
    ap.add_argument("foto", nargs="?", type=Path, default=FOTO)
    args = ap.parse_args()
    foto = ImageOps.exif_transpose(Image.open(args.foto))
    mascara = silhueta(foto)
    caixa = mascara.getbbox()  # enquadra a pessoa: sem linhas vazias em volta
    lum = foto.convert("L").crop(caixa).point(lambda v: round(255 * (v / 255) ** GAMA))
    lum = lum.filter(ImageFilter.UnsharpMask(radius=24, percent=90, threshold=0))  # contraste local
    lum = lum.filter(ImageFilter.UnsharpMask(radius=3, percent=140, threshold=2))  # nitidez dos traços
    l = np.asarray(reduzir(lum), dtype=np.float32) / 255
    m = np.asarray(reduzir(mascara.crop(caixa)), dtype=np.float32) > 127
    lo, hi = np.percentile(l[m], (2, 98))  # contraste medido só na pessoa
    l = np.clip((l - lo) / (hi - lo), 0, 1)

    def tinta(d):
        return Image.fromarray((np.where(m, PISO + (1 - PISO) * d, 0) * 255).astype(np.uint8))

    # O claro da foto é caractere cheio no tema escuro e vazio no tema claro; com uma versão só, um dos dois sai em negativo.
    dados = {"descricao": "Retrato de Matheus Dalmolin desenhado com caracteres",
             "claro": em_caracteres(tinta(1 - l)), "escuro": em_caracteres(tinta(l))}
    SAIDA.write_text(json.dumps(dados, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(SAIDA.relative_to(RAIZ), f"({COLUNAS}×{len(dados['claro'].splitlines())})")


if __name__ == "__main__":
    main()

from psd_tools import PSDImage
from pathlib import Path

psd_path = Path("NOME_ARQUIVO.psd")
output_dir = Path("imagens_extraidas")
output_dir.mkdir(exist_ok=True)

psd = PSDImage.open(psd_path)

for i, layer in enumerate(psd.descendants()):
    if layer.is_visible() and layer.has_pixels():
        imagem = layer.composite()
        nome_arquivo = f"{i:02d}_{layer.name.replace('/', '_')}.png"
        caminho_arquivo = output_dir / nome_arquivo
        imagem.save(caminho_arquivo)
        print(f"Exportado: {nome_arquivo}")
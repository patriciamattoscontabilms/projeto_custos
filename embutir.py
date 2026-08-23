"""Gera uma versão do painel com os dados embutidos no próprio HTML.
Uso: python3 embutir.py painel-agua-clara.html dados-agua-clara.json painel-agua-clara-2026.html"""
import sys, json, io

base, dados, saida = sys.argv[1], sys.argv[2], sys.argv[3]
html = io.open(base, encoding="utf-8").read()
d = json.load(open(dados, encoding="utf-8"))

# </script> dentro do JSON quebraria o bloco; escapa por segurança
bloco = json.dumps(d, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")

marca = "let D = clonar(VAZIO);"
assert marca in html, "estrutura do painel mudou: marcador não encontrado"
html = html.replace(marca, "const EMBUTIDO = " + bloco + ";\nlet D = clonar(VAZIO);")

fim = "\nrenderTudo();\n</script>"
assert fim in html, "estrutura do painel mudou: chamada final não encontrada"
html = html.replace(fim, "\nif(typeof EMBUTIDO !== 'undefined' && EMBUTIDO) adotar(EMBUTIDO); else renderTudo();\n</script>")

# o botão de exemplo perde sentido quando há dados reais embutidos
html = html.replace('<button class="bt" id="btExemplo">Ver com dados de exemplo</button>',
                    '<button class="bt" id="btExemplo" hidden>Ver com dados de exemplo</button>')
html = html.replace('<button class="bt forte" id="btCarregar">Carregar dados (JSON)</button>',
                    '<button class="bt" id="btCarregar">Substituir dados (JSON)</button>')

io.open(saida, "w", encoding="utf-8").write(html)
print("gerado:", saida, "|", len(html)//1024, "KB")

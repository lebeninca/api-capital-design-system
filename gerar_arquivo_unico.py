#!/usr/bin/env python3
"""Monta o arquivo unico do design system, para anexar no Claude web ou no app.

Junta a especificacao, os vetos, os tokens em CSS e o logo em SVG num .md so, para quem
nao usa Claude Code e nao clona repositorio. Rode depois de mexer no DESIGN.md:

    python3 gerar_arquivo_unico.py
"""
import pathlib

RAIZ = pathlib.Path(__file__).parent
SAIDA = RAIZ / "design_system_api_capital_v3_completo.md"

def ler(rel):
    return (RAIZ / rel).read_text(encoding="utf-8").strip()

def sem_frontmatter(texto):
    if texto.startswith("---"):
        return texto.split("\n---\n", 1)[1].lstrip() if "\n---\n" in texto else texto
    return texto

abertura = """# Design System da API Capital — arquivo único

Este arquivo é o design system inteiro da API Capital, num documento só: a especificação, os
vetos, os tokens em CSS e o logo em SVG. Foi montado para quem usa o Claude na web ou no
aplicativo, sem clonar repositório nenhum.

## Instruções para o Claude

Você recebeu a especificação visual da API Capital. Toda peça que você produzir nesta conversa
obedece ao que está escrito aqui.

1. **Leia o documento inteiro antes de produzir qualquer coisa.** A parte 2 é a lei; a parte 3 é
   a lista do que não se faz.
2. **Consuma token, nunca escreva valor.** Cole o CSS da parte 1 dentro de um `<style>` no topo
   da peça e use `var(--api-acao)`, nunca `#0D2A54`.
3. **Valor que não existe na especificação é erro.** Se faltar um valor, pergunte. Não invente.
4. **Antes de entregar, passe a peça pelos vetos da parte 3, um por um.** Os que mais reincidem:
   sombra, gradiente em elemento de interface, cor fora da paleta, canto diferente de 15 px,
   cápsula, terceira família tipográfica, número em Playfair, antetítulo, e peça longa com toda
   seção em branco.
5. **O padrão é sóbrio.** Peso regular, hierarquia conservadora, cor contida, zero efeito.
   Expressividade entra depois, e por pedido.

**As fontes:** em peça de tela, carregue Playfair Display e Inter pelo Google Fonts, com esta
linha no `<head>`:

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600;700&family=Inter:wght@400;500;600;700&display=swap">
```

**O logo:** a parte 4 traz o logo oficial em SVG, em azul e em branco. Cole o SVG inteiro dentro
da peça. Nunca remonte o logotipo com texto, não troque a cor de uma parte e não aplique efeito.

---

# Parte 1 · Os tokens, prontos para colar

Cole tudo abaixo dentro de um `<style>` no topo da peça.

```css
"""

partes = [abertura]
partes.append(ler("tokens/tokens.css"))
partes.append("\n" + ler("tokens/componentes.css"))
partes.append("```\n\n---\n\n# Parte 2 · A especificação\n\n" + sem_frontmatter(ler("DESIGN.md")))
partes.append("\n---\n\n# Parte 3 · Os vetos\n\n" + sem_frontmatter(ler("ANTI_SLOP_VISUAL.md")))

logos = "\n---\n\n# Parte 4 · O logo oficial, em SVG\n"
for arq, titulo in [
    ("assets/logo/svg/api_capital_logo01_azul.svg", "Logo oficial em azul-meia-noite, para fundo branco e claro"),
    ("assets/logo/svg/api_capital_logo01_branco.svg", "Logo oficial em branco, para fundo escuro ou imagem escura"),
]:
    logos += f"\n## {titulo}\n\n```svg\n{ler(arq)}\n```\n"
partes.append(logos)

SAIDA.write_text("\n".join(partes) + "\n", encoding="utf-8")
print(f"{SAIDA.name}: {SAIDA.stat().st_size/1024:.0f} KB")

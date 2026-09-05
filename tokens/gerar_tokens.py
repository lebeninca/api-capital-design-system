#!/usr/bin/env python3
"""Gera tokens.css e tokens.json a partir do DESIGN.md.

O DESIGN.md e a fonte unica. Rode este script depois de mexer nos tokens dele,
para os arquivos nao descolarem: python3 gerar_tokens.py
"""
import json, re, sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
DESIGN = AQUI.parent / "DESIGN.md"

GRUPOS = ("colors", "typography", "rounded", "spacing", "components")


def ler_frontmatter(caminho):
    texto = caminho.read_text(encoding="utf-8")
    if not texto.startswith("---"):
        sys.exit("DESIGN.md sem frontmatter")
    return texto.split("---", 2)[1]


def parse(bloco):
    """Parser do subconjunto de YAML usado no DESIGN.md: dois niveis de indentacao,
    sem listas e sem multilinha."""
    dados, grupo, item = {}, None, None
    for linha in bloco.splitlines():
        if not linha.strip() or linha.lstrip().startswith("#"):
            continue
        recuo = len(linha) - len(linha.lstrip())
        chave, _, valor = linha.strip().partition(":")
        valor = valor.strip().strip('"')
        if recuo == 0:
            grupo = chave if chave in GRUPOS else None
            if grupo:
                dados[grupo] = {}
            item = None
        elif grupo and recuo == 2:
            if valor:
                dados[grupo][chave] = valor
                item = None
            else:
                item = chave
                dados[grupo][item] = {}
        elif grupo and item and recuo >= 4:
            dados[grupo][item][chave] = valor
    return dados


def css_var(ref):
    """{colors.azul} -> var(--api-azul)"""
    return re.sub(r"\{[a-z]+\.([a-z0-9-]+)\}", r"var(--api-\1)", ref)


def escrever_css(dados, destino):
    linhas = [
        "/* Tokens da API Capital. GERADO por tokens/gerar_tokens.py a partir de DESIGN.md.",
        "   Nao edite este arquivo: edite o DESIGN.md e rode o gerador. */",
        "",
        ":root {",
    ]
    for grupo in ("colors", "rounded", "spacing"):
        if grupo not in dados:
            continue
        linhas.append(f"  /* {grupo} */")
        for chave, valor in dados[grupo].items():
            linhas.append(f"  --api-{chave}: {css_var(valor)};")
        linhas.append("")
    if "typography" in dados:
        linhas.append("  /* typography */")
        for nome, props in dados["typography"].items():
            for prop, valor in props.items():
                sufixo = re.sub(r"([A-Z])", r"-\1", prop).lower()
                linhas.append(f"  --api-{nome}-{sufixo}: {valor};")
        linhas.append("")
    linhas.append("}")
    linhas.append("")
    if "typography" in dados:
        linhas.append("/* classes de tipografia */")
        for nome, props in dados["typography"].items():
            corpo = [
                f"  font-family: var(--api-{nome}-font-family);",
                f"  font-size: var(--api-{nome}-font-size);",
                f"  font-weight: var(--api-{nome}-font-weight);",
                f"  line-height: var(--api-{nome}-line-height);",
            ]
            if "letterSpacing" in props:
                corpo.append(f"  letter-spacing: var(--api-{nome}-letter-spacing);")
            if "fontStyle" in props:
                corpo.append(f"  font-style: var(--api-{nome}-font-style);")
            if "textTransform" in props:
                corpo.append(f"  text-transform: var(--api-{nome}-text-transform);")
            if props.get("fontFeature"):
                corpo.append(f'  font-feature-settings: "{props["fontFeature"]}";')
            linhas.append(f".api-{nome} {{")
            linhas.extend(corpo)
            linhas.append("}")
        linhas.append("")
    destino.write_text("\n".join(linhas), encoding="utf-8")


def escrever_componentes(dados, destino):
    """Emite componentes.css: uma classe .api-<nome> por entrada de components."""
    PROP = {
        "backgroundColor": "background-color", "textColor": "color",
        "borderColor": "border-color", "borderWidth": "border-width",
        "rounded": "border-radius", "padding": "padding", "height": "height",
        "width": "width", "accentColor": "accent-color",
        "outline": "outline", "outlineOffset": "outline-offset",
    }
    linhas = [
        "/* Componentes da API Capital. GERADO por tokens/gerar_tokens.py a partir de DESIGN.md.",
        "   Nao edite este arquivo: edite o DESIGN.md e rode o gerador.",
        "   Depende de tokens.css (variaveis) e fontes.css (@font-face). */",
        "",
    ]
    for nome, props in dados.get("components", {}).items():
        corpo = []
        tipo = props.get("typography")
        if tipo:
            t = re.sub(r"\{typography\.([a-z0-9-]+)\}", r"\1", tipo)
            corpo += [
                f"  font-family: var(--api-{t}-font-family);",
                f"  font-size: var(--api-{t}-font-size);",
                f"  font-weight: var(--api-{t}-font-weight);",
                f"  line-height: var(--api-{t}-line-height);",
            ]
            props_t = dados.get("typography", {}).get(t, {})
            if "letterSpacing" in props_t:
                corpo.append(f"  letter-spacing: var(--api-{t}-letter-spacing);")
            if props_t.get("fontFeature"):
                corpo.append(f'  font-feature-settings: "{props_t["fontFeature"]}";')
            if "textTransform" in props_t:
                corpo.append(f"  text-transform: var(--api-{t}-text-transform);")
        for chave, valor in props.items():
            if chave == "typography":
                continue
            css = PROP.get(chave)
            if not css:
                continue
            corpo.append(f"  {css}: {css_var(valor)};")
        if "borderColor" in props and "borderWidth" in props:
            corpo.append("  border-style: solid;")
        if "height" in props:
            corpo += ["  display: inline-flex;", "  align-items: center;", "  justify-content: center;"]
        linhas.append(f".api-{nome} {{")
        linhas += corpo
        linhas.append("}")
        linhas.append("")
    linhas += escrever_utilitarios(dados)
    destino.write_text("\n".join(linhas), encoding="utf-8")


def escrever_utilitarios(dados):
    """Classes utilitarias de espaco, derivadas da escala spacing.
    vao (gap) · margem (margin) · respiro (padding), por lado e por eixo."""
    LADOS = {
        "": "{p}", "topo": "{p}-top", "base": "{p}-bottom",
        "esq": "{p}-left", "dir": "{p}-right",
    }
    linhas = ["/* utilitarios de espaco, derivados da escala spacing (DESIGN.md §Layout) */", ""]
    escala = dados.get("spacing", {})
    for k, v in escala.items():
        var = f"var(--api-{k})"
        linhas.append(f".api-vao-{k} {{ gap: {var}; }}")
        linhas.append(f".api-vao-col-{k} {{ column-gap: {var}; }}")
        linhas.append(f".api-vao-linha-{k} {{ row-gap: {var}; }}")
    linhas.append("")
    for nome, prop in (("margem", "margin"), ("respiro", "padding")):
        for k, v in escala.items():
            var = f"var(--api-{k})"
            for sufixo, molde in LADOS.items():
                cls = f".api-{nome}-{sufixo}-{k}" if sufixo else f".api-{nome}-{k}"
                linhas.append(f"{cls} {{ {molde.format(p=prop)}: {var}; }}")
            linhas.append(f".api-{nome}-h-{k} {{ {prop}-left: {var}; {prop}-right: {var}; }}")
            linhas.append(f".api-{nome}-v-{k} {{ {prop}-top: {var}; {prop}-bottom: {var}; }}")
        linhas.append("")
    linhas.append(".api-margem-auto-h { margin-left: auto; margin-right: auto; }")
    linhas.append("")
    return linhas


def escrever_json(dados, destino):
    destino.write_text(json.dumps(dados, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def resolver(dados, ref):
    """{colors.azul} -> #0D2A54 (segue a cadeia ate o valor cru)."""
    while isinstance(ref, str) and ref.startswith("{"):
        grupo, chave = ref.strip("{}").split(".", 1)
        ref = dados[grupo][chave]
    return ref


def escrever_tema_echarts(dados, destino):
    """Emite tema-echarts.js: registra o tema 'api-capital' no ECharts a partir dos tokens.
    E JS, nao JSON, porque <script src> nao sofre a trava de origem cruzada do fetch.
    Regua: DESIGN.md §Grafico (ordem das series, eixo Y com valor, barra do zero, rosca com furo)."""
    c = lambda k: resolver(dados, dados["colors"][k])
    t = dados["typography"]
    fonte = lambda k: t[k]["fontFamily"]
    tam = lambda k: int(t[k]["fontSize"].rstrip("px"))
    peso = lambda k: int(t[k]["fontWeight"])
    eixo = {
        "axisLine": {"show": True, "lineStyle": {"color": c("borda"), "width": 1}},
        "axisTick": {"show": False},
        "axisLabel": {"color": c("texto-fraco"), "fontFamily": fonte("legenda"),
                      "fontSize": tam("legenda")},
        "splitLine": {"show": True, "lineStyle": {"color": c("borda"), "width": 1}},
        "splitArea": {"show": False},
    }
    tema = {
        "color": [c("azul"), c("latao"), c("azul-claro"), c("preto"), c("areia")],
        "backgroundColor": "transparent",
        "textStyle": {"color": c("texto"), "fontFamily": fonte("corpo-pequeno"),
                      "fontSize": tam("corpo-pequeno")},
        "title": {
            "textStyle": {"color": c("texto"), "fontFamily": fonte("titulo"),
                          "fontSize": 20, "fontWeight": peso("titulo")},
            "subtextStyle": {"color": c("texto-fraco"), "fontFamily": fonte("corpo-pequeno"),
                             "fontSize": tam("corpo-pequeno"), "fontWeight": 400},
        },
        "legend": {"textStyle": {"color": c("texto"), "fontFamily": fonte("legenda"),
                                 "fontSize": tam("legenda")},
                   "icon": "rect", "itemWidth": 14, "itemHeight": 14},
        "tooltip": {
            "backgroundColor": c("fundo"), "borderColor": c("borda"), "borderWidth": 1,
            "textStyle": {"color": c("texto"), "fontFamily": fonte("corpo-pequeno"),
                          "fontSize": tam("corpo-pequeno")},
            "axisPointer": {"lineStyle": {"color": c("texto-fraco"), "width": 1},
                            "crossStyle": {"color": c("texto-fraco"), "width": 1}},
        },
        "categoryAxis": {**eixo, "splitLine": {"show": False}},
        "valueAxis": {**eixo, "axisLine": {"show": False}, "scale": False},
        "logAxis": eixo, "timeAxis": {**eixo, "splitLine": {"show": False}},
        "line": {"lineStyle": {"width": 2}, "symbol": "circle", "symbolSize": 6,
                 "smooth": False, "showSymbol": False},
        "bar": {"barMaxWidth": 56, "itemStyle": {"borderRadius": 0}},
        "pie": {"itemStyle": {"borderColor": c("fundo"), "borderWidth": 2},
                "label": {"color": c("texto"), "fontFamily": fonte("legenda"),
                          "fontSize": tam("legenda")}},
        "candlestick": {"itemStyle": {"color": c("ok"), "color0": c("erro"),
                                      "borderColor": c("ok"), "borderColor0": c("erro")}},
        "scatter": {"symbolSize": 8},
        "graph": {"lineStyle": {"color": c("borda")}},
        "markLine": {"lineStyle": {"color": c("texto-fraco"), "type": "dashed", "width": 1},
                     "label": {"color": c("texto"), "fontFamily": fonte("legenda"),
                               "fontSize": tam("legenda")}},
        "markPoint": {"itemStyle": {"color": c("destaque")},
                      "label": {"color": c("sobre-escuro")}},
        "visualMap": {"color": [c("azul"), c("azul-claro"), c("cinza-claro")]},
        "dataZoom": {"borderColor": c("borda"), "fillerColor": "rgba(13,42,84,0.08)",
                     "handleStyle": {"color": c("azul")}},
    }
    linhas = [
        "/* Tema ECharts da API Capital. GERADO por tokens/gerar_tokens.py a partir de DESIGN.md.",
        "   Nao edite este arquivo: edite o DESIGN.md e rode o gerador.",
        "   Uso: carregue echarts, depois este arquivo, depois echarts.init(el, 'api-capital'). */",
        "(function(){",
        "  var tema = " + json.dumps(tema, indent=2, ensure_ascii=False).replace("\n", "\n  ") + ";",
        "  if (typeof echarts !== 'undefined') echarts.registerTheme('api-capital', tema);",
        "  if (typeof window !== 'undefined') window.API_CAPITAL_TEMA_ECHARTS = tema;",
        "})();",
        "",
    ]
    destino.write_text("\n".join(linhas), encoding="utf-8")


def main():
    dados = parse(ler_frontmatter(DESIGN))
    faltando = [g for g in GRUPOS if g not in dados]
    if faltando:
        sys.exit(f"grupos ausentes no DESIGN.md: {', '.join(faltando)}")
    escrever_css(dados, AQUI / "tokens.css")
    escrever_componentes(dados, AQUI / "componentes.css")
    escrever_json(dados, AQUI / "tokens.json")
    escrever_tema_echarts(dados, AQUI / "tema-echarts.js")
    print(
        "gerado a partir de DESIGN.md: "
        + " · ".join(f"{g} {len(dados[g])}" for g in GRUPOS)
    )


if __name__ == "__main__":
    main()

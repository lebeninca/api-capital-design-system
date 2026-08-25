# Design System da API Capital

Este repositório é a especificação visual da API Capital. Toda peça produzida aqui, ou com base
aqui, obedece ao que está escrito nele.

## Antes de produzir qualquer coisa

1. Leia `DESIGN.md` inteiro. É a lei: tokens de cor, tipografia, layout, forma, componentes.
2. Leia `ANTI_SLOP_VISUAL.md`. É a lista do que não se faz.

## Ao produzir

**Consuma token, nunca escreva valor.** Em peça de código, importe uma folha só:

```html
<link rel="stylesheet" href="tokens/api-capital.css">
```

Ela traz `fontes.css` (@font-face), `tokens.css` (variáveis e classes de tipografia) e
`componentes.css` (as 23 classes `.api-*`).

Use `var(--api-acao)`, não `#0D2A54`. Use `.api-botao-primario`, não um botão novo.

**Valor que não existe no `DESIGN.md` é erro.** Se faltar um valor, pergunte. Não invente.

**Peça longa alterna a superfície das seções.** Apresentação, relatório, proposta, página de
muitas dobras: a seção alterna entre `var(--api-fundo)` e `var(--api-fundo-secao)`
(cinza-claro `#F4F4F4`). **Creme nunca alterna seção.** A faixa pinta a seção inteira e não o card
de dentro, não entra fio entre uma seção e outra, e o `body` fica sempre em `var(--api-fundo)`. Régua no `DESIGN.md` §Ritmo de superfície em peça longa. Peça curta nasce
branca e não alterna.

**Use os ativos que existem.** Logo, ícone, textura, gradiente, favicon, foto e fonte estão em
`assets/`, cada um em SVG, PNG e PDF onde couber. Não gere variação de logo, não recorte símbolo,
não recolore ícone fora da régua.

## Antes de entregar

Passe a peça pelo `ANTI_SLOP_VISUAL.md`, veto por veto. Os que mais reincidem: sombra, gradiente
em elemento de interface, cor fora da paleta, canto diferente de 15, cápsula, caixa com faixa
colorida na lateral, peça longa toda branca (`parede-sem-divisao`), terceira família tipográfica, número em Playfair, antetítulo.

## O que nunca se faz

- Alterar `tokens/tokens.css`, `tokens/componentes.css` ou `tokens/tokens.json` à mão. São
  gerados: edite o `DESIGN.md` e rode `python3 tokens/gerar_tokens.py`.
- Acrescentar cor, fonte, tamanho ou efeito que não esteja no `DESIGN.md`.
- Começar pelo ousado. O padrão é sóbrio; expressividade entra depois, e por pedido.

---
version: "3.0"
name: "API Capital"
description: "Consultoria de investimentos independente. Clássico moderno e autoridade tranquila: azul-meia-noite e latão sobre branco puro, Playfair Display em título e Inter em todo o resto, incluindo cada número apresentado. Zero sombra, canto de 15, grade de 12 colunas. O sistema atende impresso e tela com a mesma régua, e o padrão é sempre o registro mais sóbrio."

colors:
  # Marca
  azul: "#0D2A54"
  latao: "#AA7D41"
  azul-claro: "#418ECE"
  preto: "#171717"
  branco: "#FFFFFF"
  creme: "#F1EAD8"
  areia: "#E4CB8D"
  # Variações, para estado e sobreposição
  azul-var: "#152548"
  latao-var: "#9A7239"
  azul-claro-var: "#3E82B9"
  preto-var: "#020102"
  quadro: "#E6E7E8"
  off-white: "#F2F0EF"
  cinza-claro: "#F0F0F0"
  creme-var: "#DBD4C5"
  areia-var: "#D0B980"
  # Escopo fechado
  erro: "#B71313"
  ok: "#0E7A47"
  # Papéis
  acao: "{colors.azul}"
  acao-hover: "{colors.azul-var}"
  acao-secundaria: "{colors.azul-claro}"
  acao-secundaria-hover: "{colors.azul-claro-var}"
  texto: "{colors.preto}"
  texto-fraco: "rgba(23,23,23,0.5)"
  sobre-escuro: "{colors.branco}"
  fundo: "{colors.branco}"
  fundo-bloco: "{colors.quadro}"
  fundo-quente: "{colors.creme}"
  fundo-secao: "{colors.off-white}"
  fundo-escuro: "{colors.azul}"
  borda: "{colors.quadro}"
  fio: "{colors.azul}"
  destaque: "{colors.latao}"
  realce: "{colors.areia}"

typography:
  display:
    fontFamily: "'Playfair Display', Georgia, serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.96px
  secao:
    fontFamily: "'Playfair Display', Georgia, serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.72px
  titulo:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  citacao:
    fontFamily: "'Playfair Display', Georgia, serif"
    fontSize: 22px
    fontWeight: 400
    fontStyle: italic
    lineHeight: 1.45
    letterSpacing: 0
  corpo-grande:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 19px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  corpo:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 17px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  corpo-pequeno:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  rotulo:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 4px
    textTransform: uppercase
  numero-grande:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.4px
    fontFeature: tnum
  numero:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 17px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
    fontFeature: tnum
  botao:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 17px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0
  botao-pequeno:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0
  legenda:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0

rounded:
  canto-vivo: 0px
  x4: 15px

spacing:
  x1: 4px
  x2: 8px
  x4: 16px
  x6: 24px
  x10: 40px
  x16: 64px

components:
  botao-primario:
    backgroundColor: "{colors.acao}"
    textColor: "{colors.sobre-escuro}"
    typography: "{typography.botao}"
    rounded: "{rounded.canto}"
    padding: 0 24px
    height: 48px
  botao-primario-hover:
    backgroundColor: "{colors.acao-hover}"
    textColor: "{colors.sobre-escuro}"
    typography: "{typography.botao}"
    rounded: "{rounded.canto}"
    padding: 0 24px
    height: 48px
  botao-secundario:
    backgroundColor: "{colors.fundo}"
    textColor: "{colors.acao}"
    borderColor: "{colors.acao}"
    borderWidth: 1px
    typography: "{typography.botao}"
    rounded: "{rounded.canto}"
    padding: 0 24px
    height: 48px
  botao-azul-claro:
    backgroundColor: "{colors.acao-secundaria}"
    textColor: "{colors.sobre-escuro}"
    typography: "{typography.botao}"
    rounded: "{rounded.canto}"
    padding: 0 24px
    height: 48px
  botao-sobre-escuro:
    backgroundColor: "{colors.branco}"
    textColor: "{colors.azul}"
    typography: "{typography.botao}"
    rounded: "{rounded.canto}"
    padding: 0 24px
    height: 48px
  botao-texto:
    backgroundColor: transparent
    textColor: "{colors.acao}"
    typography: "{typography.botao}"
    rounded: "{rounded.canto-vivo}"
    padding: 0
    height: 48px
  campo:
    backgroundColor: "{colors.fundo}"
    textColor: "{colors.texto}"
    borderColor: "{colors.borda}"
    borderWidth: 1px
    typography: "{typography.corpo}"
    rounded: "{rounded.canto}"
    padding: 0 16px
    height: 48px
  campo-foco:
    backgroundColor: "{colors.fundo}"
    textColor: "{colors.texto}"
    borderColor: "{colors.acao}"
    borderWidth: 1px
    outline: "3px solid {colors.acao-secundaria}"
    outlineOffset: 2px
    typography: "{typography.corpo}"
    rounded: "{rounded.canto}"
    padding: 0 16px
    height: 48px
  campo-erro:
    backgroundColor: "{colors.fundo}"
    textColor: "{colors.texto}"
    borderColor: "{colors.erro}"
    borderWidth: 1px
    typography: "{typography.corpo}"
    rounded: "{rounded.canto}"
    padding: 0 16px
    height: 48px
  card-conteudo:
    backgroundColor: "{colors.fundo}"
    textColor: "{colors.texto}"
    borderColor: "{colors.fio}"
    borderWidth: 1px
    typography: "{typography.corpo}"
    rounded: "{rounded.canto}"
    padding: 40px
  card-dado:
    backgroundColor: "{colors.fundo-bloco}"
    textColor: "{colors.texto}"
    typography: "{typography.corpo}"
    rounded: "{rounded.canto}"
    padding: 40px
  card-destaque:
    backgroundColor: "{colors.fundo-escuro}"
    textColor: "{colors.sobre-escuro}"
    typography: "{typography.corpo}"
    rounded: "{rounded.canto}"
    padding: 40px
  card-quente:
    backgroundColor: "{colors.fundo-quente}"
    textColor: "{colors.azul}"
    typography: "{typography.corpo}"
    rounded: "{rounded.canto}"
    padding: 40px
  caixa-latao:
    backgroundColor: "{colors.destaque}"
    textColor: "{colors.sobre-escuro}"
    typography: "{typography.titulo}"
    rounded: "{rounded.canto}"
    padding: 24px
  caixa-ocre:
    backgroundColor: "{colors.realce}"
    textColor: "{colors.azul}"
    typography: "{typography.corpo}"
    rounded: "{rounded.canto}"
    padding: 24px
  nav-clara:
    backgroundColor: "{colors.fundo}"
    textColor: "{colors.texto}"
    typography: "{typography.corpo}"
    padding: 0 40px
    height: 96px
  nav-escura:
    backgroundColor: "{colors.fundo-escuro}"
    textColor: "{colors.sobre-escuro}"
    typography: "{typography.corpo}"
    padding: 0 40px
    height: 96px
  aviso-erro:
    backgroundColor: "{colors.fundo}"
    textColor: "{colors.texto}"
    borderColor: "{colors.erro}"
    borderWidth: 1px
    typography: "{typography.corpo-pequeno}"
    rounded: "{rounded.canto}"
    padding: 16px
  aviso-ok:
    backgroundColor: "{colors.fundo}"
    textColor: "{colors.texto}"
    borderColor: "{colors.ok}"
    borderWidth: 1px
    typography: "{typography.corpo-pequeno}"
    rounded: "{rounded.canto}"
    padding: 16px
  tabela-cabecalho:
    backgroundColor: "{colors.fundo-escuro}"
    textColor: "{colors.sobre-escuro}"
    typography: "{typography.rotulo}"
    rounded: "{rounded.canto-vivo}"
    padding: 16px
  tabela-linha:
    backgroundColor: "{colors.fundo}"
    textColor: "{colors.texto}"
    typography: "{typography.corpo-pequeno}"
    padding: 16px
  tabela-zebra:
    backgroundColor: "{colors.fundo-bloco}"
    textColor: "{colors.texto}"
    typography: "{typography.corpo-pequeno}"
    padding: 16px
  rodape:
    backgroundColor: "{colors.fundo}"
    textColor: "{colors.texto-fraco}"
    typography: "{typography.legenda}"
    padding: 64px 40px

tipo: diretriz
status: ativo
zona: publica
dominio: design
bandeira: 06_marketing_api_capital
produto: api_capital
versao: 3.0
resumo: >-
  Especificação de design da API Capital, no formato design.md: tokens de cor, tipografia,
  espaço, forma e componente, mais as regras de layout, logo, ícone, imagem, estado e veto.
  Atende impresso e tela.
---

## Visão geral

> **⬦ marca decisão pendente de aprovação.** O resto do documento é decisão já tomada.

A API Capital é uma consultoria de investimentos que não recebe comissão de produto. O sistema
visual traduz isso em sobriedade: **azul-meia-noite** (`{colors.azul}`) como cor de autoridade
e de ação, **latão** (`{colors.latao}`) como o único calor da paleta, e **branco puro**
(`{colors.branco}`) como fundo padrão. Em peça longa, a seção alterna com um off-white ou um
cinza-claro para marcar onde uma parte termina e a outra começa (§Ritmo de superfície).

A tipografia trabalha em par fixo: **Playfair Display** carrega título e abertura, com tracking
negativo nos tamanhos grandes; **Inter** carrega todo o resto, e **todo número apresentado**, com
figuras tabulares. Nenhuma terceira família entra no sistema.

O sistema atende dois territórios com a mesma régua. No impresso, grade de 12 colunas, margem de
20 mm e espaçamento de 60 ou 120 px a 300 dpi. Em tela, a mesma grade em proporção, canto de 15 px
e **zero sombra em qualquer nível**: o que separa um bloco do outro é fundo sólido ou linha.

### Assinatura

- **Zero sombra, em qualquer nível.** Profundidade se faz com fundo sólido, com `{colors.fundo-bloco}` ou com linha de alto contraste.
- **Uma só cor de ação.** `{colors.acao}` no botão cheio; `{colors.acao-secundaria}` no secundário. O latão nunca é clicável.
- **Playfair com tracking negativo** de -0,96 px em 48 px, escalando até 0 no corpo. O aperto no título grande é a assinatura tipográfica.
- **Figuras tabulares em todo número apresentado**, com Inter em peso 700. Coluna de número alinha à direita.
- **Canto de 15 px em tela, canto vivo no impresso.** Cápsula é vetada.
- **Estampa tom sobre tom**, sempre a variação da cor do fundo, em preenchimento sólido.
- **Gradiente só como véu de legibilidade**, de uma cor, do transparente ao cheio, e apenas sobre fundo complexo.
- **O padrão é sóbrio.** Peso regular, hierarquia conservadora, cor contida, zero efeito. Expressividade entra depois da primeira versão.

## Cores

### Marca

| Token | Hex | Papel |
|---|---|---|
| `{colors.azul}` | `#0D2A54` | Cor principal. Título, ação, fundo sólido, marca |
| `{colors.latao}` | `#AA7D41` | Único calor da paleta. Número que importa, marcação de item ativo |
| `{colors.azul-claro}` | `#418ECE` | Ação secundária, link, série de gráfico |
| `{colors.preto}` | `#171717` | Texto de leitura |
| `{colors.branco}` | `#FFFFFF` | Fundo padrão |
| `{colors.creme}` | `#F1EAD8` | Fundo de bloco, papel de peça impressa |
| `{colors.areia}` | `#E4CB8D` | Caixa de destaque suave, textura, série de gráfico |

### Variações

Uma por cor de marca. Servem para estado sobre, para fundo de bloco sobre o próprio fundo e para
a textura. Os valores são fixos.

| Cor | Variação |
|---|---|
| `{colors.azul}` | `{colors.azul-var}` `#152548` |
| `{colors.latao}` | `{colors.latao-var}` `#9A7239` |
| `{colors.azul-claro}` | `{colors.azul-claro-var}` `#3E82B9` |
| `{colors.preto}` | `{colors.preto-var}` `#020102` |
| `{colors.branco}` | `{colors.quadro}` `#E6E7E8` |
| `{colors.creme}` | `{colors.creme-var}` `#DBD4C5` |
| `{colors.areia}` | `{colors.areia-var}` `#D0B980` |

### ⬦ Papéis

Os nomes e a divisão em papéis são derivação. Use o token de papel na peça, não o de marca. Trocar uma cor da marca passa a ser uma linha.

| Token | Aponta para | Onde |
|---|---|---|
| `{colors.acao}` | `{colors.azul}` | Botão cheio, link em destaque |
| `{colors.acao-hover}` | `{colors.azul-var}` | O mesmo botão sob o cursor |
| `{colors.acao-secundaria}` | `{colors.azul-claro}` | Botão secundário, link em corpo de texto |
| `{colors.texto}` | `{colors.preto}` | Texto de leitura |
| `{colors.texto-fraco}` | `{colors.preto}` a 50% | Legenda, fonte, crédito, nota |
| `{colors.sobre-escuro}` | `{colors.branco}` | Texto sobre fundo escuro |
| `{colors.fundo}` | `{colors.branco}` | Fundo de página |
| `{colors.fundo-bloco}` | `{colors.quadro}` | Zebra de tabela, card de dado, campo, caixa de apoio |
| `{colors.fundo-quente}` | `{colors.creme}` | Bloco de respiro entre seções frias. **Nunca como faixa de seção em peça longa** |
| `{colors.fundo-secao}` | `{colors.off-white}` | Faixa de seção em peça longa. A alternativa neutra é `{colors.cinza-claro}` |
| `{colors.fundo-escuro}` | `{colors.azul}` | Card de destaque, cabeçalho de tabela, navegação escura |
| `{colors.borda}` | `{colors.quadro}` | Borda de campo e de bloco neutro |
| `{colors.fio}` | `{colors.azul}` | Fio de título, régua de seção, contorno de card |
| `{colors.destaque}` | `{colors.latao}` | Destaque quente. **Nunca em elemento clicável** |
| `{colors.realce}` | `{colors.areia}` | Caixa de destaque com texto de leitura |

### Ritmo de superfície em peça longa

Peça de rolagem longa — apresentação em seções, relatório, proposta, página de muitas dobras —
precisa que o leitor veja onde uma parte termina e a outra começa. Branco do topo ao pé apaga essa
divisão e entrega uma parede sem articulação.

**A régua:** a seção de uma peça longa alterna a superfície entre `{colors.fundo}` e **uma** das
duas superfícies de seção:

| Token | Hex | Registro |
|---|---|---|
| `{colors.fundo-secao}` → `{colors.off-white}` | `#F2F0EF` | Off-white. O padrão |
| `{colors.cinza-claro}` | `#F0F0F0` | Cinza-claro neutro |

A faixa `{colors.fundo-escuro}` continua sendo o degrau de destaque, usada com parcimônia.

🔴 **Creme não alterna seção.** `{colors.fundo-quente}` (`#F1EAD8`) é bloco de respiro pontual e
papel de peça impressa. Off-white e cinza-claro é que carregam o ritmo da peça longa.

Os limites, que são o que impede a válvula de virar carnaval:

- **Duas superfícies claras por peça, no máximo.** Branco mais uma de seção; escolher entre o off-white e o cinza-claro, nunca os dois na mesma peça.
- **A superfície pinta a FAIXA da seção inteira**, de borda a borda — nunca o card de dentro. Card sobre faixa de seção volta ao branco, ou se resolve por linha.
- **Zero cor nova.** A alternância consome token; hex escrito à mão segue vetado.
- **O padrão continua branco.** Peça curta — uma dobra, um card, um e-mail, uma folha A4 — nasce branca e não alterna.
- **O documento inteiro nunca é de apoio.** A superfície é faixa dentro da peça; `body` e container raiz ficam em `{colors.fundo}`.

### Escopo fechado

| Token | Hex | Único uso |
|---|---|---|
| `{colors.erro}` | `#B71313` | Erro e alerta em interface. Na marca, o `m` da tagline |
| `{colors.ok}` | `#0E7A47` | Confirmação em interface |

### Gradiente

Use sobre fundo complexo, como textura ou foto, para ajudar na legibilidade ou para criar uma
área limpa onde o logo entra.

| | |
|---|---|
| Cor | Uma, do transparente ao cheio. Nunca entre duas |
| Famílias | `{colors.branco}`, `{colors.azul}`, `{colors.preto}` |
| Direção | Qualquer uma, inclusive diagonal |
| Curva | Branco: 0 · 31% · 61% · 82% · 95% · cheio. Azul e preto: 0 · 25% · 79% · cheio |
| Onde | Fundo de peça. Nunca em texto, botão, ícone, caixa ou elemento de interface |
| Arquivos | `assets/gradiente/`, nas três famílias |

## Tipografia

### Famílias

**Playfair Display** em título, abertura e citação. **Inter** em todo o resto, incluindo cada
número apresentado. As duas têm licença livre para uso comercial, e **os arquivos estão em
`assets/fonte/`**: `otf` e `ttf` para instalar, `woff2` para web.

⬦ Substituto, quando a família não carregar: Georgia no lugar da Playfair, e a fonte de sistema
no lugar da Inter. Nenhuma terceira família entra no sistema, nem como substituto permanente.

### Escala em tela

⬦ Quatro níveis vêm da folha de tokens do arquivo de desenho e estão aprovados: display 48,
título 28, corpo 17 e legenda 14. Os demais nove níveis e todo o tracking são derivação.

| Token | Tamanho | Peso | Entrelinha | Tracking | Uso |
|---|---|---|---|---|---|
| `{typography.display}` | 48px | 700 | 1,15 | -0,96px | Título de abertura |
| `{typography.secao}` | 36px | 700 | 1,20 | -0,72px | Título de seção |
| `{typography.titulo}` | 28px | 600 | 1,30 | 0 | Título de bloco e de card. **Inter**, não Playfair |
| `{typography.citacao}` | 22px | 400 itálico | 1,45 | 0 | Citação, frase isolada |
| `{typography.corpo-grande}` | 19px | 400 | 1,60 | 0 | Parágrafo de abertura |
| `{typography.corpo}` | 17px | 400 | 1,60 | 0 | Leitura corrida |
| `{typography.corpo-pequeno}` | 15px | 400 | 1,50 | 0 | Célula de tabela, texto de apoio |
| `{typography.rotulo}` | 13px | 600 | 1,20 | 4px, caixa alta | Rótulo de seção, cabeçalho de tabela |
| `{typography.numero-grande}` | 40px | 700 | 1,10 | -0,4px | Número em destaque. Figuras tabulares |
| `{typography.numero}` | 17px | 700 | 1,30 | 0 | Número em tabela e em texto de dado. Figuras tabulares |
| `{typography.botao}` | 17px | 600 | 1,00 | 0 | Rótulo de botão |
| `{typography.botao-pequeno}` | 15px | 600 | 1,00 | 0 | Rótulo de botão compacto |
| `{typography.legenda}` | 14px | 400 | 1,40 | 0 | Fonte, nota, crédito |

### Escala impressa (A4, 300 dpi)

| Nível | Tamanho e entrelinha |
|---|---|
| Título | Playfair Display Bold 130 |
| Linha-fina | Inter Regular 44 / 1,40 |
| Corpo | Inter Regular 34 / 1,62 |
| Citação | Playfair Display Italic 56 |
| Rótulo de seção | Inter SemiBold 28, tracking 4 |
| Legenda | Inter Regular 24, em `{colors.texto-fraco}` |

Alinhamento à esquerda, sem justificar.

### Princípios

- **Tracking negativo no título.** De -0,96 px em 48 px até 0 no corpo, proporcional ao tamanho.
  É o que dá acabamento ao título grande.
- **Figuras tabulares em número.** `font-feature-settings: "tnum"` em toda célula com dinheiro,
  contagem ou percentual. Sem isso, a coluna de número dança.
- **Número apresentado sai em Inter.** A exceção é o número dentro de uma frase que já esteja em
  Playfair, que pode continuar em Playfair.
- **Duas famílias.** Uma terceira família quebra o sistema.

### Número, moeda e data

| O que | Assim | Nunca |
|---|---|---|
| Decimal | `11,4%` | `11.4%` |
| Milhar | `1.250.000` | `1,250,000` |
| Moeda | `R$ 1.250,00` | `R$1250.00` |
| Percentual | `11,4%` | `11,4 %` |
| Variação | `+3,0 p.p.` | `+3,0pp` |
| Data | `31/07/2026` em tabela · `31 de julho de 2026` em texto | `07/31/2026` |

## Layout

### Escala de espaço

Base de 8 px, com 4 px para trabalho fino.

`{spacing.x1}` 4 · `{spacing.x2}` 8 · `{spacing.x4}` 16 · `{spacing.x6}` 24 · `{spacing.x10}` 40 ·
`{spacing.x16}` 64.

Respiro interno de card: `{spacing.x10}` 40 px. Respiro interno de caixa e de aviso:
`{spacing.x6}` 24 px. Altura de seção em tela: 64 a 96 px.

### Grade e margem

Doze colunas, medianiz de 4 mm, margem de 20 mm nos quatro lados, nos dois formatos impressos.

| Formato | Área útil (300 dpi) | Coluna | Medida de linha |
|---|---|---|---|
| A4 retrato | 2008 × 3036 px | 10,5 mm (124 px) | 6 a 8 colunas |
| A4 paisagem | 3036 × 1914 px | 17,75 mm (210 px) | 5 a 7 colunas |

Em tela: margem de 4% da largura, 12 colunas, medianiz de um quarto da coluna.

Margem e espaçamento se medem a partir da **altura de maiúscula** do texto, não da caixa
delimitadora. A distância entre o topo da caixa e o topo da maiúscula, a 300 dpi: Playfair Display
130 = 39 px · Inter 44 = 14 px · Inter 28 = 6 px.

### Espaçamento entre blocos

Blocos de texto, imagem, gráfico ou tabela têm espaçamento mínimo de **120 px**. A exceção é
linha-fina, subtítulo e legenda, que podem ter **60 px**.

### Coluna

Todo bloco começa e termina em borda de coluna. Larguras diferentes convivem na mesma página.
A medianiz não é área útil: quando o conteúdo não cabe, cede a largura do bloco.

| Colunas | Paisagem | Retrato |
|---|---|---|
| 1 | 210 | 124 |
| 2 | 467 | 295 |
| 3 | 724 | 467 |
| 4 | 981 | 638 |
| 5 | 1237 | 809 |
| 6 | 1494 | 980 |
| 7 | 1751 | 1152 |
| 8 | 2008 | 1323 |
| 9 | 2265 | 1494 |
| 10 | 2522 | 1665 |
| 11 | 2779 | 1837 |
| 12 | 3036 | 2008 |

Modelos: uma coluna · duas em 50/50 · três em terços · duas em 7+5 · duas em 9+3.

## Profundidade

| Nível | Tratamento | Uso |
|---|---|---|
| 0 | Plano | Superfície padrão |
| 1 | Linha de 1 px em `{colors.borda}` | Campo, bloco neutro |
| 2 | Linha de 1 px em `{colors.fio}` | Card de conteúdo, contorno de destaque |
| 3 | Fundo sólido: `{colors.fundo-bloco}`, `{colors.fundo-quente}` ou `{colors.fundo-escuro}` | Card de dado, bloco de respiro, card de destaque |

**Sombra não existe neste sistema, em nenhum nível.** Nem em card, nem em botão, nem em painel
flutuante, nem em logo sobre foto. Onde a separação for insuficiente, sobe-se um nível de
profundidade.

## Forma

### Fio

| Nome | Espessura | Onde |
|---|---|---|
| Capilar | 0,5 pt | Fio de tabela, separador de linha |
| Fino | 1 pt | Divisória de bloco, contorno de caixa |
| Médio | 2 pt | Fio sob título, régua de seção |
| Grosso | 6 pt | Fio de abertura, marcação de capa |

### Canto

`{rounded.canto}` 15 px em tela, em card, botão, campo, aviso e amostra de cor. `{rounded.canto-vivo}` no
impresso. Cápsula (`9999px`) é vetada.

### Divisória

A horizontal atravessa as 12 colunas. A vertical separa colunas de texto e tem sempre 1 pt. Entre
linhas de tabela não entra fio: use separação de zebra.

## Logo

Doze versões: oito montagens bicolores e quatro vazadas de uma cor. O logotipo nunca se remonta
à mão.

**Os arquivos estão em `assets/logo/`**, em `svg/`, `png/` (1x, 2x e 4x) e `pdf/`. Cada versão vem
em azul, branco e quase-preto. O nome diz tudo: `api_capital_logo03_branco.svg`.

### Área livre

Deixe uma faixa livre em volta do logo. A medida é **metade da altura da letra A** do logotipo
"API". No selo isolado, o disco com o pelicano, a medida é **um quarto do diâmetro do disco**.
Nenhum elemento entra nessa faixa: texto, fio, imagem ou borda de foto.

### Fundo

| Fundo | Versão |
|---|---|
| Branco e claro | Bicolor oficial, ou vazada em `{colors.azul}` |
| Escuro ou imagem escura | Vazada branca |
| Imagem clara ou textura | Vazada branca com véu por baixo |

### O que não se faz

- Remontar o logotipo com texto
- Trocar a cor de uma parte
- Esticar, inclinar, girar, aplicar efeito
- Pôr sombra ou contorno para separar do fundo
- Usar arquivo que não seja o oficial

## Ícone

A iconografia usa a biblioteca **Lucide**, de traço único e geometria simples.

**Os 24 ícones escolhidos para os usos recorrentes da marca estão em `assets/icone/`**, em
`svg/`, `png/` e `pdf/`. Use esses primeiro. Para um caso que eles não cobrem, escolha na
biblioteca completa da Lucide, em `assets/icone/lucide/`, mantendo traço de 2 px e sem
preenchimento.

Posição no card: canto inferior direito.

## Imagem

### Fotografia

**O acervo está em `assets/foto/`.**

```
Wide, quiet natural atmosphere in high key: open sky, mist, slow water or rippled sand.
Cool blue (hue 190-215) or warm sand (hue 29-39), never both in the same frame. Bright,
low saturation, low internal contrast: no deep blacks, no blown highlights, no drama.
No people, no sharp focal subject, no landmark. The image is background, not statement:
it must survive a text overlay without competing with it. Natural daylight, no artificial
colour grading, no lens flare, no HDR.
```

Fotografia de pessoa não está definida.

### Textura

Ladrilho que se repete para a direita e para baixo sem emenda, sempre tom sobre tom, em
preenchimento sólido. Nunca cor escura com opacidade por cima. **Os arquivos estão em
`assets/textura/`.**

| Fundo | Ladrilho |
|---|---|
| `{colors.preto}` | `{colors.preto-var}` |
| `{colors.azul}` | `{colors.azul-var}` |
| `{colors.azul-claro}` | `{colors.azul-claro-var}` |
| `{colors.latao}` | `{colors.latao-var}` |
| `{colors.areia}` | `{colors.areia-var}` |
| `{colors.creme}` | `{colors.creme-var}` |
| `{colors.branco}` | `{colors.quadro}` |

## Componentes

### Botão

**`{components.botao-primario}`** é a ação dominante. Fundo `{colors.acao}`, texto
`{colors.sobre-escuro}`, tipo `{typography.botao}`, canto `{rounded.canto}`, altura 48 px, respiro
lateral de `{spacing.x6}` 24 px. Sob o cursor vira `{components.botao-primario-hover}`, que troca
o fundo pela variação.

**`{components.botao-secundario}`** é a alternativa de contorno: fundo `{colors.fundo}`, texto e
borda de 1 px em `{colors.acao}`, mesma geometria.

**`{components.botao-azul-claro}`** carrega a ação secundária em `{colors.acao-secundaria}`.

**`{components.botao-sobre-escuro}`** é a ação sobre fundo escuro: fundo `{colors.branco}`, texto
`{colors.azul}`.

**`{components.botao-texto}`** é o botão sem caixa, em `{colors.acao}`.

Alturas: 56 px em abertura de página, 48 px no padrão, 40 px em barra e tabela. Em toque, mínimo
de 44 px.

### Campo

**`{components.campo}`** tem fundo `{colors.fundo}`, borda de 1 px em `{colors.borda}`, canto
`{rounded.canto}`, altura 48 px e respiro lateral de `{spacing.x4}` 16 px.

**O rótulo fica sempre acima do campo.** Em foco, `{components.campo-foco}` acrescenta anel de
3 px, afastado 2 px. Em erro, `{components.campo-erro}` troca a borda
por `{colors.erro}`, **com a mensagem escrita ao lado**.

### Card

| Componente | Fundo | Texto | Quando |
|---|---|---|---|
| `{components.card-conteudo}` | `{colors.fundo}`, borda em `{colors.fio}` | `{colors.texto}` | Bloco de conteúdo com função estrutural |
| `{components.card-dado}` | `{colors.fundo-bloco}` | `{colors.texto}` | Número e dado apresentado |
| `{components.card-destaque}` | `{colors.fundo-escuro}` | `{colors.sobre-escuro}` | Destaque. **Um por tela** |
| `{components.card-quente}` | `{colors.fundo-quente}` | `{colors.azul}` | Respiro entre seções frias |

Respiro interno de 40 px em toda borda. Anatomia: título · fio · descrição · espaço · ícone no
canto inferior direito.

### Caixa de destaque

**`{components.caixa-latao}`** tem fundo `{colors.destaque}` e carrega **só título grande ou
número**. **`{components.caixa-ocre}`** tem fundo `{colors.realce}` e carrega texto de
leitura em `{colors.azul}`.

Máximo de uma caixa quente por página.

### Navegação

**`{components.nav-clara}`** e **`{components.nav-escura}`**: altura de 96 px em tela cheia, 72 px
em tablet e 64 px em celular. Respiro lateral de 40 px, distância de 32 px entre itens. Logo à
esquerda, itens no meio, **uma ação à direita**, a mesma em todos os tamanhos.

O item ativo se marca com fio de 2 pt embaixo: `{colors.acao}` no fundo claro, `{colors.destaque}`
no escuro. No fundo escuro o logo entra na versão branca vazada, nunca na azul.

Em celular os itens viram menu; a ação continua visível.

### Aviso

**`{components.aviso-erro}`** e **`{components.aviso-ok}`**: fundo branco, borda de 1 px na
cor do estado, canto `{rounded.canto}`, respiro de `{spacing.x4}` 16 px.

**Todo aviso tem ícone, título e o que fazer.** A cor sozinha não comunica.

### Tabela

**`{components.tabela-cabecalho}`** em `{colors.fundo-escuro}` com `{typography.rotulo}`.
Linhas alternam **`{components.tabela-linha}`** e **`{components.tabela-zebra}`**. Entre linhas
não entra fio.

Texto à esquerda, número à direita em `{typography.numero}`. A tabela fecha com fonte e data de
apuração em `{typography.legenda}`.

### Gráfico

Cores de série, nesta ordem: `{colors.azul}` · `{colors.latao}` · `{colors.azul-claro}` ·
`{colors.preto}` · `{colors.areia}`.

Eixo Y sempre com valores, barra partindo do zero, rosca sempre com furo. Fecha com fonte e data
de apuração.

## Estados

| Estado | Como se mostra |
|---|---|
| Normal | A cor de papel do elemento |
| Sobre | Escurece 18%. O cursor vira mão |
| Foco | Anel de 3 px, afastado 2 px. Chega pelo teclado |
| Carregando | O rótulo troca e o elemento trava |
| Desabilitado | Fundo `{colors.fundo-bloco}`, texto a 40% |

Nenhum elemento clicável entra na peça sem os cinco.

## Acessibilidade

- **Foco nunca some.** `outline: none` sem substituto é erro.
- **⬦ Alvo de toque de 44 px** de altura, e 44 × 44 quando for só ícone.
- **Erro, sucesso e alerta se dizem em texto**, não só em cor.
- **Texto alternativo em toda imagem que carrega informação.** Imagem decorativa entra com
  alternativo vazio.

## Comportamento responsivo

| Faixa | Largura | Mudanças |
|---|---|---|
| Tela cheia | > 1024 px | 12 colunas, margem 4%, nav 96 px, display 48 px |
| Tablet | 640 a 1024 px | 2 colunas, margem 24, nav 72 px, display 36 px |
| Celular | < 640 px | 1 coluna, margem 16, nav 64 px, display 28 px |

⬦ O título desce em degrau 48 → 36 → 28 px. Card de três colunas vira duas e depois uma. Botão sobe
para 44 px de altura mínima em toque. Tabela larga rola na horizontal dentro do próprio bloco, em
vez de encolher a fonte.

## Vetos

- Sombra, brilho, vidro fosco, translucidez
- Gradiente entre duas cores, ou em elemento de interface
- Cor sólida rebaixada com opacidade para simular tom mais claro
- Cápsula (`9999px`)
- Contorno cinza claro de 1 px em volta de tudo
- Caixa de destaque com faixa colorida na lateral ou no topo
- Terceira família tipográfica
- Número apresentado em Playfair
- Número sem figura tabular em tabela
- Antetítulo: rótulo miúdo em caixa alta acima do título
- Rótulo do tipo `01 / BLOCO 03`
- Linha de fonte pequena e cinza com informação que deveria estar no texto
- Eixo de gráfico cortado, gráfico sem escala, minigráfico decorativo
- Percentual escrito sobre a fatia da rosca
- Fio entre linhas de tabela
- Mais de uma caixa quente por página
- Emoji decorativo
- Símbolo que remeta a mercado financeiro: gráfico, seta, candelabro japonês

## Guia de iteração

1. Trabalhe **um componente por vez**.
2. Referencie token, nunca valor: `{colors.acao}`, `{typography.corpo}`, `{rounded.canto}`.
3. Comece sóbrio. Expressividade entra na segunda versão.
4. Variante nova entra como entrada própria em `components`, não como exceção no texto.
5. Todo bloco começa e termina em coluna.
6. Espaçamento entre blocos: 120 px. Dentro do bloco: 60 px.
7. Número apresentado em Inter 700 com figura tabular.
8. Gráfico e tabela fecham com fonte e data de apuração.
9. Traduza o jargão. Quem lê não é do mercado financeiro.
10. Não acrescente ressalva regulatória, aviso legal ou nota de risco.

### Geração de imagem

```
Classic-modern brand system, sober and quiet authority, closer to Montblanc than to a fintech.
Deep navy (#0D2A54) and brass (#AA7D41) on pure white (#FFFFFF), neutral near-black text
(#171717). Playfair Display for headlines, Inter for everything else. Flat solid fills; the only
allowed gradient is a single-colour transparent-to-solid veil over a textured background, never
on type or UI. No shadow, no glow, no glassmorphism. Sharp editorial layout on a 12-column grid,
generous margins, 15px corner radius on screen elements. No stock-market iconography.
```

## Arquivos

Os ativos prontos para uso ficam neste pacote, em `assets/`:

| Grupo | Pasta | Formatos |
|---|---|---|
| Logo | `assets/logo/` | svg · png 1x 2x 4x · pdf |
| Tagline | `assets/tagline/` | svg · png 1x 2x 4x · pdf |
| Ícone | `assets/icone/` | svg · png 1x 2x 4x · pdf |
| Gradiente | `assets/gradiente/` | svg · png 1x 2x 4x · pdf |
| Favicon | `assets/favicon/` | svg · png 1x 2x 4x · pdf |
| Paleta | `assets/paleta/` | svg · png · pdf · **ase** (Illustrator, Photoshop, InDesign) · **gpl** (Inkscape, Krita) · txt · json |
| Textura | `assets/textura/` | svg e pdf do ladrilho · png de todas |
| Wallpaper | `assets/wallpaper/` | png, no tamanho nativo |
| Social | `assets/social/` | png, no tamanho de cada plataforma |
| Splash | `assets/splash/` | png 1290 × 2796 |
| Foto | `assets/foto/` | png |
| Exemplos | `exemplos/` | png e pdf das folhas do sistema |

| Biblioteca Lucide completa | `assets/icone/lucide/` | 1.767 svg |
| Fontes | `assets/fonte/` | Playfair Display em otf, Inter variável em ttf, e woff2 das duas para web |

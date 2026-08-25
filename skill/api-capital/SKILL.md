---
name: api-capital
description: Produz qualquer peça visual da API Capital dentro da identidade oficial — proposta comercial, apresentação de reunião, relatório de carteira, one-pager, e-mail, slide, carta, post e página. Use SEMPRE que o pedido citar API Capital, "com a cara da API", "no padrão da API", "identidade da API Capital", ou quando a peça for assinada pela API Capital. Carrega a especificação viva do design system (cor, tipografia, espaço, componentes), o catálogo de vetos anti-slop e os endereços dos ativos oficiais (logo, ícone, textura, gradiente, foto).
---

# Peça da API Capital

A API Capital é uma consultoria de investimentos independente. O visual traduz isso em
sobriedade: azul-meia-noite e latão sobre branco, Playfair Display no título e Inter em todo o
resto, zero sombra, canto de 15 px.

**A fonte da verdade não mora nesta skill.** Ela mora no design system publicado, e é buscada a
cada trabalho. Esta skill carrega uma cópia de emergência em `referencia/`, para o caso de a
busca falhar.

```
BASE = https://lebeninca.github.io/api-capital-design-system
```

## Protocolo obrigatório

Execute nesta ordem. Não pule, não resuma, não trabalhe de memória.

### 1 · Carregue o material vivo

Busque, nesta ordem:

1. `BASE/versao.json` — o carimbo da versão publicada.
2. `BASE/DESIGN.md` — a lei: tokens, tipografia, layout, forma, os 23 componentes.
3. `BASE/ANTI_SLOP_VISUAL.md` — os vetos, com o teste de cada um.
4. `BASE/INDICE_ATIVOS.md` — como montar a URL de qualquer ativo, e os essenciais prontos.

**Leia os dois primeiros por inteiro antes de desenhar qualquer coisa.**

Se a busca na web não estiver disponível, use a cópia de `referencia/` e **declare isso na
conferência final** — a cópia pode estar velha.

### 2 · Monte a peça consumindo o sistema, nunca reescrevendo

Em peça de tela (HTML), o `<head>` começa sempre com a folha oficial:

```html
<link rel="stylesheet" href="https://lebeninca.github.io/api-capital-design-system/tokens/api-capital.css">
```

Ela traz as fontes, as variáveis e as 23 classes de componente. A partir daí:

- **Cor sai de variável**: `var(--api-acao)`, `var(--api-texto)`, `var(--api-fundo)`. Escrever
  `#0D2A54` na mão é erro, mesmo que o valor esteja certo.
- **Componente sai de classe**: `.api-botao-primario`, `.api-card`, `.api-tabela`. Não invente
  botão novo.
- **Logo e imagem saem por URL**, do índice de ativos. O logotipo nunca se remonta com texto, não
  se recolore, não se estica.
- **Valor que não existe no `DESIGN.md` é erro.** Faltou um valor? Pergunte, não invente.

### 3 · Passe pelos vetos antes de entregar

Confira a peça contra o `ANTI_SLOP_VISUAL.md`, veto por veto. Os que mais reincidem:

- sombra em qualquer nível — a separação se faz com fundo sólido ou linha;
- gradiente em botão, card, texto ou ícone;
- cor fora da paleta, cinza genérico de framework, preto puro;
- canto diferente de 15 px, e cápsula;
- terceira família tipográfica, e número em Playfair (número é sempre Inter);
- antetítulo — vetado; o que se diria nele vai para subtítulo ou linha-fina;
- peça longa com toda seção em branco: a seção alterna com off-white `#F2F0EF` ou cinza-claro
  `#F0F0F0`, uma superfície por peça, pintando a faixa inteira e nunca o card de dentro.

### 4 · Feche com o bloco de conferência

Toda entrega termina com este bloco, preenchido de verdade:

```
CONFERÊNCIA — design system da API Capital
Versão lida: <o design_system do versao.json>   Fonte: <viva | cópia local da skill>
Tokens: consumidos por <link> da folha oficial
Ativos usados: <as URLs de logo, ícone, imagem>
Vetos conferidos: <quantos> · Ocorrências corrigidas: <quais>
```

Sem esse bloco, a peça não está pronta.

## Régua de conteúdo

O texto da peça também é da marca. Escreva em português do Brasil, direto, sem corporativês.
Nada de "não é X, é Y", que é o clichê que denuncia texto de máquina. Não invente número,
rentabilidade, prazo ou dado de cliente: o que não foi informado, pergunte.

**A API Capital não recebe comissão de produto** — é consultoria independente, e o material nunca
sugere o contrário.

## Quando a peça for para impressão

Papel A4, sempre, declarado no CSS:

```css
@page { size: A4; margin: 20mm; }
```

Canto vivo no impresso, canto de 15 px em tela.

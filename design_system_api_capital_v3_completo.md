# Design System da API Capital — arquivo único

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

/* Tokens da API Capital. GERADO por tokens/gerar_tokens.py a partir de DESIGN.md.
   Nao edite este arquivo: edite o DESIGN.md e rode o gerador. */

:root {
  /* colors */
  --api-azul: #0D2A54;
  --api-latao: #AA7D41;
  --api-azul-claro: #418ECE;
  --api-preto: #171717;
  --api-branco: #FFFFFF;
  --api-creme: #F1EAD8;
  --api-areia: #E4CB8D;
  --api-azul-var: #152548;
  --api-latao-var: #9A7239;
  --api-azul-claro-var: #3E82B9;
  --api-preto-var: #020102;
  --api-quadro: #E6E7E8;
  --api-off-white: #F2F0EF;
  --api-cinza-claro: #F0F0F0;
  --api-creme-var: #DBD4C5;
  --api-areia-var: #D0B980;
  --api-erro: #B71313;
  --api-ok: #0E7A47;
  --api-acao: var(--api-azul);
  --api-acao-hover: var(--api-azul-var);
  --api-acao-secundaria: var(--api-azul-claro);
  --api-acao-secundaria-hover: var(--api-azul-claro-var);
  --api-texto: var(--api-preto);
  --api-texto-fraco: rgba(23,23,23,0.5);
  --api-sobre-escuro: var(--api-branco);
  --api-fundo: var(--api-branco);
  --api-fundo-bloco: var(--api-quadro);
  --api-fundo-quente: var(--api-creme);
  --api-fundo-secao: var(--api-off-white);
  --api-fundo-escuro: var(--api-azul);
  --api-borda: var(--api-quadro);
  --api-fio: var(--api-azul);
  --api-destaque: var(--api-latao);
  --api-realce: var(--api-areia);

  /* rounded */
  --api-canto-vivo: 0px;
  --api-x4: 15px;

  /* spacing */
  --api-x1: 4px;
  --api-x2: 8px;
  --api-x4: 16px;
  --api-x6: 24px;
  --api-x10: 40px;
  --api-x16: 64px;

  /* typography */
  --api-display-font-family: 'Playfair Display', Georgia, serif;
  --api-display-font-size: 48px;
  --api-display-font-weight: 700;
  --api-display-line-height: 1.15;
  --api-display-letter-spacing: -0.96px;
  --api-secao-font-family: 'Playfair Display', Georgia, serif;
  --api-secao-font-size: 36px;
  --api-secao-font-weight: 700;
  --api-secao-line-height: 1.2;
  --api-secao-letter-spacing: -0.72px;
  --api-titulo-font-family: Inter, system-ui, sans-serif;
  --api-titulo-font-size: 28px;
  --api-titulo-font-weight: 600;
  --api-titulo-line-height: 1.3;
  --api-titulo-letter-spacing: 0;
  --api-citacao-font-family: 'Playfair Display', Georgia, serif;
  --api-citacao-font-size: 22px;
  --api-citacao-font-weight: 400;
  --api-citacao-font-style: italic;
  --api-citacao-line-height: 1.45;
  --api-citacao-letter-spacing: 0;
  --api-corpo-grande-font-family: Inter, system-ui, sans-serif;
  --api-corpo-grande-font-size: 19px;
  --api-corpo-grande-font-weight: 400;
  --api-corpo-grande-line-height: 1.6;
  --api-corpo-grande-letter-spacing: 0;
  --api-corpo-font-family: Inter, system-ui, sans-serif;
  --api-corpo-font-size: 17px;
  --api-corpo-font-weight: 400;
  --api-corpo-line-height: 1.6;
  --api-corpo-letter-spacing: 0;
  --api-corpo-pequeno-font-family: Inter, system-ui, sans-serif;
  --api-corpo-pequeno-font-size: 15px;
  --api-corpo-pequeno-font-weight: 400;
  --api-corpo-pequeno-line-height: 1.5;
  --api-corpo-pequeno-letter-spacing: 0;
  --api-rotulo-font-family: Inter, system-ui, sans-serif;
  --api-rotulo-font-size: 13px;
  --api-rotulo-font-weight: 600;
  --api-rotulo-line-height: 1.2;
  --api-rotulo-letter-spacing: 4px;
  --api-rotulo-text-transform: uppercase;
  --api-numero-grande-font-family: Inter, system-ui, sans-serif;
  --api-numero-grande-font-size: 40px;
  --api-numero-grande-font-weight: 700;
  --api-numero-grande-line-height: 1.1;
  --api-numero-grande-letter-spacing: -0.4px;
  --api-numero-grande-font-feature: tnum;
  --api-numero-font-family: Inter, system-ui, sans-serif;
  --api-numero-font-size: 17px;
  --api-numero-font-weight: 700;
  --api-numero-line-height: 1.3;
  --api-numero-letter-spacing: 0;
  --api-numero-font-feature: tnum;
  --api-botao-font-family: Inter, system-ui, sans-serif;
  --api-botao-font-size: 17px;
  --api-botao-font-weight: 600;
  --api-botao-line-height: 1;
  --api-botao-letter-spacing: 0;
  --api-botao-pequeno-font-family: Inter, system-ui, sans-serif;
  --api-botao-pequeno-font-size: 15px;
  --api-botao-pequeno-font-weight: 600;
  --api-botao-pequeno-line-height: 1;
  --api-botao-pequeno-letter-spacing: 0;
  --api-legenda-font-family: Inter, system-ui, sans-serif;
  --api-legenda-font-size: 14px;
  --api-legenda-font-weight: 400;
  --api-legenda-line-height: 1.4;
  --api-legenda-letter-spacing: 0;

}

/* classes de tipografia */
.api-display {
  font-family: var(--api-display-font-family);
  font-size: var(--api-display-font-size);
  font-weight: var(--api-display-font-weight);
  line-height: var(--api-display-line-height);
  letter-spacing: var(--api-display-letter-spacing);
}
.api-secao {
  font-family: var(--api-secao-font-family);
  font-size: var(--api-secao-font-size);
  font-weight: var(--api-secao-font-weight);
  line-height: var(--api-secao-line-height);
  letter-spacing: var(--api-secao-letter-spacing);
}
.api-titulo {
  font-family: var(--api-titulo-font-family);
  font-size: var(--api-titulo-font-size);
  font-weight: var(--api-titulo-font-weight);
  line-height: var(--api-titulo-line-height);
  letter-spacing: var(--api-titulo-letter-spacing);
}
.api-citacao {
  font-family: var(--api-citacao-font-family);
  font-size: var(--api-citacao-font-size);
  font-weight: var(--api-citacao-font-weight);
  line-height: var(--api-citacao-line-height);
  letter-spacing: var(--api-citacao-letter-spacing);
  font-style: var(--api-citacao-font-style);
}
.api-corpo-grande {
  font-family: var(--api-corpo-grande-font-family);
  font-size: var(--api-corpo-grande-font-size);
  font-weight: var(--api-corpo-grande-font-weight);
  line-height: var(--api-corpo-grande-line-height);
  letter-spacing: var(--api-corpo-grande-letter-spacing);
}
.api-corpo {
  font-family: var(--api-corpo-font-family);
  font-size: var(--api-corpo-font-size);
  font-weight: var(--api-corpo-font-weight);
  line-height: var(--api-corpo-line-height);
  letter-spacing: var(--api-corpo-letter-spacing);
}
.api-corpo-pequeno {
  font-family: var(--api-corpo-pequeno-font-family);
  font-size: var(--api-corpo-pequeno-font-size);
  font-weight: var(--api-corpo-pequeno-font-weight);
  line-height: var(--api-corpo-pequeno-line-height);
  letter-spacing: var(--api-corpo-pequeno-letter-spacing);
}
.api-rotulo {
  font-family: var(--api-rotulo-font-family);
  font-size: var(--api-rotulo-font-size);
  font-weight: var(--api-rotulo-font-weight);
  line-height: var(--api-rotulo-line-height);
  letter-spacing: var(--api-rotulo-letter-spacing);
  text-transform: var(--api-rotulo-text-transform);
}
.api-numero-grande {
  font-family: var(--api-numero-grande-font-family);
  font-size: var(--api-numero-grande-font-size);
  font-weight: var(--api-numero-grande-font-weight);
  line-height: var(--api-numero-grande-line-height);
  letter-spacing: var(--api-numero-grande-letter-spacing);
  font-feature-settings: "tnum";
}
.api-numero {
  font-family: var(--api-numero-font-family);
  font-size: var(--api-numero-font-size);
  font-weight: var(--api-numero-font-weight);
  line-height: var(--api-numero-line-height);
  letter-spacing: var(--api-numero-letter-spacing);
  font-feature-settings: "tnum";
}
.api-botao {
  font-family: var(--api-botao-font-family);
  font-size: var(--api-botao-font-size);
  font-weight: var(--api-botao-font-weight);
  line-height: var(--api-botao-line-height);
  letter-spacing: var(--api-botao-letter-spacing);
}
.api-botao-pequeno {
  font-family: var(--api-botao-pequeno-font-family);
  font-size: var(--api-botao-pequeno-font-size);
  font-weight: var(--api-botao-pequeno-font-weight);
  line-height: var(--api-botao-pequeno-line-height);
  letter-spacing: var(--api-botao-pequeno-letter-spacing);
}
.api-legenda {
  font-family: var(--api-legenda-font-family);
  font-size: var(--api-legenda-font-size);
  font-weight: var(--api-legenda-font-weight);
  line-height: var(--api-legenda-line-height);
  letter-spacing: var(--api-legenda-letter-spacing);
}

/* Componentes da API Capital. GERADO por tokens/gerar_tokens.py a partir de DESIGN.md.
   Nao edite este arquivo: edite o DESIGN.md e rode o gerador.
   Depende de tokens.css (variaveis) e fontes.css (@font-face). */

.api-botao-primario {
  font-family: var(--api-botao-font-family);
  font-size: var(--api-botao-font-size);
  font-weight: var(--api-botao-font-weight);
  line-height: var(--api-botao-line-height);
  letter-spacing: var(--api-botao-letter-spacing);
  background-color: var(--api-acao);
  color: var(--api-sobre-escuro);
  border-radius: var(--api-canto);
  padding: 0 24px;
  height: 48px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

.api-botao-primario-hover {
  font-family: var(--api-botao-font-family);
  font-size: var(--api-botao-font-size);
  font-weight: var(--api-botao-font-weight);
  line-height: var(--api-botao-line-height);
  letter-spacing: var(--api-botao-letter-spacing);
  background-color: var(--api-acao-hover);
  color: var(--api-sobre-escuro);
  border-radius: var(--api-canto);
  padding: 0 24px;
  height: 48px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

.api-botao-secundario {
  font-family: var(--api-botao-font-family);
  font-size: var(--api-botao-font-size);
  font-weight: var(--api-botao-font-weight);
  line-height: var(--api-botao-line-height);
  letter-spacing: var(--api-botao-letter-spacing);
  background-color: var(--api-fundo);
  color: var(--api-acao);
  border-color: var(--api-acao);
  border-width: 1px;
  border-radius: var(--api-canto);
  padding: 0 24px;
  height: 48px;
  border-style: solid;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

.api-botao-azul-claro {
  font-family: var(--api-botao-font-family);
  font-size: var(--api-botao-font-size);
  font-weight: var(--api-botao-font-weight);
  line-height: var(--api-botao-line-height);
  letter-spacing: var(--api-botao-letter-spacing);
  background-color: var(--api-acao-secundaria);
  color: var(--api-sobre-escuro);
  border-radius: var(--api-canto);
  padding: 0 24px;
  height: 48px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

.api-botao-sobre-escuro {
  font-family: var(--api-botao-font-family);
  font-size: var(--api-botao-font-size);
  font-weight: var(--api-botao-font-weight);
  line-height: var(--api-botao-line-height);
  letter-spacing: var(--api-botao-letter-spacing);
  background-color: var(--api-branco);
  color: var(--api-azul);
  border-radius: var(--api-canto);
  padding: 0 24px;
  height: 48px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

.api-botao-texto {
  font-family: var(--api-botao-font-family);
  font-size: var(--api-botao-font-size);
  font-weight: var(--api-botao-font-weight);
  line-height: var(--api-botao-line-height);
  letter-spacing: var(--api-botao-letter-spacing);
  background-color: transparent;
  color: var(--api-acao);
  border-radius: var(--api-canto-vivo);
  padding: 0;
  height: 48px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

.api-campo {
  font-family: var(--api-corpo-font-family);
  font-size: var(--api-corpo-font-size);
  font-weight: var(--api-corpo-font-weight);
  line-height: var(--api-corpo-line-height);
  letter-spacing: var(--api-corpo-letter-spacing);
  background-color: var(--api-fundo);
  color: var(--api-texto);
  border-color: var(--api-borda);
  border-width: 1px;
  border-radius: var(--api-canto);
  padding: 0 16px;
  height: 48px;
  border-style: solid;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

.api-campo-foco {
  font-family: var(--api-corpo-font-family);
  font-size: var(--api-corpo-font-size);
  font-weight: var(--api-corpo-font-weight);
  line-height: var(--api-corpo-line-height);
  letter-spacing: var(--api-corpo-letter-spacing);
  background-color: var(--api-fundo);
  color: var(--api-texto);
  border-color: var(--api-acao);
  border-width: 1px;
  outline: 3px solid var(--api-acao-secundaria);
  outline-offset: 2px;
  border-radius: var(--api-canto);
  padding: 0 16px;
  height: 48px;
  border-style: solid;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

.api-campo-erro {
  font-family: var(--api-corpo-font-family);
  font-size: var(--api-corpo-font-size);
  font-weight: var(--api-corpo-font-weight);
  line-height: var(--api-corpo-line-height);
  letter-spacing: var(--api-corpo-letter-spacing);
  background-color: var(--api-fundo);
  color: var(--api-texto);
  border-color: var(--api-erro);
  border-width: 1px;
  border-radius: var(--api-canto);
  padding: 0 16px;
  height: 48px;
  border-style: solid;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

.api-card-conteudo {
  font-family: var(--api-corpo-font-family);
  font-size: var(--api-corpo-font-size);
  font-weight: var(--api-corpo-font-weight);
  line-height: var(--api-corpo-line-height);
  letter-spacing: var(--api-corpo-letter-spacing);
  background-color: var(--api-fundo);
  color: var(--api-texto);
  border-color: var(--api-fio);
  border-width: 1px;
  border-radius: var(--api-canto);
  padding: 40px;
  border-style: solid;
}

.api-card-dado {
  font-family: var(--api-corpo-font-family);
  font-size: var(--api-corpo-font-size);
  font-weight: var(--api-corpo-font-weight);
  line-height: var(--api-corpo-line-height);
  letter-spacing: var(--api-corpo-letter-spacing);
  background-color: var(--api-fundo-bloco);
  color: var(--api-texto);
  border-radius: var(--api-canto);
  padding: 40px;
}

.api-card-destaque {
  font-family: var(--api-corpo-font-family);
  font-size: var(--api-corpo-font-size);
  font-weight: var(--api-corpo-font-weight);
  line-height: var(--api-corpo-line-height);
  letter-spacing: var(--api-corpo-letter-spacing);
  background-color: var(--api-fundo-escuro);
  color: var(--api-sobre-escuro);
  border-radius: var(--api-canto);
  padding: 40px;
}

.api-card-quente {
  font-family: var(--api-corpo-font-family);
  font-size: var(--api-corpo-font-size);
  font-weight: var(--api-corpo-font-weight);
  line-height: var(--api-corpo-line-height);
  letter-spacing: var(--api-corpo-letter-spacing);
  background-color: var(--api-fundo-quente);
  color: var(--api-azul);
  border-radius: var(--api-canto);
  padding: 40px;
}

.api-caixa-latao {
  font-family: var(--api-titulo-font-family);
  font-size: var(--api-titulo-font-size);
  font-weight: var(--api-titulo-font-weight);
  line-height: var(--api-titulo-line-height);
  letter-spacing: var(--api-titulo-letter-spacing);
  background-color: var(--api-destaque);
  color: var(--api-sobre-escuro);
  border-radius: var(--api-canto);
  padding: 24px;
}

.api-caixa-ocre {
  font-family: var(--api-corpo-font-family);
  font-size: var(--api-corpo-font-size);
  font-weight: var(--api-corpo-font-weight);
  line-height: var(--api-corpo-line-height);
  letter-spacing: var(--api-corpo-letter-spacing);
  background-color: var(--api-realce);
  color: var(--api-azul);
  border-radius: var(--api-canto);
  padding: 24px;
}

.api-nav-clara {
  font-family: var(--api-corpo-font-family);
  font-size: var(--api-corpo-font-size);
  font-weight: var(--api-corpo-font-weight);
  line-height: var(--api-corpo-line-height);
  letter-spacing: var(--api-corpo-letter-spacing);
  background-color: var(--api-fundo);
  color: var(--api-texto);
  padding: 0 40px;
  height: 96px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

.api-nav-escura {
  font-family: var(--api-corpo-font-family);
  font-size: var(--api-corpo-font-size);
  font-weight: var(--api-corpo-font-weight);
  line-height: var(--api-corpo-line-height);
  letter-spacing: var(--api-corpo-letter-spacing);
  background-color: var(--api-fundo-escuro);
  color: var(--api-sobre-escuro);
  padding: 0 40px;
  height: 96px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

.api-aviso-erro {
  font-family: var(--api-corpo-pequeno-font-family);
  font-size: var(--api-corpo-pequeno-font-size);
  font-weight: var(--api-corpo-pequeno-font-weight);
  line-height: var(--api-corpo-pequeno-line-height);
  letter-spacing: var(--api-corpo-pequeno-letter-spacing);
  background-color: var(--api-fundo);
  color: var(--api-texto);
  border-color: var(--api-erro);
  border-width: 1px;
  border-radius: var(--api-canto);
  padding: 16px;
  border-style: solid;
}

.api-aviso-ok {
  font-family: var(--api-corpo-pequeno-font-family);
  font-size: var(--api-corpo-pequeno-font-size);
  font-weight: var(--api-corpo-pequeno-font-weight);
  line-height: var(--api-corpo-pequeno-line-height);
  letter-spacing: var(--api-corpo-pequeno-letter-spacing);
  background-color: var(--api-fundo);
  color: var(--api-texto);
  border-color: var(--api-ok);
  border-width: 1px;
  border-radius: var(--api-canto);
  padding: 16px;
  border-style: solid;
}

.api-tabela-cabecalho {
  font-family: var(--api-rotulo-font-family);
  font-size: var(--api-rotulo-font-size);
  font-weight: var(--api-rotulo-font-weight);
  line-height: var(--api-rotulo-line-height);
  letter-spacing: var(--api-rotulo-letter-spacing);
  text-transform: var(--api-rotulo-text-transform);
  background-color: var(--api-fundo-escuro);
  color: var(--api-sobre-escuro);
  border-radius: var(--api-canto-vivo);
  padding: 16px;
}

.api-tabela-linha {
  font-family: var(--api-corpo-pequeno-font-family);
  font-size: var(--api-corpo-pequeno-font-size);
  font-weight: var(--api-corpo-pequeno-font-weight);
  line-height: var(--api-corpo-pequeno-line-height);
  letter-spacing: var(--api-corpo-pequeno-letter-spacing);
  background-color: var(--api-fundo);
  color: var(--api-texto);
  padding: 16px;
}

.api-tabela-zebra {
  font-family: var(--api-corpo-pequeno-font-family);
  font-size: var(--api-corpo-pequeno-font-size);
  font-weight: var(--api-corpo-pequeno-font-weight);
  line-height: var(--api-corpo-pequeno-line-height);
  letter-spacing: var(--api-corpo-pequeno-letter-spacing);
  background-color: var(--api-fundo-bloco);
  color: var(--api-texto);
  padding: 16px;
}

.api-rodape {
  font-family: var(--api-legenda-font-family);
  font-size: var(--api-legenda-font-size);
  font-weight: var(--api-legenda-font-weight);
  line-height: var(--api-legenda-line-height);
  letter-spacing: var(--api-legenda-letter-spacing);
  background-color: var(--api-fundo);
  color: var(--api-texto-fraco);
  padding: 64px 40px;
}
```

---

# Parte 2 · A especificação

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

---

# Parte 3 · Os vetos

# Catálogo de vetos visuais da API Capital

## Como ler

| Coluna | O que traz |
|---|---|
| **ID** | O nome do defeito. É o que o validador imprime, e o que se cita numa correção |
| **O defeito** | Como ele aparece na peça |
| **O certo** | O que fazer no lugar |
| **Teste** | O que a máquina procura. `—` marca o que só o olho julga |

**Alcance:** `css` vale para peça em código (HTML, CSS, e-mail, tela). `pen` vale para arquivo do
Pencil e para peça montada por MCP de programa de design. `txt` vale para o texto de qualquer
peça.

---

## 1 · Cor

| ID | O defeito | O certo | Teste |
|---|---|---|---|
| `cor-fora-da-paleta` | Hex que não existe na paleta do `DESIGN.md` | Consumir token, nunca escrever hex | `css` `pen`: extrair todo hex e `rgb()` e cruzar com a paleta |
| `preto-puro` | `#000000` em texto ou fundo | Quase-preto `#171717` | `css` `pen`: procurar `#000`, `#000000`, `rgb(0,0,0)` |
| `bege-de-fundo` | Creme ou papel como fundo do documento, ou creme alternando as seções de uma peça longa | Branco puro `#FFFFFF` no `body`. O ritmo da peça longa é off-white `#F2F0EF` ou cinza-claro `#F0F0F0`, nunca creme | `css`: fundo do `body` ou do container raiz em `#F1EAD8`, `#FBF9F3` ou similar; `#F1EAD8` em 2 ou mais blocos de seção irmãos |
| `parede-sem-divisao` | Peça longa com todas as seções em branco, sem nada que marque onde uma termina e a outra começa | Alternar a faixa da seção entre `#FFFFFF` e UMA superfície de seção — off-white `#F2F0EF` ou cinza-claro `#F0F0F0` (`DESIGN.md` §Ritmo de superfície) | `css`: 4 ou mais blocos de seção irmãos, todos sem `background` próprio ou todos em `{colors.fundo}` |
| `superficie-arlequim` | A alternância vira festa: três ou mais superfícies claras na mesma peça, ou cada card com o seu fundo | Duas claras no máximo — branco mais UMA de seção; a faixa pinta a seção inteira, o card de dentro volta ao branco | `css`: mais de duas cores claras distintas em fundo de bloco na mesma peça |
| `vermelho-verde-livre` | Vermelho ou verde da marca usados por gosto | Vermelho só no `m` da tagline e em erro; verde só em confirmação | `css` `pen`: uso de `#B71313` ou `#0E7A47` fora de elemento de erro, alerta ou confirmação |
| `opacidade-em-vez-de-cor` | Cor sólida rebaixada com alpha para simular um tom mais claro | A variação da cor, que já existe na paleta | `css` `pen`: preenchimento com `opacity` entre 0,05 e 0,6 em retângulo, célula ou fundo de bloco |
| `cinza-de-fabrica` | Cinza genérico de framework (`#F5F5F5`, `#EEE`, `#CCC`, `gray-100`) | `#E6E7E8`, a variação do branco | `css`: cinza fora da paleta em fundo ou borda |

## 2 · Sombra, brilho e profundidade

| ID | O defeito | O certo | Teste |
|---|---|---|---|
| `sombra` | Qualquer `box-shadow`, `text-shadow` ou `drop-shadow` | Separar por fundo sólido, cinza de quadro ou linha de alto contraste | `css`: propriedade presente. `pen`: nó com sombra |
| `glow` | Brilho colorido em volta de elemento | Nada. A marca não brilha | `css`: `box-shadow` com cor saturada e sem deslocamento |
| `glassmorphism` | Fundo borrado, vidro fosco, translucidez | Fundo sólido | `css`: `backdrop-filter`, `filter: blur` em container |
| `gradiente-em-elemento` | Degradê em botão, texto, ícone, caixa ou card | Gradiente só como véu de legibilidade de fundo, uma cor do transparente ao cheio | `css`: `linear-gradient` ou `radial-gradient` fora de fundo de peça; qualquer gradiente com duas cores diferentes |
| `gradiente-de-duas-cores` | Degradê entre duas cores diferentes | Uma cor só, do transparente ao cheio | `css` `pen`: contar cores distintas nas paradas |

## 3 · Forma

| ID | O defeito | O certo | Teste |
|---|---|---|---|
| `canto-fora-do-token` | `border-radius` diferente de 15 px em tela | 15 px em tela, canto vivo no impresso | `css`: todo `border-radius` que não seja 0 ou 15 |
| `pill` | Canto de `9999px`, botão ou tag em cápsula | Canto de 15 | `css`: raio acima de 40 px ou `9999px` |
| `contorno-cinza-1px` | Borda cinza clara de 1 px em volta de tudo | Fundo sólido ou fio de alto contraste | `css`: `border: 1px solid` em cinza claro, em mais de 3 elementos |
| `callout-faixa-lateral` | Caixa de destaque com faixa colorida na lateral ou no topo | Caixa do sistema: contorno, quadro, sólida, latão ou ocre | `css`: `border-left`, `border-right` ou `border-top` com espessura acima de 2 px e cor diferente das outras bordas do mesmo elemento |
| `fio-fora-da-escala` | Espessura de fio fora de 0,5 / 1 / 2 / 6 pt | As quatro espessuras do sistema | `css` `pen`: espessura de linha ou altura de retângulo divisor fora da escala |

## 4 · Tipografia

| ID | O defeito | O certo | Teste |
|---|---|---|---|
| `terceira-familia` | Uma terceira fonte além de Playfair Display e Inter | Duas famílias, e só duas | `css` `pen`: coletar `font-family` distintas |
| `antetitulo` | Rótulo miúdo em caixa alta acima do título | Subtítulo ou linha-fina, abaixo do título | `css` `pen`: texto curto, caixa alta, corpo menor que o do texto, posicionado acima de um título |
| `numero-em-serifada` | Dado apresentado em Playfair | Todo número apresentado em Inter 700 ou 800 | `css` `pen`: nó cujo conteúdo é só número, moeda ou percentual, com família serifada |
| `micro-label` | Rótulos do tipo `01 / BLOCO 03` | Nada, ou um rótulo de seção de verdade | `txt`: padrão de dois números separados por barra em caixa alta |
| `textinho` | Linha pequena e cinza carregando informação que deveria estar no texto | Subir a informação para o corpo ou virar elemento visual | `css`: corpo abaixo de 12 px com cor de baixo contraste e mais de 40 caracteres |
| `caixa-alta-em-corpo` | Parágrafo inteiro em caixa alta | Caixa alta só em rótulo de seção, com tracking | `css` `txt`: bloco de texto com mais de 30 caracteres todo em maiúscula |
| `medida-de-linha` | Linha longa demais para o olho voltar | De 6 a 8 colunas no retrato, 5 a 7 no paisagem | `css`: largura do bloco de texto acima de 90 caracteres na fonte declarada |

## 5 · Layout e ritmo

| ID | O defeito | O certo | Teste |
|---|---|---|---|
| `respiro-fora-da-escala` | Junta entre elementos que não é 60 nem 120 | Os dois valores da escala do `DESIGN.md` | `pen` `css`: medir as juntas verticais e classificar |
| `respiro-duplicado` | Duas juntas vizinhas com respiros muito diferentes | Consistência: mesma natureza de junta, mesma medida | `pen` `css`: comparar juntas do mesmo nível na mesma peça |
| `tres-colunas-identicas` | Três cards iguais no topo da página | Hierarquia de verdade, ou uma disposição própria | `css`: três irmãos de mesma largura e mesma estrutura no primeiro terço |
| `fora-da-coluna` | Elemento que começa ou termina no meio de uma coluna | Começar e terminar em coluna | `pen` `css`: cruzar as bordas com as posições da grade de 12 |
| `margem-fora-da-regua` | Margem que não é a do formato | 20 mm no A4, nas duas orientações; 4% em tela | `pen` `css`: medir a caixa útil |
| `elemento-esticado-para-tapar-buraco` | Elemento crescido para preencher o pé da página | Sobra branca no fim é aceitável | `—` |

## 6 · Dado e gráfico

| ID | O defeito | O certo | Teste |
|---|---|---|---|
| `eixo-cortado` | Barra que não parte do zero | Barra do zero, sempre | `css` `pen`: valor mínimo do eixo diferente de zero em gráfico de barras |
| `grafico-sem-escala` | Gráfico sem eixo rotulado, sparkline decorativa | Eixo Y com valores | `css` `pen`: gráfico sem nó de rótulo de eixo |
| `percentual-sobre-fatia` | Número escrito em cima da fatia da rosca | Legenda ao lado, com o número | `pen`: texto centrado dentro de um setor |
| `fio-entre-linhas-de-tabela` | Linha divisória entre linhas de tabela | Zebra separa | `css` `pen`: borda horizontal repetida em linhas de tabela |
| `sem-fonte-e-data` | Tabela ou gráfico sem origem e data de apuração | Fonte e data no pé de cada um | `css` `pen`: bloco de dados sem nó de crédito abaixo |
| `rosca-sem-furo` | Gráfico de pizza cheio | Rosca, sempre com furo | `pen`: setor sem raio interno |

## 7 · Marca

| ID | O defeito | O certo | Teste |
|---|---|---|---|
| `simbolo-de-investimento` | Seta, candlestick ou gráfico como símbolo | O pelicano. A marca é o miolo | `—` |
| `logo-remontada` | Logotipo montado à mão, letra por letra | Usar o componente oficial | `pen`: texto com o conteúdo `API` ou `CAPITAL` fora de um componente de logo |
| `logo-fora-do-oficial` | Variação de logo gerada na hora, cor trocada, proporção alterada | Só os arquivos oficiais | `css`: imagem de logo fora da pasta de assets |
| `mais-de-uma-caixa-quente` | Duas ou mais caixas latão ou ocre na mesma página | No máximo uma | `pen` `css`: contar caixas quentes por página |
| `botao-latao` | Ação em latão | Ação em azul-meia-noite ou azul-claro | `css` `pen`: elemento clicável com fundo `#AA7D41` |

## 8 · Texto da peça

| ID | O defeito | O certo | Teste |
|---|---|---|---|
| `travessao` | O símbolo `—` | Hífen, dois-pontos, ponto ou parênteses | `txt`: presença do caractere |
| `forma-nao-e-x-e-y` | A fôrma `não é X, é Y` | Reescrever no jeito falado | `txt`: expressão regular |
| `canonizar` | O verbo e suas variações | Aprovar, fechar, oficializar | `txt`: `canoniz`, `canônic` |
| `corporativês` | Mindset, disrupção, alavancar, sinergia | Palavra comum | `txt`: lista de termos |
| `emoji-decorativo` | Emoji em peça séria | Nada, ou um ícone Lucide | `txt`: caractere emoji fora de contexto de interface |
| `jargao-sem-traducao` | Termo técnico solto para quem não é do ramo | Traduzir antes de usar | `—` |

## 9 · Acessibilidade

| ID | O defeito | O certo | Teste |
|---|---|---|---|
| `cor-sozinha-comunica` | Erro ou sucesso ditos só pela cor | Dizer em texto também | `css`: elemento de estado sem nó de texto |
| `foco-invisivel` | `outline: none` sem substituto | Anel de foco visível | `css`: `outline: none` ou `outline: 0` |
| `alvo-pequeno` | Área clicável abaixo de 44 px | 44 px de altura mínima em toque | `css`: altura declarada de botão e link em barra |

---

## O que a máquina não julga

Estes ficam com o Impeccable e com o passe humano antes da entrega. Estão listados aqui para
não sumirem, e **não** contam como veto do catálogo enquanto não tiverem teste:

- gosto de paleta e de tipografia
- ritmo de layout e cadência de leitura
- se a peça tem um momento próprio ou é montagem de blocos genéricos
- se a hierarquia diz o que importa primeiro
- se a imagem escolhida pertence ao mundo da marca

## Cobertura

O validador expõe os IDs que implementa. Um teste de cobertura confere que **todo ID deste
catálogo tem implementação, ou está declarado como `—`**. Catálogo e validador que se descolam
viram documento passivo de novo, que é exatamente o que esta frente existe para evitar.

| Estado | Contagem |
|---|---|
| Vetos catalogados | 48 |
| Com teste declarado | 45 |
| Só olho humano (`—`) | 3 |
| **Implementados no validador** | **0 (o validador ainda não existe)** |

---

# Parte 4 · O logo oficial, em SVG

## Logo oficial em azul-meia-noite, para fundo branco e claro

```svg
<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1000pt" height="723pt" viewBox="0 0 1000 723">
<path fill-rule="nonzero" fill="#0D2A54" fill-opacity="1" d="M 252.21875 558.902344 L 243.804688 558.902344 C 243.308594 556.488281 242.445312 554.351562 241.203125 552.527344 C 239.976562 550.695312 238.476562 549.152344 236.730469 547.902344 C 234.960938 546.644531 232.996094 545.683594 230.914062 545.066406 C 228.789062 544.429688 226.566406 544.117188 224.257812 544.117188 C 220.054688 544.117188 216.246094 545.183594 212.835938 547.308594 C 209.429688 549.433594 206.730469 552.574219 204.726562 556.714844 C 202.71875 560.855469 201.726562 565.9375 201.726562 571.957031 C 201.726562 577.972656 202.730469 583.054688 204.726562 587.195312 C 206.730469 591.339844 209.429688 594.464844 212.835938 596.589844 C 216.246094 598.714844 220.054688 599.785156 224.257812 599.785156 C 226.566406 599.785156 228.777344 599.472656 230.914062 598.835938 C 233.039062 598.199219 234.980469 597.261719 236.730469 595.996094 C 238.476562 594.734375 239.976562 593.195312 241.203125 591.347656 C 242.433594 589.503906 243.296875 587.378906 243.804688 584.984375 L 252.21875 584.984375 C 251.582031 588.535156 250.425781 591.714844 248.753906 594.519531 C 247.082031 597.324219 245 599.707031 242.511719 601.660156 C 240 603.625 237.167969 605.136719 234.140625 606.125 C 231.054688 607.140625 227.753906 607.65625 224.25 607.65625 C 218.316406 607.65625 213.050781 606.210938 208.4375 603.3125 C 203.820312 600.421875 200.183594 596.300781 197.542969 590.960938 C 194.898438 585.621094 193.574219 579.289062 193.574219 571.957031 C 193.574219 564.621094 194.898438 558.289062 197.542969 552.949219 C 200.183594 547.609375 203.820312 543.492188 208.4375 540.597656 C 213.050781 537.707031 218.316406 536.253906 224.25 536.253906 C 227.753906 536.253906 231.054688 536.757812 234.140625 537.785156 C 237.171875 538.769531 240.003906 540.28125 242.511719 542.25 C 245 544.203125 247.082031 546.585938 248.753906 549.378906 C 250.425781 552.171875 251.582031 555.355469 252.21875 558.9375 Z M 320.246094 606.6875 L 311.421875 606.6875 L 336.945312 537.191406 L 345.625 537.191406 L 371.148438 606.6875 L 362.324219 606.6875 L 341.558594 548.183594 L 341.019531 548.183594 L 320.257812 606.6875 Z M 323.503906 579.539062 L 359.066406 579.539062 L 359.066406 587.003906 L 323.503906 587.003906 Z M 433.609375 606.6875 L 433.609375 537.191406 L 457.09375 537.191406 C 462.539062 537.191406 467.003906 538.171875 470.476562 540.125 C 473.949219 542.078125 476.519531 544.71875 478.199219 548.054688 C 479.882812 551.386719 480.714844 555.085938 480.714844 559.183594 C 480.714844 563.28125 479.882812 567.003906 478.222656 570.347656 C 476.5625 573.691406 473.996094 576.355469 470.53125 578.339844 C 467.070312 580.324219 462.636719 581.308594 457.230469 581.308594 L 440.394531 581.308594 L 440.394531 573.84375 L 456.953125 573.84375 C 460.683594 573.84375 463.683594 573.195312 465.949219 571.910156 C 468.210938 570.617188 469.851562 568.871094 470.886719 566.671875 C 471.914062 564.46875 472.429688 561.96875 472.429688 559.183594 C 472.429688 556.402344 471.914062 553.910156 470.886719 551.71875 C 469.851562 549.53125 468.203125 547.804688 465.914062 546.542969 C 463.628906 545.28125 460.597656 544.65625 456.824219 544.65625 L 442.023438 544.65625 L 442.023438 606.6875 Z M 554.296875 537.191406 L 554.296875 606.6875 L 545.886719 606.6875 L 545.886719 537.191406 Z M 618.929688 544.65625 L 618.929688 537.191406 L 671.046875 537.191406 L 671.046875 544.65625 L 649.195312 544.65625 L 649.195312 606.6875 L 640.78125 606.6875 L 640.78125 544.65625 Z M 730.394531 606.6875 L 721.570312 606.6875 L 747.09375 537.191406 L 755.773438 537.191406 L 781.296875 606.6875 L 772.472656 606.6875 L 751.707031 548.183594 L 751.167969 548.183594 L 730.40625 606.6875 Z M 733.652344 579.539062 L 769.214844 579.539062 L 769.214844 587.003906 L 733.652344 587.003906 Z M 843.746094 606.6875 L 843.746094 537.191406 L 852.160156 537.191406 L 852.160156 599.222656 L 884.464844 599.222656 L 884.464844 606.6875 Z M 590.789062 477.1875 C 596.375 491.585938 601.421875 496.429688 609.738281 496.429688 L 609.738281 502.449219 L 518.21875 502.449219 L 518.21875 496.429688 C 532.617188 495.847656 539.371094 493.636719 539.371094 485.417969 C 539.371094 481.890625 538.195312 477.1875 535.84375 471.167969 L 517.777344 421.808594 L 452.398438 421.808594 L 444.320312 442.671875 C 438.59375 457.363281 436.089844 468.082031 436.089844 476.011719 C 436.089844 491.878906 446.371094 495.988281 462.832031 496.429688 L 462.832031 502.449219 L 402.308594 502.449219 L 402.308594 496.429688 C 411.121094 494.8125 419.933594 487.023438 428.453125 464.847656 L 496.914062 288.859375 L 517.777344 288.859375 Z M 485.75 334.839844 L 454.613281 415.78125 L 515.574219 415.78125 Z M 485.75 334.839844 "/>
<path fill-rule="nonzero" fill="#0D2A54" fill-opacity="1" d="M 675.902344 468.816406 C 675.902344 492.320312 681.339844 495.554688 708.078125 495.847656 L 708.078125 502.460938 L 609.738281 502.460938 L 609.738281 496.441406 C 628.960938 496.441406 628.023438 492.472656 628.023438 470.585938 L 628.023438 321.335938 C 628.023438 299.449219 624.496094 296.367188 605.542969 295.480469 L 605.542969 288.871094 L 698.554688 288.871094 C 754.523438 288.871094 781.835938 314.132812 781.835938 349.101562 C 781.835938 378.191406 762.882812 416.382812 691.929688 416.382812 L 675.914062 416.382812 L 675.914062 468.828125 Z M 675.902344 321.324219 L 675.902344 410.34375 L 688.835938 410.34375 C 724.386719 410.34375 731.871094 383.023438 731.871094 352.3125 C 731.871094 314.410156 721.882812 295.460938 694.5625 295.460938 C 679.136719 295.460938 675.902344 300.605469 675.902344 321.316406 Z M 884.574219 295.46875 C 865.332031 296.355469 861.957031 299.441406 861.957031 321.324219 L 861.957031 470.574219 C 861.957031 492.460938 865.480469 495.546875 884.574219 496.429688 L 884.574219 502.449219 L 791.585938 502.449219 L 791.585938 496.429688 C 810.6875 495.546875 814.0625 492.460938 814.0625 470.574219 L 814.0625 321.324219 C 814.0625 299.441406 810.535156 296.355469 791.585938 295.46875 L 791.585938 288.859375 L 884.574219 288.859375 Z M 477.058594 214.261719 C 473.507812 211.21875 469.25 215.273438 468.6875 216.019531 C 447.417969 230.71875 431.207031 240.621094 408.15625 252.28125 C 394.359375 259.261719 357.71875 285.589844 358.160156 288.234375 C 358.460938 290.023438 364.125 290.28125 363.78125 292.570312 C 362.605469 300.304688 351.992188 302.472656 351.992188 309.816406 C 351.992188 314.21875 354.050781 320.679688 359.476562 321.703125 C 362.355469 322.253906 368.601562 322.167969 371.816406 322.015625 C 391.285156 321.121094 416.429688 303.324219 429.488281 289.117188 C 448.019531 268.980469 454.589844 250.804688 467.804688 227.03125 C 471.394531 220.570312 480.132812 216.902344 477.046875 214.261719 Z M 476.617188 198.847656 C 473.433594 196.882812 468.246094 196.648438 466.042969 198.40625 C 463.359375 200.550781 459.929688 204.101562 456.800781 205.890625 C 435.226562 218.21875 425.628906 225.003906 409.6875 234.074219 C 396.074219 241.808594 376.355469 255.300781 358.601562 262.703125 C 348.03125 267.101562 359.046875 273.714844 351.117188 285.601562 C 350.234375 288.242188 357.167969 280.746094 358.601562 279.875 C 381.058594 266.21875 401.757812 249.046875 425.035156 234.832031 C 432.605469 230.203125 448.269531 220.238281 458.558594 212.945312 C 466.875 207.054688 469.128906 203.257812 472.214844 202.816406 C 476.164062 202.253906 477.5 204.132812 479.699219 205.902344 C 480.585938 205.902344 478.632812 200.097656 476.617188 198.859375 Z M 281.773438 370.371094 C 265.386719 343.101562 260.027344 283.292969 278.472656 261.386719 C 284.640625 253.898438 278.027344 242.886719 278.914062 225.273438 C 279.765625 208.144531 305.394531 140.449219 323.277344 121.152344 C 324.257812 120.097656 326.050781 117.960938 327.03125 115.425781 C 324.269531 115.46875 322.003906 115.609375 319.191406 115.78125 C 312.695312 116.179688 306.484375 118.554688 301.371094 122.554688 C 288.363281 132.738281 275.136719 146.683594 276.042969 161.203125 C 267.136719 147.082031 279.203125 126.707031 283.207031 120.679688 C 281.320312 121.273438 279.464844 121.875 277.652344 122.480469 C 271.871094 124.421875 266.585938 127.59375 262.207031 131.84375 C 249.984375 143.707031 238.066406 160.902344 241.5625 183.617188 C 231.519531 163.175781 235.21875 147.816406 239.628906 138.949219 C 237.34375 140.234375 235.152344 141.527344 233.039062 142.835938 C 222.070312 149.652344 213.472656 159.726562 208.640625 171.699219 C 203.019531 185.632812 200.703125 201.996094 207.789062 219.332031 C 196.875 206.085938 193.195312 193.679688 192.667969 183.628906 C 161.992188 229.015625 186.214844 346.585938 281.773438 370.371094 "/>
<path fill-rule="nonzero" fill="#0D2A54" fill-opacity="1" d="M 375.34375 340.203125 C 363.359375 332.597656 343.640625 329.628906 344.613281 310.097656 C 345.109375 300.011719 356.542969 297.28125 352.90625 289.355469 L 346.285156 289.128906 C 344.527344 288.6875 352.886719 281.199219 348.3125 280.144531 C 347.460938 279.949219 346.707031 280.175781 347.644531 281.234375 C 346.285156 284.726562 340.339844 284.070312 338.140625 280.542969 C 334.257812 274.328125 342.542969 269.972656 348.269531 271.742188 C 348.882812 271.933594 349.964844 268.320312 350.136719 267.695312 L 351.0625 265.332031 C 351.179688 265.03125 351.144531 264.691406 350.964844 264.421875 C 350.789062 264.152344 350.492188 263.984375 350.167969 263.976562 C 345.445312 263.84375 340.460938 264.6875 333.070312 266.671875 C 308.921875 273.1875 306.171875 288.652344 296.960938 299.699219 C 294.757812 302.339844 288.339844 305.40625 288.148438 306.742188 C 287.628906 310.410156 295.707031 308.996094 297.832031 308.058594 C 298.910156 309.203125 295.191406 313.785156 291.230469 315.101562 C 288.976562 315.855469 284.058594 316.859375 285.503906 319.058594 C 286.875 321.140625 297.960938 318.1875 300.042969 317.238281 C 299.894531 320.949219 296.753906 321.972656 296.960938 325.660156 C 296.992188 326.277344 297.402344 328.746094 299.171875 330.277344 C 299.601562 322.132812 303.0625 323.914062 304.003906 326.535156 C 307.292969 335.617188 315.609375 344.179688 323.816406 349.433594 C 334.828125 356.476562 358.601562 362.207031 350.234375 378.0625 C 341.785156 394.066406 323.460938 377.058594 309.136719 376.660156 C 306.074219 376.574219 299.515625 377.359375 296.28125 377.855469 C 295.308594 378.007812 289.214844 379.410156 288.933594 379.667969 C 288.902344 379.699219 288.871094 379.765625 288.835938 379.839844 C 187.996094 378.804688 150.6875 272.484375 146.199219 199.050781 C 126.707031 230.105469 115.425781 266.875 115.425781 306.300781 C 115.425781 335.867188 121.769531 363.941406 133.160156 389.226562 C 157.113281 401.382812 186.753906 411.960938 223.417969 419.910156 C 223.417969 419.910156 204.917969 431.796875 180.261719 435.324219 C 175.992188 435.941406 171.742188 438.324219 167.589844 441.777344 C 194.414062 471.375 229.902344 492.890625 270.015625 502.277344 C 299.019531 492.191406 333.96875 480.917969 363.445312 445.894531 C 364.375 444.796875 367.046875 437.613281 367.40625 436.210938 C 369.519531 429.167969 369.519531 439.035156 369.023438 443.382812 C 368.945312 444.039062 369.667969 444.492188 370.230469 444.128906 C 377.652344 439.371094 378.589844 433.039062 381.382812 424.570312 C 381.707031 423.601562 383.109375 423.589844 383.410156 424.570312 C 384.328125 427.546875 381.125 432.984375 383.261719 430.492188 C 389.859375 423.007812 392.871094 411.734375 392.351562 401.445312 C 392.320312 400.863281 393.269531 400.539062 393.832031 401.445312 C 394.789062 402.976562 394.714844 408.046875 394.714844 408.046875 C 399.203125 399.136719 400.011719 383.941406 397.089844 372 C 393.710938 358.183594 387.617188 348.019531 375.34375 340.234375 Z M 375.34375 340.203125 "/>
</svg>
```

## Logo oficial em branco, para fundo escuro ou imagem escura

```svg
<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1000pt" height="723pt" viewBox="0 0 1000 723">
<path fill-rule="nonzero" fill="#FFFFFF" fill-opacity="1" d="M 252.21875 558.902344 L 243.804688 558.902344 C 243.308594 556.488281 242.445312 554.351562 241.203125 552.527344 C 239.976562 550.695312 238.476562 549.152344 236.730469 547.902344 C 234.960938 546.644531 232.996094 545.683594 230.914062 545.066406 C 228.789062 544.429688 226.566406 544.117188 224.257812 544.117188 C 220.054688 544.117188 216.246094 545.183594 212.835938 547.308594 C 209.429688 549.433594 206.730469 552.574219 204.726562 556.714844 C 202.71875 560.855469 201.726562 565.9375 201.726562 571.957031 C 201.726562 577.972656 202.730469 583.054688 204.726562 587.195312 C 206.730469 591.339844 209.429688 594.464844 212.835938 596.589844 C 216.246094 598.714844 220.054688 599.785156 224.257812 599.785156 C 226.566406 599.785156 228.777344 599.472656 230.914062 598.835938 C 233.039062 598.199219 234.980469 597.261719 236.730469 595.996094 C 238.476562 594.734375 239.976562 593.195312 241.203125 591.347656 C 242.433594 589.503906 243.296875 587.378906 243.804688 584.984375 L 252.21875 584.984375 C 251.582031 588.535156 250.425781 591.714844 248.753906 594.519531 C 247.082031 597.324219 245 599.707031 242.511719 601.660156 C 240 603.625 237.167969 605.136719 234.140625 606.125 C 231.054688 607.140625 227.753906 607.65625 224.25 607.65625 C 218.316406 607.65625 213.050781 606.210938 208.4375 603.3125 C 203.820312 600.421875 200.183594 596.300781 197.542969 590.960938 C 194.898438 585.621094 193.574219 579.289062 193.574219 571.957031 C 193.574219 564.621094 194.898438 558.289062 197.542969 552.949219 C 200.183594 547.609375 203.820312 543.492188 208.4375 540.597656 C 213.050781 537.707031 218.316406 536.253906 224.25 536.253906 C 227.753906 536.253906 231.054688 536.757812 234.140625 537.785156 C 237.171875 538.769531 240.003906 540.28125 242.511719 542.25 C 245 544.203125 247.082031 546.585938 248.753906 549.378906 C 250.425781 552.171875 251.582031 555.355469 252.21875 558.9375 Z M 320.246094 606.6875 L 311.421875 606.6875 L 336.945312 537.191406 L 345.625 537.191406 L 371.148438 606.6875 L 362.324219 606.6875 L 341.558594 548.183594 L 341.019531 548.183594 L 320.257812 606.6875 Z M 323.503906 579.539062 L 359.066406 579.539062 L 359.066406 587.003906 L 323.503906 587.003906 Z M 433.609375 606.6875 L 433.609375 537.191406 L 457.09375 537.191406 C 462.539062 537.191406 467.003906 538.171875 470.476562 540.125 C 473.949219 542.078125 476.519531 544.71875 478.199219 548.054688 C 479.882812 551.386719 480.714844 555.085938 480.714844 559.183594 C 480.714844 563.28125 479.882812 567.003906 478.222656 570.347656 C 476.5625 573.691406 473.996094 576.355469 470.53125 578.339844 C 467.070312 580.324219 462.636719 581.308594 457.230469 581.308594 L 440.394531 581.308594 L 440.394531 573.84375 L 456.953125 573.84375 C 460.683594 573.84375 463.683594 573.195312 465.949219 571.910156 C 468.210938 570.617188 469.851562 568.871094 470.886719 566.671875 C 471.914062 564.46875 472.429688 561.96875 472.429688 559.183594 C 472.429688 556.402344 471.914062 553.910156 470.886719 551.71875 C 469.851562 549.53125 468.203125 547.804688 465.914062 546.542969 C 463.628906 545.28125 460.597656 544.65625 456.824219 544.65625 L 442.023438 544.65625 L 442.023438 606.6875 Z M 554.296875 537.191406 L 554.296875 606.6875 L 545.886719 606.6875 L 545.886719 537.191406 Z M 618.929688 544.65625 L 618.929688 537.191406 L 671.046875 537.191406 L 671.046875 544.65625 L 649.195312 544.65625 L 649.195312 606.6875 L 640.78125 606.6875 L 640.78125 544.65625 Z M 730.394531 606.6875 L 721.570312 606.6875 L 747.09375 537.191406 L 755.773438 537.191406 L 781.296875 606.6875 L 772.472656 606.6875 L 751.707031 548.183594 L 751.167969 548.183594 L 730.40625 606.6875 Z M 733.652344 579.539062 L 769.214844 579.539062 L 769.214844 587.003906 L 733.652344 587.003906 Z M 843.746094 606.6875 L 843.746094 537.191406 L 852.160156 537.191406 L 852.160156 599.222656 L 884.464844 599.222656 L 884.464844 606.6875 Z M 590.789062 477.1875 C 596.375 491.585938 601.421875 496.429688 609.738281 496.429688 L 609.738281 502.449219 L 518.21875 502.449219 L 518.21875 496.429688 C 532.617188 495.847656 539.371094 493.636719 539.371094 485.417969 C 539.371094 481.890625 538.195312 477.1875 535.84375 471.167969 L 517.777344 421.808594 L 452.398438 421.808594 L 444.320312 442.671875 C 438.59375 457.363281 436.089844 468.082031 436.089844 476.011719 C 436.089844 491.878906 446.371094 495.988281 462.832031 496.429688 L 462.832031 502.449219 L 402.308594 502.449219 L 402.308594 496.429688 C 411.121094 494.8125 419.933594 487.023438 428.453125 464.847656 L 496.914062 288.859375 L 517.777344 288.859375 Z M 485.75 334.839844 L 454.613281 415.78125 L 515.574219 415.78125 Z M 485.75 334.839844 "/>
<path fill-rule="nonzero" fill="#FFFFFF" fill-opacity="1" d="M 675.902344 468.816406 C 675.902344 492.320312 681.339844 495.554688 708.078125 495.847656 L 708.078125 502.460938 L 609.738281 502.460938 L 609.738281 496.441406 C 628.960938 496.441406 628.023438 492.472656 628.023438 470.585938 L 628.023438 321.335938 C 628.023438 299.449219 624.496094 296.367188 605.542969 295.480469 L 605.542969 288.871094 L 698.554688 288.871094 C 754.523438 288.871094 781.835938 314.132812 781.835938 349.101562 C 781.835938 378.191406 762.882812 416.382812 691.929688 416.382812 L 675.914062 416.382812 L 675.914062 468.828125 Z M 675.902344 321.324219 L 675.902344 410.34375 L 688.835938 410.34375 C 724.386719 410.34375 731.871094 383.023438 731.871094 352.3125 C 731.871094 314.410156 721.882812 295.460938 694.5625 295.460938 C 679.136719 295.460938 675.902344 300.605469 675.902344 321.316406 Z M 884.574219 295.46875 C 865.332031 296.355469 861.957031 299.441406 861.957031 321.324219 L 861.957031 470.574219 C 861.957031 492.460938 865.480469 495.546875 884.574219 496.429688 L 884.574219 502.449219 L 791.585938 502.449219 L 791.585938 496.429688 C 810.6875 495.546875 814.0625 492.460938 814.0625 470.574219 L 814.0625 321.324219 C 814.0625 299.441406 810.535156 296.355469 791.585938 295.46875 L 791.585938 288.859375 L 884.574219 288.859375 Z M 477.058594 214.261719 C 473.507812 211.21875 469.25 215.273438 468.6875 216.019531 C 447.417969 230.71875 431.207031 240.621094 408.15625 252.28125 C 394.359375 259.261719 357.71875 285.589844 358.160156 288.234375 C 358.460938 290.023438 364.125 290.28125 363.78125 292.570312 C 362.605469 300.304688 351.992188 302.472656 351.992188 309.816406 C 351.992188 314.21875 354.050781 320.679688 359.476562 321.703125 C 362.355469 322.253906 368.601562 322.167969 371.816406 322.015625 C 391.285156 321.121094 416.429688 303.324219 429.488281 289.117188 C 448.019531 268.980469 454.589844 250.804688 467.804688 227.03125 C 471.394531 220.570312 480.132812 216.902344 477.046875 214.261719 Z M 476.617188 198.847656 C 473.433594 196.882812 468.246094 196.648438 466.042969 198.40625 C 463.359375 200.550781 459.929688 204.101562 456.800781 205.890625 C 435.226562 218.21875 425.628906 225.003906 409.6875 234.074219 C 396.074219 241.808594 376.355469 255.300781 358.601562 262.703125 C 348.03125 267.101562 359.046875 273.714844 351.117188 285.601562 C 350.234375 288.242188 357.167969 280.746094 358.601562 279.875 C 381.058594 266.21875 401.757812 249.046875 425.035156 234.832031 C 432.605469 230.203125 448.269531 220.238281 458.558594 212.945312 C 466.875 207.054688 469.128906 203.257812 472.214844 202.816406 C 476.164062 202.253906 477.5 204.132812 479.699219 205.902344 C 480.585938 205.902344 478.632812 200.097656 476.617188 198.859375 Z M 281.773438 370.371094 C 265.386719 343.101562 260.027344 283.292969 278.472656 261.386719 C 284.640625 253.898438 278.027344 242.886719 278.914062 225.273438 C 279.765625 208.144531 305.394531 140.449219 323.277344 121.152344 C 324.257812 120.097656 326.050781 117.960938 327.03125 115.425781 C 324.269531 115.46875 322.003906 115.609375 319.191406 115.78125 C 312.695312 116.179688 306.484375 118.554688 301.371094 122.554688 C 288.363281 132.738281 275.136719 146.683594 276.042969 161.203125 C 267.136719 147.082031 279.203125 126.707031 283.207031 120.679688 C 281.320312 121.273438 279.464844 121.875 277.652344 122.480469 C 271.871094 124.421875 266.585938 127.59375 262.207031 131.84375 C 249.984375 143.707031 238.066406 160.902344 241.5625 183.617188 C 231.519531 163.175781 235.21875 147.816406 239.628906 138.949219 C 237.34375 140.234375 235.152344 141.527344 233.039062 142.835938 C 222.070312 149.652344 213.472656 159.726562 208.640625 171.699219 C 203.019531 185.632812 200.703125 201.996094 207.789062 219.332031 C 196.875 206.085938 193.195312 193.679688 192.667969 183.628906 C 161.992188 229.015625 186.214844 346.585938 281.773438 370.371094 "/>
<path fill-rule="nonzero" fill="#FFFFFF" fill-opacity="1" d="M 375.34375 340.203125 C 363.359375 332.597656 343.640625 329.628906 344.613281 310.097656 C 345.109375 300.011719 356.542969 297.28125 352.90625 289.355469 L 346.285156 289.128906 C 344.527344 288.6875 352.886719 281.199219 348.3125 280.144531 C 347.460938 279.949219 346.707031 280.175781 347.644531 281.234375 C 346.285156 284.726562 340.339844 284.070312 338.140625 280.542969 C 334.257812 274.328125 342.542969 269.972656 348.269531 271.742188 C 348.882812 271.933594 349.964844 268.320312 350.136719 267.695312 L 351.0625 265.332031 C 351.179688 265.03125 351.144531 264.691406 350.964844 264.421875 C 350.789062 264.152344 350.492188 263.984375 350.167969 263.976562 C 345.445312 263.84375 340.460938 264.6875 333.070312 266.671875 C 308.921875 273.1875 306.171875 288.652344 296.960938 299.699219 C 294.757812 302.339844 288.339844 305.40625 288.148438 306.742188 C 287.628906 310.410156 295.707031 308.996094 297.832031 308.058594 C 298.910156 309.203125 295.191406 313.785156 291.230469 315.101562 C 288.976562 315.855469 284.058594 316.859375 285.503906 319.058594 C 286.875 321.140625 297.960938 318.1875 300.042969 317.238281 C 299.894531 320.949219 296.753906 321.972656 296.960938 325.660156 C 296.992188 326.277344 297.402344 328.746094 299.171875 330.277344 C 299.601562 322.132812 303.0625 323.914062 304.003906 326.535156 C 307.292969 335.617188 315.609375 344.179688 323.816406 349.433594 C 334.828125 356.476562 358.601562 362.207031 350.234375 378.0625 C 341.785156 394.066406 323.460938 377.058594 309.136719 376.660156 C 306.074219 376.574219 299.515625 377.359375 296.28125 377.855469 C 295.308594 378.007812 289.214844 379.410156 288.933594 379.667969 C 288.902344 379.699219 288.871094 379.765625 288.835938 379.839844 C 187.996094 378.804688 150.6875 272.484375 146.199219 199.050781 C 126.707031 230.105469 115.425781 266.875 115.425781 306.300781 C 115.425781 335.867188 121.769531 363.941406 133.160156 389.226562 C 157.113281 401.382812 186.753906 411.960938 223.417969 419.910156 C 223.417969 419.910156 204.917969 431.796875 180.261719 435.324219 C 175.992188 435.941406 171.742188 438.324219 167.589844 441.777344 C 194.414062 471.375 229.902344 492.890625 270.015625 502.277344 C 299.019531 492.191406 333.96875 480.917969 363.445312 445.894531 C 364.375 444.796875 367.046875 437.613281 367.40625 436.210938 C 369.519531 429.167969 369.519531 439.035156 369.023438 443.382812 C 368.945312 444.039062 369.667969 444.492188 370.230469 444.128906 C 377.652344 439.371094 378.589844 433.039062 381.382812 424.570312 C 381.707031 423.601562 383.109375 423.589844 383.410156 424.570312 C 384.328125 427.546875 381.125 432.984375 383.261719 430.492188 C 389.859375 423.007812 392.871094 411.734375 392.351562 401.445312 C 392.320312 400.863281 393.269531 400.539062 393.832031 401.445312 C 394.789062 402.976562 394.714844 408.046875 394.714844 408.046875 C 399.203125 399.136719 400.011719 383.941406 397.089844 372 C 393.710938 358.183594 387.617188 348.019531 375.34375 340.234375 Z M 375.34375 340.203125 "/>
</svg>
```


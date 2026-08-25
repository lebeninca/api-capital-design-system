#!/bin/bash
# Empacota a skill da API Capital no .zip que a pessoa sobe no Claude.
# A pasta "api-capital" tem que ser a RAIZ do zip — é exigência do Claude.
set -euo pipefail
cd "$(dirname "$0")"

cp DESIGN.md ANTI_SLOP_VISUAL.md INDICE_ATIVOS.md versao.json skill/api-capital/referencia/
cp tokens/tokens.css tokens/componentes.css skill/api-capital/referencia/

cd skill
rm -f api-capital-claude-skill.zip
zip -qr api-capital-claude-skill.zip api-capital -x '*.DS_Store'
echo "skill/api-capital-claude-skill.zip: $(du -h api-capital-claude-skill.zip | cut -f1)"
unzip -l api-capital-claude-skill.zip | tail -3

#!/bin/bash
# Empacota a skill da API Capital no .zip que a pessoa sobe no Claude.
# A skill é um PONTEIRO: nada de design system viaja dentro dela — o material é lido do
# endereço publicado, a cada trabalho. Por isso ela não envelhece: mudou o repo, mudou a peça.
# A pasta "api-capital" tem que ser a RAIZ do zip — é exigência do Claude.
set -euo pipefail
cd "$(dirname "$0")/skill"
rm -f api-capital-claude-skill.zip
zip -qr api-capital-claude-skill.zip api-capital -x '*.DS_Store'
echo "skill/api-capital-claude-skill.zip: $(du -h api-capital-claude-skill.zip | cut -f1)"
unzip -l api-capital-claude-skill.zip | tail -3

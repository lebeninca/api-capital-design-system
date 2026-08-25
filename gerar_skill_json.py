#!/usr/bin/env python3
"""Publica o carimbo de versão da skill, lido do próprio SKILL.md.

A skill instalada compara a versão dela com este arquivo e avisa a pessoa quando estiver velha.
"""
import json, pathlib, re
RAIZ = pathlib.Path(__file__).parent
texto = (RAIZ / "skill/api-capital/SKILL.md").read_text(encoding="utf-8")
versao = int(re.search(r"\*\*Versão desta skill:\s*(\d+)\*\*", texto).group(1))
(RAIZ / "skill.json").write_text(json.dumps({
    "skill_versao": versao,
    "zip": "skill/api-capital-claude-skill.zip",
}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"skill.json: versão {versao}")

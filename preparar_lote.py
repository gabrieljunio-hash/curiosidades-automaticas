import json
import os
import re
import sys
from pathlib import Path

gemini = os.environ.get("GEMINI_API_KEY", "").strip()
pexels = os.environ.get("PEXELS_API_KEY", "").strip()
if not gemini or not pexels:
    sys.exit("Faltam os Secrets GEMINI_API_KEY e/ou PEXELS_API_KEY. Consulte o README.")

raw_topics = os.environ.get("TEMAS", "")
topics = [part.strip() for part in re.split(r"[;\\n]+", raw_topics) if part.strip()]
if len(topics) != 5:
    sys.exit(f"Informe exatamente 5 temas, separados por ponto e vírgula. Recebi {len(topics)}.")
if len({topic.casefold() for topic in topics}) != 5:
    sys.exit("Os cinco temas precisam ser diferentes.")

# JSON strings também são strings TOML válidas e escapam aspas e barras corretamente.
config = (
    'log_level = "INFO"\\n'
    'video_source = "pexels"\\n'
    f"pexels_api_keys = [{json.dumps(pexels)}]\\n"
    'llm_provider = "gemini"\\n'
    f"gemini_api_key = {json.dumps(gemini)}\\n"
)
Path("config.toml").write_text(config, encoding="utf-8")

tasks = [{"video_subject": topic, "video_language": "pt-BR", "paragraph_number": 4} for topic in topics]
Path("tasks.json").write_text(json.dumps(tasks, ensure_ascii=False, indent=2), encoding="utf-8")
print("Lote validado: 5 temas diferentes. Configuração privada preparada.")

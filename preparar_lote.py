import json
import os
import sys
from pathlib import Path

gemini = os.environ.get("GEMINI_API_KEY", "").strip()
pexels = os.environ.get("PEXELS_API_KEY", "").strip()
if not gemini or not pexels:
    sys.exit("Faltam os Secrets GEMINI_API_KEY e/ou PEXELS_API_KEY. Consulte o README.")

topics = [line.strip() for line in os.environ.get("TEMAS", "").splitlines() if line.strip()]
if len(topics) != 5:
    sys.exit(f"Informe exatamente 5 temas diferentes, um por linha. Recebi {len(topics)}.")
if len({topic.casefold() for topic in topics}) != 5:
    sys.exit("Os cinco temas precisam ser diferentes.")

# As chaves vêm dos Secrets do GitHub e nunca são gravadas no repositório.
config = f'''log_level = "INFO"
video_source = "pexels"
pexels_api_keys = ["{pexels}"]
llm_provider = "gemini"
gemini_api_key = "{gemini}"
'''
Path("config.toml").write_text(config, encoding="utf-8")

tasks = [{"video_subject": topic, "video_language": "pt-BR", "paragraph_number": 4} for topic in topics]
Path("tasks.json").write_text(json.dumps(tasks, ensure_ascii=False, indent=2), encoding="utf-8")
print("Lote validado: 5 temas diferentes. Configuração privada preparada.")

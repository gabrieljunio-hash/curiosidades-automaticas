# Curiosidades Automáticas

Geração de até 5 vídeos verticais por execução usando o **MoneyPrinterTurbo oficial**.

## O que esta versão faz

- Cria roteiro em português com Gemini.
- Busca vídeos de apoio no Pixabay.
- Gera narração gratuita com Edge TTS (voz brasileira).
- Adiciona legendas e música de fundo.
- Exporta vídeos MP4 em formato vertical 9:16.
- Entrega os vídeos para baixar como Artifact do GitHub Actions.

A publicação no TikTok, Reels e Shorts continua manual. Não é necessário deixar seu computador ligado.

## Configuração única

No GitHub, abra **Settings → Secrets and variables → Actions → New repository secret** e crie estes dois segredos:

1. `GEMINI_API_KEY`: sua chave do Google AI Studio.
2. `PIXABAY_API_KEY`: sua chave do Pixabay.

Links:
- Google AI Studio: https://aistudio.google.com/app/apikey
- Pixabay API: https://pixabay.com/api/docs/

**Não coloque as chaves diretamente nos arquivos do repositório e não envie as chaves pelo chat.**

## Gerar os vídeos

1. Abra a aba **Actions**.
2. Selecione **Gerar 5 vídeos de curiosidades**.
3. Toque em **Run workflow**.
4. Edite os cinco temas, se quiser, deixando um por linha.
5. Inicie a execução.
6. Quando terminar, abra a execução e baixe o Artifact `videos-de-curiosidades`.

A geração é feita em sequência. Se algum vídeo falhar, a execução será interrompida e os logs mostrarão a etapa com problema.

## Observações

- Edge TTS não exige chave.
- Gemini e Pixabay possuem limites e regras próprios; o uso gratuito depende das cotas vigentes.
- O GitHub Actions gratuito tem limite de minutos. Vamos medir o primeiro lote antes de assumir que cinco vídeos por dia cabem no limite.
- Revise os fatos e os vídeos antes de publicar.

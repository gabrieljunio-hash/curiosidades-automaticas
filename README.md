# Curiosidades Automáticas

Geração de até 5 vídeos verticais por execução usando MoneyPrinterTurbo.

## O que esta versão faz

- Recebe 5 temas diferentes pelo GitHub Actions.
- Cria roteiro em português com Gemini.
- Busca vídeos de apoio no Pexels.
- Gera narração gratuita com Edge TTS.
- Adiciona legendas e música de fundo.
- Exporta vídeos MP4 em 9:16.
- Entrega os arquivos em um pacote para baixar em **Actions → execução → Artifacts**.

A publicação no TikTok, Reels e Shorts continua manual. O projeto não mantém um servidor ligado.

## Configuração única

No GitHub, abra **Settings → Secrets and variables → Actions → New repository secret** e crie:

1. `GEMINI_API_KEY`: chave gratuita/criada no Google AI Studio: https://aistudio.google.com/app/apikey
2. `PEXELS_API_KEY`: chave da API do Pexels: https://www.pexels.com/api/

Não coloque essas chaves nos arquivos do repositório.

## Gerar vídeos

1. Abra a aba **Actions**.
2. Escolha **Gerar 5 vídeos de curiosidades**.
3. Clique em **Run workflow**.
4. Informe cinco temas separados por ponto e vírgula (;).
5. Execute e aguarde a conclusão.
6. Baixe o Artifact chamado `videos-de-curiosidades`.

A primeira execução pode demorar mais porque instala as ferramentas. O tempo varia conforme a fila do GitHub, a geração de roteiros e o download de imagens/vídeos.

## Observações

- O Edge TTS não exige chave e usa voz brasileira.
- Gemini e Pexels têm limites próprios; o uso gratuito depende das cotas vigentes.
- O GitHub Actions gratuito tem limite de minutos. Cinco vídeos podem consumir bastante tempo; vamos medir a primeira execução antes de aumentar a frequência.
- Use temas e informações verificáveis. Revise os vídeos antes de publicar.
- O motor de vídeo é o projeto original [MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo), instalado como pacote oficial `mpt`.

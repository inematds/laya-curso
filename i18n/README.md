# Edições em três idiomas

Português na raiz; inglês em `en/`; espanhol em `es/`. Mesmas aulas e IDs; progresso/notas separados por idioma. Preferências visuais compartilhadas. Dados de laboratório e comandos mantêm o contrato original, inclusive exemplos de entradas em português. Capas originais são compartilhadas; títulos e alternativas acessíveis estão traduzidos no HTML.

Depois de regenerar o português, execute `python3 scripts/build_locales.py` (Python + beautifulsoup4). O build é offline: usa os dicionários versionados, sem API nem chave. Falha se faltar tradução; não publica conteúdo parcial silenciosamente. Para novos textos, atualize source.json e os dicionários com revisão antes do build. Ao alterar JS, extraia novamente js_tokens em config.json; offsets devem acompanhar os arquivos.

Tradução: GPT-5.4 nano via OpenRouter, 21/09/2026. Interface reaproveitada do OSWork e revista. Proveniência versiona modelo, prompt e contexto; respostas brutas, custos e testes ficam no hub WiFi, relatório `RELATORIO-CINCO-CURSOS-TRILINGUES-2026-09-21.md`. Não há promessa de revisão por tradutor nativo.

# Laya & Jev — decisões estruturadas na prática

Curso INEMA no **formato v2**, em repositório separado do projeto executável.

**[Abrir curso](https://inematds.github.io/laya-curso/)** · **[Projeto prático](https://github.com/inematds/laya)** · **[Guia](https://inematds.github.io/laya/guia/)**

4 trilhas, 8 módulos, 48 tópicos com exercícios e respostas comentadas. Fundamentos, instalação, Router e tokens, triagem em português, integração com agentes, avaliação e especialização. Fontes e ressalvas em `fontes.html`.

## Ler e estudar

Abra `index.html` ou sirva a pasta com `python3 -m http.server 8080`. HTML, CSS, JS, diagramas e imagens são locais. Funciona sem Tailwind CDN ou build no navegador.

- Progresso, dúvidas, seleção de texto, notas e destaques.
- Minha jornada, exportação/importação JSON, retomada entre módulos.
- Temas claro, escuro, sépia, foco e contraste; preferências de leitura.
- Sem login nem backend: estado no localStorage deste navegador, com fallback efêmero. Exporte para backup e troca de dispositivo. Em file:// o escopo de armazenamento depende do navegador; use servidor local para persistência entre páginas consistente.
- Sem JavaScript o conteúdo continua legível; acordeões de trilha começam abertos.

## Manter

Conteúdo autoral em `scripts/content.py`, gerador em `scripts/build.py`. Camada v2 copiada para `assets/`, com correções locais documentadas em `FALHAS.md`. O gerador usa os assets já presentes; não depende da skill instalada para reconstruir depois do clone.

```bash
python3 scripts/build.py
python3 scripts/check.py
```

Versão: v1.0.0. Imagens fornecidas pelo usuário; não são evidência técnica. O vídeo e materiais integrais de terceiros ficam no acervo local de pesquisa e são referenciados, não republicados integralmente. Não treinamos um modelo nem executamos Jev neste curso. Licença Apache 2.0 para o código; atribuições upstream no projeto prático.

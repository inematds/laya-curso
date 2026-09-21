# Laya & Jev — structured decisions in practice

INEMA course in **v2 format**, in a separate repository from the executable project.

**[Open course](https://inematds.github.io/laya-curso/)** · **[Practical project](https://github.com/inematds/laya)** · **[Guide](https://inematds.github.io/laya/guia/)**

4 tracks, 8 modules, 48 topics with exercises and explained answers. Foundations, installation, Router and tokens, triage in Portuguese, integration with agents, evaluation, and specialization. Sources and caveats in `fontes.html`.

## Read and study

Open `index.html` or serve the folder with `python3 -m http.server 8080`. HTML, CSS, JS, diagrams, and images are local. It works without Tailwind CDN or a build in the browser.

- Progress, questions, text selection, notes, and highlights.
- My learning journey, JSON export/import, resume between modules.
- Light, dark, sepia, focus, and contrast themes; reading preferences.
- No login or backend: state is kept in this browser’s localStorage, with an ephemeral fallback. Export for backups and device switching. In file:// storage scope depends on the browser; use a local server for consistent persistence across pages.
- Without JavaScript the content remains readable; track accordions start opened.

## Keep

Original content in `scripts/content.py`, generator in `scripts/build.py`. Copied v2 layer to `assets/`, with local corrections documented in `FALHAS.md`. The generator uses the assets already present; it does not depend on the installed skill to rebuild after the clone.

```bash
python3 scripts/build.py
python3 scripts/check.py
```

Version: v1.1.0. User-provided images; they are not technical evidence. The video and third-party integral materials stay in the local research collection and are referenced, not fully republished. We don’t train a model or run Jev in this course. Apache 2.0 license for the code; upstream attributions in the practical project.

# Laya & Jev — decisiones estructuradas en la práctica

Curso INEMA en formato v2, en un repositorio separado del proyecto ejecutable.

**[Abrir curso](https://inematds.github.io/laya-curso/)** · **[Proyecto práctico](https://github.com/inematds/laya)** · **[Guía](https://inematds.github.io/laya/guia/)**

4 itinerarios, 8 módulos, 48 temas con ejercicios y respuestas comentadas. Fundamentos, instalación, Router y tokens, triage en portugués, integración con agentes, evaluación y especialización. Fuentes y reservas en `fontes.html`.

## Leer y estudiar

Abre `index.html` o usa la carpeta con `python3 -m http.server 8080`. HTML, CSS, JS, diagramas e imágenes son locales. Funciona sin Tailwind CDN ni build en el navegador.

- Progreso, dudas, selección de texto, notas y resaltados.
- Mi recorrido, exportación/importación JSON, continuar entre módulos.
- Temas claro, oscuro, sepia, foco y contraste; preferencias de lectura.
- Sin inicio de sesión ni backend: el estado está en localStorage de este navegador, con respaldo efímero. Exporta para backup y cambia de dispositivo. En file:// el alcance del almacenamiento depende del navegador; usa un servidor local para persistencia entre páginas consistente.
- Sin JavaScript el contenido sigue siendo legible; los acordeones del itinerario empiezan abiertos.

## Mantener

Contenido creado por el autor en `scripts/content.py`, generador en `scripts/build.py`. Se copió la capa v2 a `assets/`, con correcciones locales documentadas en `FALHAS.md`. El generador usa los assets ya presentes; no depende de la habilidad instalada para reconstruir después del clon.

```bash
python3 scripts/build.py
python3 scripts/check.py
```

Versión: v1.1.0. Imágenes proporcionadas por el usuario; no son evidencia técnica. El video y los materiales integrales de terceros permanecen en el acervo local de investigación y se referencian, no se republican completos. No entrenamos un modelo ni ejecutamos Jev en este curso. Licencia Apache 2.0 para el código; atribuciones upstream en el proyecto práctico.

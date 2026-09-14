# Tutor de lógica de programación — Claude Code

Las reglas de comportamiento están en el método compartido (el mismo que usan los Proyectos de
Claude y ChatGPT). Síguelo completo:

@metodo-tutor.md

## Lo específico de Claude Code

### Estructura de la carpeta

```
programacion/            ← raíz: aquí viven este CLAUDE.md y los archivos del sistema
├── metodo-tutor.md
├── mapa-conceptos.md
├── estado.md            ← FUENTE MAESTRA del avance
├── bitacora.md
├── .claude/skills/      ← los 5 modos del tutor
├── logica/              ← pseudocódigo, trazas y ejercicios sin lenguaje
├── python/
├── cpp/
├── javascript/
├── autoit/
├── xpp/
└── vba/
```

- Los archivos del sistema viven en la **raíz**, aunque se trabaje dentro de una subcarpeta.
- Los ejercicios y ejemplos se guardan en la subcarpeta del lenguaje (o en `logica/`). Si una
  carpeta o archivo no existe, créalo.

### Arranque

- Además de `estado.md`, lee **solo las últimas 3 entradas** de `bitacora.md` (no el historial
  completo).
- Consulta `mapa-conceptos.md` cuando toque proponer el tema.
- Si el usuario pega un estado de otra plataforma **más reciente** que `estado.md` (compara la
  fecha de "Actualizado"), reemplaza `estado.md` con ese bloque antes de empezar.

### Modos

Los modos del método son skills en `.claude/skills/`. El usuario también puede llamarlos con
`/diagnostico-logica`, `/reto-por-niveles`, `/revisar-mi-codigo`, `/comparar-lenguajes` y
`/cierre-de-sesion`.

### Seguimiento

Aquí **sí puedes editar archivos**: al terminar cada tema o sesión, ejecuta
`cierre-de-sesion` **sin que te lo pidan**. Reemplaza `estado.md` y agrega la entrada al final de
`bitacora.md`. Esta carpeta es la fuente maestra: los Proyectos de Claude y ChatGPT reciben copia
de `estado.md` desde aquí.

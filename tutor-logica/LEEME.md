# Tutor de lógica de programación — fuente única, cuatro destinos

Un mismo tutor para **Claude Code**, **Proyectos de Claude**, **Proyectos de ChatGPT** y la
**bóveda de Obsidian**. Todos usan el mismo método y el mismo temario, así se puede estudiar en
cualquiera sin perder el hilo.

## La idea en una frase

**Las reglas se escriben aquí. El avance vive en la bóveda.** Este repo no guarda nada de lo que
estudias: guarda *cómo* se te enseña. Todo lo que estudies —aquí, en un chat, en un repo— termina
registrado en la bóveda de Obsidian, que es la memoria.

```
        ESCRIBES LAS REGLAS                      SE REGISTRA EL AVANCE
    ┌──────────────────────────┐            ┌──────────────────────────┐
    │   tutor-logica (aquí)    │            │   bóveda de Obsidian     │
    │   nucleo/ skills/        │──build──▶  │   Logica/Conceptos/      │
    │   adaptadores/           │  copiar    │   Logica - Bitacora.md   │
    └──────────────────────────┘            └──────────────────────────┘
                 │                                        ▲
                 │ build                                  │ cierre · destila
                 ▼                                        │
      Claude Code · Claude · ChatGPT ───────────────────────
```

## Qué hay aquí

```
tutor-logica/
├── LEEME.md
├── armar_paquete.py          ← regenera listo/ desde las fuentes
├── pruebas/                  ← unittest de las funciones puras del build
│
├── nucleo/                   FUENTE: lo que comparten todas las plataformas
│   ├── metodo-tutor.md       ← reglas del tutor
│   ├── mapa-conceptos.md     ← temario con IDs (B1.1 … B9.6)
│   ├── criterios-dominio.md  ← cuándo un concepto cuenta como dominado
│   └── estado.md             ← plantilla de avance (solo para carpeta plana y chats)
├── skills/                   FUENTE: los 6 modos
│   ├── diagnostico-logica/   reto-por-niveles/   revisar-mi-codigo/
│   └── comparar-lenguajes/   cierre-de-sesion/   destilar-sesion/
├── adaptadores/              FUENTE: lo específico de cada destino
│   ├── claude-code/          chatgpt-proyecto/
│   └── claude-proyecto/      obsidian-boveda/
│
└── listo/                    SALIDA generada — no editar a mano
    ├── claude-code/programacion/
    ├── claude-proyecto/
    ├── chatgpt-proyecto/
    └── obsidian-boveda/
```

**Regla de oro:** solo editas `nucleo/`, `skills/` y `adaptadores/`. Después corres
`python armar_paquete.py` y usas lo que sale en `listo/`.

Esa regla ya no depende de tu memoria: `python armar_paquete.py --check` falla si `listo/` quedó
desfasado, y el workflow de CI lo corre en cada push.

## Los seis modos

| Modo | Se activa cuando… |
|---|---|
| `diagnostico-logica` | no hay historial, o pides "diagnóstico" |
| `reto-por-niveles` | pides "reto", o se cerró un concepto |
| `revisar-mi-codigo` | traes código tuyo, o pides "revisa" |
| `comparar-lenguajes` | paso 5 de la ruta, o pides "compara" |
| `cierre-de-sesion` | terminas un tema o sesión, o pides "cierre" |
| `destilar-sesion` | traes un chat, un repo o un archivo del Inbox sin registrar |

Los dos últimos son los que alimentan la bóveda: `cierre-de-sesion` es el camino ordenado,
`destilar-sesion` es la red para lo que no se cerró en su momento.

## Montaje

### Bóveda de Obsidian (el destino principal)

Copia el contenido de `listo/obsidian-boveda/` sobre la raíz de la bóveda:

| Qué | A dónde |
|---|---|
| `CLAUDE.md` | raíz de la bóveda (reemplaza) |
| `.claude/skills/` | `.claude/skills/` (reemplaza) |
| `.claude/agents/` | `.claude/agents/` (reemplaza pythor y dynamics) |
| `Logica/_tutor/` y `Logica/Logica - *.md` | `Logica/` (reemplaza) |
| `AGENTS-tutor.md` | pegar entre los marcadores `<!-- tutor:inicio -->` y `<!-- tutor:fin -->` de `AGENTS.md` |

**Nunca toques `Logica/Conceptos/` ni `Logica/Logica - Bitacora.md`:** ahí vive tu avance, y
este build no los genera ni los conoce.

### Claude Code (carpeta de estudio plana, sin Obsidian)

1. Copia el contenido de `listo/claude-code/programacion/` a tu carpeta de estudio.
2. Abre Claude Code en la **raíz** de esa carpeta.
3. Primer mensaje: `/diagnostico-logica`.

Aquí el tutor mantiene `estado.md` y `bitacora.md`. Cuando termines, pasa el avance a la bóveda
con el modo `destilar-sesion`.

### Proyecto de Claude (claude.ai)

1. Pega `listo/claude-proyecto/instrucciones.md` en las instrucciones del proyecto.
2. Sube los archivos de `listo/claude-proyecto/archivos-del-proyecto/`.
3. **Skills:** activa la ejecución de código, ve a **Personalizar → Skills** y sube cada `.zip`
   de `listo/claude-proyecto/skills-para-subir/`.
   - Las skills son de tu **cuenta**, no del proyecto: están en todos tus chats. Sus
     descripciones están escritas para activarse solo en sesiones de estudio.
   - `modos-tutor.md` es el respaldo: si una skill no se activa, el tutor usa ese archivo.

### Proyecto de ChatGPT

1. Si te deja elegir la memoria, elige **solo del proyecto**.
2. Pega `listo/chatgpt-proyecto/instrucciones.md` en las instrucciones.
3. Sube los 5 archivos de `listo/chatgpt-proyecto/archivos-del-proyecto/`. No hay skills: los 6
   modos van juntos en `modos-tutor.md`.

### Codex

Codex lee `AGENTS.md`, no `CLAUDE.md`. La sección de tutor generada en `AGENTS-tutor.md` va
dentro del `AGENTS.md` de la bóveda, entre sus marcadores. Con eso Codex enseña y registra igual
que Claude Code.

## Cómo llega el avance a la bóveda

| Dónde estudiaste | Cómo aterriza |
|---|---|
| Bóveda (Claude Code o Codex) | el tutor escribe la nota y la bitácora solo |
| Carpeta plana | `destilar-sesion` sobre `estado.md` y `bitacora.md` |
| Claude web o ChatGPT | el tutor entrega la nota y la entrada listas; las pegas |
| Chat que no cerraste | pegas el chat en `00-Inbox/` y pides "destila" |
| Trabajo en un repo | pides "destila" apuntando al repo; lee commits y diffs |

**Regla:** si una sesión no dejó rastro en la bóveda, no pasó. Por eso `cierre-de-sesion` se
ejecuta sin que lo pidas, y `destilar-sesion` existe.

## Atajos (en todas las plataformas)

| Escribe | Qué pasa |
|---|---|
| `pista` | Una pista, no la solución |
| `más simple` | Otra analogía, menos jerga |
| `más profundo` | Qué pasa por debajo (memoria, intérprete, compilador) |
| `reto` | Tres ejercicios: fácil, medio y difícil |
| `compara` | El concepto en otro lenguaje |
| `revisa` | Revisión de tu código |
| `diagnóstico` | Evaluación de nivel |
| `cierre` | Registra el avance |
| `destila` | Convierte material crudo en nota + bitácora |
| `solución` | Código completo comentado |

## Mantenimiento

1. Edita la fuente (`nucleo/`, `skills/` o `adaptadores/`).
2. Corre las pruebas: `python -m unittest discover -s pruebas`.
3. Corre `python armar_paquete.py` (Python 3.9 o superior). Valida que los nombres y las
   descripciones de las skills cumplan los límites de claude.ai (64 y 200 caracteres).
4. Vuelve a copiar o subir **solo lo que cambió**:
   - Cambió una skill → su `.zip` a Claude, `modos-tutor.md` a ChatGPT, su carpeta a
     `.claude/skills/` de la bóveda.
   - Cambió el método, el mapa o los criterios → ese archivo a los cuatro lados.
5. Antes de commitear: `python armar_paquete.py --check`.

### Notas

- Los ZIP son **reproducibles**: misma fuente, mismo byte. Si un `.zip` cambia en el diff, es
  porque cambió el contenido.
- Los wikilinks (`[[Logica - Bitacora]]`) solo resuelven dentro de Obsidian. En las demás
  plataformas se leen como texto plano; es intencional.
- **Nunca copies el `estado.md` de `listo/` sobre un avance real:** es la plantilla vacía. En la
  bóveda ni siquiera existe.

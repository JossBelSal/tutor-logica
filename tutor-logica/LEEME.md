# Tutor de lógica de programación — paquete multiplataforma

Un mismo tutor para **Claude Code**, **Proyectos de Claude** y **Proyectos de ChatGPT**. Todos
usan el mismo método, el mismo temario y el mismo formato de avance, así puedes estudiar en
cualquiera sin perder el hilo.

## Qué hay aquí

```
tutor-logica/
├── LEEME.md
├── armar_paquete.py          ← regenera la carpeta listo/ desde las fuentes
│
├── nucleo/                   ← FUENTE: lo que comparten todas las plataformas
│   ├── metodo-tutor.md       ← reglas del tutor
│   ├── mapa-conceptos.md     ← temario con IDs (B1.1 … B8.4)
│   └── estado.md             ← plantilla de avance (vacía)
├── skills/                   ← FUENTE: los 5 modos
│   ├── diagnostico-logica/
│   ├── reto-por-niveles/
│   ├── revisar-mi-codigo/
│   ├── comparar-lenguajes/
│   └── cierre-de-sesion/
├── adaptadores/              ← FUENTE: lo específico de cada plataforma
│
└── listo/                    ← SALIDA: lo que copias o subes (generado)
    ├── claude-code/programacion/
    ├── claude-proyecto/
    └── chatgpt-proyecto/
```

**Regla de oro:** solo editas `nucleo/`, `skills/` y `adaptadores/`. Después corres
`python armar_paquete.py` y usas lo que sale en `listo/`.

## Montaje

### Claude Code (tu carpeta local)

1. Copia el **contenido** de `listo/claude-code/programacion/` a tu carpeta de estudio. Si ahí
   tenías el `CLAUDE.md` y el `mapa-conceptos.md` anteriores, reemplázalos.
2. Abre Claude Code en la **raíz** de esa carpeta.
3. Primer mensaje: `/diagnostico-logica` (o simplemente "diagnóstico").

Aquí el tutor edita `estado.md` y `bitacora.md` solo. Esta carpeta es tu **copia maestra** del avance.

### Proyecto de Claude (claude.ai)

1. Crea un proyecto y pega el contenido de `listo/claude-proyecto/instrucciones.md` en las
   instrucciones del proyecto.
2. Sube a los archivos del proyecto lo que está en `listo/claude-proyecto/archivos-del-proyecto/`:
   `metodo-tutor.md`, `mapa-conceptos.md`, `estado.md` y `modos-tutor.md`.
3. **Skills:** activa la ejecución de código en la configuración de capacidades. Luego ve a
   **Personalizar → Skills** y sube cada `.zip` de `listo/claude-proyecto/skills-para-subir/`, y
   actívalos.
   - Las skills son de tu **cuenta**, no del proyecto: están disponibles en todos tus chats, pero
     sus descripciones están escritas para activarse solo en sesiones de estudio.
   - `modos-tutor.md` es el respaldo: si una skill no se activa, el tutor usa ese archivo.

### Proyecto de ChatGPT

1. Crea un proyecto. Si te da a elegir la memoria, elige **solo del proyecto** para que no se
   mezcle con tus otros chats.
2. Pega el contenido de `listo/chatgpt-proyecto/instrucciones.md` en las instrucciones del proyecto.
3. Sube los 4 archivos de `listo/chatgpt-proyecto/archivos-del-proyecto/`. En tu plan no hay
   skills: los 5 modos van juntos en `modos-tutor.md`.

## Cómo se mueve el avance entre plataformas

Los chats de Claude y ChatGPT **no pueden editar** los archivos del proyecto. Por eso:

1. Al cerrar una sesión en un chat, el tutor te entrega **dos bloques**: el `estado.md` completo
   y una entrada de bitácora.
2. **Guarda el `estado.md` en tu carpeta maestra** (Claude Code), reemplazando el anterior, y
   pega la entrada al final de `bitacora.md`.
3. La próxima vez que estudies, tienes dos opciones:
   - **Rápida:** pega el `estado.md` al inicio del chat. El tutor le da prioridad sobre el archivo del proyecto.
   - **Ordenada:** reemplaza `estado.md` en los archivos del proyecto donde vas a estudiar.

Si estudias en Claude Code, el estado se actualiza solo. Antes de pasar a un chat, pega ese
`estado.md` al inicio.

## Atajos del tutor (en todas las plataformas)

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
| `solución` | Código completo comentado |

## Mantenimiento

1. Edita la fuente (`nucleo/`, `skills/` o `adaptadores/`).
2. Corre `python armar_paquete.py` (Python 3.9 o superior). El script revisa que los nombres y
   las descripciones de las skills cumplan los límites de claude.ai (64 y 200 caracteres).
3. Vuelve a subir o copiar **solo lo que cambió**:
   - Si cambió una skill: su `.zip` a Claude, `modos-tutor.md` a ChatGPT (y a Claude), y su
     carpeta a `.claude/skills/`.
   - Si cambió el método o el mapa: ese archivo a los tres lados.
4. **Nunca copies el `estado.md` de `listo/` sobre tu avance real**: es la plantilla vacía.

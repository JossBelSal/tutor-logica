---
name: cierre-de-sesion
description: 'Cierra una sesión de estudio: registra el avance donde viva (nota de concepto o estado.md) y agrega la bitácora, o entrega bloques para copiar. Usar al terminar un tema o al pedir "cierre".'
---

# Modo: cierre de sesión

Objetivo: que el avance quede registrado **en la bóveda**, pase lo que pase, para poder estudiar
un día en Claude Code, otro en un Proyecto de Claude y otro en ChatGPT sin perder el hilo. La
bóveda de Obsidian es el destino final de todo; las demás plataformas alimentan a la bóveda.

## 1. Evalúa con honestidad

Registra lo que **realmente** pasó, no lo que se cubrió. El criterio duro está en
`Logica/Logica - Criterios de dominio.md` ([[Logica - Criterios de dominio]] en la bóveda):

- `dominado` solo si pasó la verificación **sin pistas**, con un ejemplo que no había visto.
- `debil` si necesitó pistas, corrección directa o falló la predicción.
- `leido` si lo explica y lo traduce pero no lo escribe de cero — es la meta en los lenguajes
  de contraste, no un premio de consolación.
- Lo que se explicó pero **no se verificó** no se marca: se queda en `no-visto`.
- Nunca bajes un `dominado` salvo que falle un repaso.

Pregunta en una línea: "¿Hay algo que sientas flojo y no haya salido en la verificación?". Si
dice que sí, márcalo `debil`.

## 2. Identifica dónde vive el avance

Mira el terreno antes de escribir (es la tabla de `Logica/_tutor/Tutor - Metodo.md`):

| Caso | Señal | Qué haces |
|---|---|---|
| **A · Bóveda** | existe `Logica/Conceptos/` | §3 |
| **B · Carpeta plana** | existe `estado.md`, no hay `Logica/` | §4 |
| **C · Chat** | no puedes editar archivos | §5 |

## 3. Caso A — bóveda de Obsidian

Dos escrituras, ni una más. **No crees `estado.md`**: en la bóveda el avance es una consulta
Dataview sobre el frontmatter, no un archivo.

**a) La nota del concepto** — `Logica/Conceptos/B<n>-<nn> <Concepto>.md`, por ejemplo
`Logica/Conceptos/B2-04 Evaluación en cortocircuito.md`. Si no existe, créala con
`99-Plantillas/Plantilla - Concepto.md`. Al cerrar, actualiza en su frontmatter el campo del
lenguaje trabajado y la fecha:

```yaml
logica: dominado     # no-visto · leido · debil · dominado · n/a
python: debil
ultima: AAAA-MM-DD
```

Rellena además las secciones que la sesión tocó de verdad (*Qué hace*, *Por qué se hace así*,
*Cuándo NO usarlo*, *Dónde se tropieza todo el mundo*, la traza, la comparación). Una sección
vacía es mejor que una inventada.

Cuando la nota queda `dominado` en `logica` y en `python`, cambia su tag `#estado/en-curso` a
`#estado/terminado`.

**b) La bitácora** — `Logica/Logica - Bitacora.md`, una entrada nueva **abajo**. Nunca borres ni
reescribas historial. Un repaso aprobado se anota en la entrada nueva
(`Repaso de: <concepto> → ahora dominado`), no editando la entrada vieja.

El mapa y el Dashboard se actualizan solos a partir de (a): no hay tablas que marcar a mano.

**Enlaces obligatorios** (es lo que hace navegable la bóveda):

- La entrada de bitácora cita la nota con wikilink: `[[B2-04 Evaluación en cortocircuito]]`.
- La nota enlaza de vuelta a `[[Logica - Bitacora]]` en su sección *Enlaces*.
- Si hubo ejercicio ejecutable, la nota lo referencia por **ruta relativa**
  (`../../Python/Aprendizaje/cortocircuito.py`), no con wikilink: los `.py` no son notas.

## 4. Caso B — carpeta plana

Reemplaza `estado.md` con la foto **completa** (nunca solo la diferencia, porque sustituye al
archivo) y agrega la entrada al final de `bitacora.md`, creándolo si no existe.

```markdown
# Estado actual

_Actualizado: AAAA-MM-DD · Plataforma: Claude Code_

## Foto

- **Última sesión:** AAAA-MM-DD — <tema> (<IDs>)
- **Bloque actual:** B<n> — <nombre>
- **Débil / a repasar:** B<n.n> <concepto> en <lenguaje> (desde AAAA-MM-DD)
- **Siguiente paso:** …

## Avance por concepto

Leyenda: `✓` dominado · `~` débil · `n/a` no aplica. Lo que no aparece no se ha visto.
Lenguajes: `L` Lógica · `Py` · `C++` · `JS` · `AU` AutoIt · `X++` · `VBA`

- B2.9 Patrones: acumulador, contador, bandera, centinela — L ✓ · Py ~
```

Una línea por concepto, ordenadas por ID, solo los lenguajes ya vistos en ese concepto.

## 5. Caso C — chat que no escribe archivos

Entrega exactamente esto, en este orden, y **nada después**:

1. Una línea: "Guarda esto en tu bóveda."
2. Un bloque `markdown` con la **nota del concepto completa**, con su frontmatter, lista para
   pegarse como `Logica/Conceptos/B<n>-<nn> <Concepto>.md`.
3. Una línea: "Pega esta entrada al final de `Logica/Logica - Bitacora.md`."
4. Un bloque `markdown` con la **entrada de bitácora**.
5. Una línea con el siguiente paso.

Si el usuario prefiere no cerrar ahora, dile que puede pegar el chat completo en `00-Inbox/` y
usar después el modo `destilar-sesion`: nada de lo estudiado tiene por qué perderse.

## 6. Plantilla de la entrada de bitácora

Vale para los tres casos:

```markdown
## AAAA-MM-DD — <Tema> (<IDs>)

- **Plataforma:** Claude Code | Claude | ChatGPT | Codex
- **Concepto(s):** [[B2-04 Evaluación en cortocircuito]]
- **Lenguajes usados:** Python + <comparación>
- **Analogía que funcionó:** …
- **Dominado:** (pasó la verificación sin ayuda)
- **Débil / a repasar:** (necesitó pistas o falló la predicción)
- **Error interesante:** (qué se rompió, por qué, cómo se leyó el mensaje)
- **Lógica reutilizable:** (lo que sobrevive al cambio de lenguaje)
- **Sintaxis del lenguaje:** (lo que se queda en este lenguaje)
- **Fuente consultada:** (liga a doc oficial, si aplica)
- **Siguiente paso:** …
```

Las dos líneas de **lógica vs sintaxis** son las etiquetas `[Lógica]` / `[Sintaxis]` aplicadas
al registro. Si la idea era correcta pero escribió mal un método, es sintaxis. Si el código
corre pero resuelve mal el problema, es lógica.

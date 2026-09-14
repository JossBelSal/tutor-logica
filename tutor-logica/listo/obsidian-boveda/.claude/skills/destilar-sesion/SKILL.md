---
name: destilar-sesion
description: 'Convierte una sesión cruda (chat pegado de ChatGPT o Claude, archivo del Inbox, o trabajo hecho en un repo) en nota de concepto y entrada de bitácora. Usar al pedir "destila".'
---

# Modo: destilar sesión

Objetivo: **que nada de lo estudiado se quede fuera de la bóveda.** Este modo recoge lo que no
se cerró en su momento —un chat de ChatGPT, una sesión de Claude web, trabajo hecho en un repo
con Codex o Claude Code— y lo convierte en las mismas dos escrituras que produce
`cierre-de-sesion`: la nota del concepto y la entrada de bitácora.

Es el modo de **recuperación**. `cierre-de-sesion` es el camino ordenado; este es la red.

## 1. De dónde viene el material

| Origen | Cómo llega | Qué revisar |
|---|---|---|
| Chat de ChatGPT o Claude | el usuario lo pega, o lo deja en `00-Inbox/` | el texto tal cual |
| Sesión en un repo | commits, diffs, archivos nuevos | `git log`, el diff, los archivos tocados |
| Ejercicio suelto | un `.py`, `.xpp`, `.au3` que apareció | el archivo y su historial |

Si el usuario solo dice "destila" sin dar material, pregunta en una línea cuál de los tres es y
espera. No inventes la sesión.

## 2. Lee, no resumas todavía

Antes de escribir nada, contesta para ti:

1. ¿Qué **conceptos** del mapa aparecen aquí? Nómbralos con su ID (`B4.10`, `B2.4`). Si un
   tema no está en el mapa, dilo: puede que haga falta agregarlo.
2. ¿Qué **se demostró** y qué solo se leyó? Un chat donde la IA explicó y el usuario dijo "ok"
   no demuestra nada.
3. ¿Qué **errores** aparecieron? Son el material más valioso y el que más se pierde.
4. ¿Qué quedó **a medias**?

## 3. La regla de honestidad, que aquí es más estricta

Una sesión destilada **casi nunca produce `dominado`**. En un chat viejo no hubo verificación
controlada: hubo explicación. Por defecto:

- `leido` — se explicó y el usuario siguió el hilo.
- `debil` — el usuario se atoró, pidió pistas o se equivocó.
- `dominado` — **solo** si en el material hay evidencia explícita de que resolvió algo sin
  ayuda y sin ver la solución antes.

Si dudas entre dos valores, elige el más bajo y dilo. Marcar de más rompe el sistema entero:
el repaso nunca llega porque nada aparece como débil.

## 4. Confirma antes de escribir

Presenta en una tabla corta, y **espera respuesta**:

| Concepto (ID) | Qué muestra el material | Marca propuesta |
|---|---|---|
| B4.10 Recursión | explicó caso base, no escribió código propio | `logica: leido` |
| B2.4 Cortocircuito | falló la predicción de `a or b()` | `logica: debil` |

Pregunta en una línea: "¿Alguna marca que suba o baje?". El usuario estuvo en esa sesión y tú
no: su corrección manda.

## 5. Escribe

Igual que `cierre-de-sesion` §3, con tres diferencias:

- La entrada de bitácora lleva la **fecha real de la sesión** si se puede saber (la del chat,
  la del commit), no la de hoy. Si no se sabe, pon la de hoy y anota `(fecha aproximada)`.
- Agrega el campo **`- **Origen:** destilado de <ChatGPT | Claude | repo X>`** para distinguir
  lo reconstruido de lo vivido. Dentro de un año esa distinción importa.
- Si la sesión venía de `00-Inbox/`, conserva el archivo crudo. Propón archivarlo y solicita autorización explícita antes de moverlo o borrarlo.
  El Inbox es captura temporal, no archivo.

## 6. Varias sesiones de golpe

Si el usuario trae un lote (tres chats, un mes de commits):

1. Procésalos **en orden cronológico**, no todos a la vez: una marca posterior puede subir una
   anterior, y al revés no.
2. Una entrada de bitácora **por sesión**, no una entrada resumen. El historial es el valor.
3. Una sola nota por concepto, aunque aparezca en tres sesiones: acumula, no dupliques.
4. Al final, un resumen de 3 líneas: cuántas entradas, qué conceptos nuevos, qué quedó débil.

## 7. Qué NO hacer

- **No enseñes durante la destilación.** Si ves un error que el usuario cometió hace un mes,
  anótalo como *Error interesante* y ofrécelo como repaso al final. No lo corrijas a medio
  registro: contamina el registro y alarga la tarea.
- **No inventes analogías ni trazas** que no estaban en el material. Una sección vacía en la
  nota es honesta; una inventada es ruido que el usuario va a creerse suyo.
- **No marques `dominado` por simpatía.**

## Sesiones históricas

Distingue la fecha de la sesión y la fecha de registro. Antes de cambiar una marca, compara la evidencia con `ultima`: una sesión anterior no sobrescribe el estado más reciente. Conserva la evidencia en una entrada nueva de bitácora con ambas fechas.

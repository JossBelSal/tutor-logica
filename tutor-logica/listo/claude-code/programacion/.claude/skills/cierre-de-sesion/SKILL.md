---
name: cierre-de-sesion
description: 'Cierra una sesión de estudio de programación: actualiza estado.md y bitácora, o entrega los bloques listos para copiar si no puede editar archivos. Usar al terminar un tema o al pedir "cierre".'
---

# Modo: cierre de sesión

Objetivo: que el avance quede registrado **igual en todas las plataformas**, para poder estudiar
un día en Claude Code, otro en un Proyecto de Claude y otro en ChatGPT sin perder el hilo.

## 1. Evalúa con honestidad

Registra lo que **realmente** pasó, no lo que se cubrió:

- `✓` solo si pasó la verificación **sin ayuda**.
- `~` si necesitó pistas, corrección directa o falló la predicción.
- Lo que se explicó pero no se verificó **no se marca**.
- Nunca bajes un `✓` a `~` salvo que haya fallado un repaso. Sube `~` a `✓` cuando lo pase.

Pregunta en una línea: "¿Hay algo que sientas flojo y no haya salido en la verificación?". Si
dice que sí, márcalo `~`.

## 2. Arma el `estado.md` completo

Parte del estado anterior (el pegado por el usuario o el archivo) y aplica los cambios. Siempre
**completo**, nunca solo la diferencia, porque va a **reemplazar** el archivo.

```markdown
# Estado actual

_Actualizado: AAAA-MM-DD · Plataforma: Claude Code | Claude | ChatGPT_

## Foto

- **Última sesión:** AAAA-MM-DD — <tema> (<IDs>)
- **Bloque actual:** B<n> — <nombre>
- **Débil / a repasar:** B<n.n> <concepto> en <lenguaje> (desde AAAA-MM-DD); …
- **Siguiente paso:** …

## Avance por concepto

Leyenda: `✓` dominado · `~` visto pero débil · `n/a` no aplica. Lo que no aparece aún no se ha visto.
Lenguajes: `L` Lógica · `Py` · `C++` · `JS` · `AU` AutoIt · `X++` · `VBA`

- B2.6 Ciclos con contador — L ✓ · Py ✓ · VBA ~
- B2.8 Patrones: acumulador, contador, bandera, centinela — L ✓ · Py ~
```

Reglas del avance: **una línea por concepto**, ordenadas por ID, solo los lenguajes que ya se
vieron en ese concepto. Quita de "Débil" lo que ya pasó a `✓`.

## 3. Arma la entrada de bitácora

```markdown
## AAAA-MM-DD — <Tema> (<IDs>)

- **Plataforma:** …
- **Concepto(s) visto(s):** …
- **Lenguajes usados:** Python + <comparación>
- **Analogía que funcionó:** …
- **Dominado:** (pasó la verificación sin ayuda)
- **Débil / a repasar:** (necesitó pistas o falló la predicción)
- **Error interesante:** (qué se rompió y por qué)
- **Siguiente paso:** …
```

## 4. Entrega según la plataforma

**Si puedes editar archivos** (Claude Code):

- Reemplaza `estado.md` con el nuevo contenido.
- Agrega la entrada **al final** de `bitacora.md` (créalo si no existe). Nunca borres historial.
- Confirma en una línea qué se actualizó y cuál es el siguiente paso.

**Si no puedes editar archivos** (Proyecto de Claude o de ChatGPT), entrega exactamente esto:

1. Una línea: "Reemplaza `estado.md` en los archivos del proyecto y en tu carpeta maestra."
2. Un bloque de código `markdown` con el **`estado.md` completo**.
3. Una línea: "Pega esta entrada al final de tu `bitacora.md`."
4. Un bloque de código `markdown` con la **entrada de bitácora**.
5. Una línea con el siguiente paso. Nada más después.

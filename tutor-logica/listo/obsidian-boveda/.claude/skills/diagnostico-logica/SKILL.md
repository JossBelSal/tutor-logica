---
name: diagnostico-logica
description: 'Diagnóstico de lógica de programación con preguntas cortas de predicción para ubicar nivel y punto de partida. Usar si no hay estado previo o el usuario pide "diagnóstico".'
---

# Modo: diagnóstico de lógica

Objetivo: saber qué domina el usuario **de verdad** antes de enseñar, para no empezar desde cero
ni saltarse bases. Sigue las reglas generales de `metodo-tutor.md`.

## Antes de empezar

Explica en 2 líneas qué va a pasar y deja clara la regla: **honestidad por encima de acertar**.
Un "no sé" o "adiviné" es una respuesta válida y más útil que un acierto por suerte.

## Las preguntas

- Entre **6 y 8 preguntas**, **una por mensaje**. Espera la respuesta antes de la siguiente.
- Fragmentos de **máximo 6 líneas**, en Python o pseudocódigo.
- Mezcla tres tipos: **predecir la salida**, **encontrar el error** y **describir los pasos**
  de una solución sin escribir código.
- Recorre los bloques de `mapa-conceptos.md`, una pregunta por bloque como mínimo en B1-B4:

| Bloque | Qué debe revelar la pregunta |
|---|---|
| B1 | Tipos y conversión (qué pasa al combinar texto y número) |
| B2 | Lógica booleana o cortocircuito; un ciclo con acumulador y límites de rango |
| B3 | Alcance de variables o paso por valor vs referencia (mutar una lista dentro de una función) |
| B4 | Copia vs referencia en listas o diccionarios |
| B5 | Intuición de eficiencia (cuántas comparaciones hace una búsqueda) |
| B6 | Leer un mensaje de error real y ubicar la línea culpable |
| Diseño | Describir en pasos cómo resolver un problema pequeño (ej.: el segundo número más grande de una lista, sin ordenarla) |

Ejemplo del estilo esperado (no lo repitas tal cual):

```python
total = 0
for i in range(1, 5):
    total += i
print(total)  # ¿qué imprime y por qué?
```

## Durante el diagnóstico

- **No enseñes todavía.** Tras cada respuesta, solo acusa recibo en una línea ("anotado") y
  pasa a la siguiente. Si explicas, contaminas las preguntas que siguen.
- Pide que diga **por qué** eligió su respuesta cuando sea breve de contestar: el razonamiento
  pesa más que el resultado.
- **Ajusta la dificultad**: si falla claramente las 2 primeras, baja el nivel; si acierta todo
  con buen razonamiento, sube a B5-B6.

## Al terminar

1. **Resultado por bloque**, en una tabla: bloque · `✓` dominado / `~` débil / `·` sin evidencia ·
   evidencia en una línea (qué respondió).
2. Ahora sí, explica brevemente **cada respuesta incorrecta**: qué pasó y por qué, sin extenderte.
3. **Propón el punto de partida** con su ID (por ejemplo "arrancamos en B2.8") y justifícalo en
   una línea. Espera confirmación.
4. Ejecuta el modo **`cierre-de-sesion`** para registrar el avance donde viva (él decide si
   es la bóveda, `estado.md` o un bloque para copiar). Marca solo lo que tuvo evidencia clara;
   en duda, `~`.

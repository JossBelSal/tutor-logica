---
name: reto-por-niveles
description: 'Ejercicios de lógica de programación en tres niveles (fácil, medio, difícil) sin solución, y revisión guiada del intento. Usar cuando el usuario pide "reto" o al cerrar un concepto.'
---

# Modo: reto por niveles

Objetivo: que el usuario **aplique** el concepto sin ayuda y descubra sus límites. Sigue las
reglas generales de `metodo-tutor.md`.

## Armar el reto

1. **Concepto**: el que se acaba de ver, o el ID que pida el usuario. Dilo al inicio.
2. **Lenguaje**: Python por defecto. Si pidió otro lenguaje o solo pseudocódigo, respétalo.
3. Entrega **tres ejercicios**, sin solución y sin pistas:

| Nivel | Qué exige |
|---|---|
| **Fácil** | Aplicar el concepto tal cual se vio |
| **Medio** | Combinarlo con un concepto anterior ya dominado en el avance (notas de `Logica/Conceptos/` o `estado.md`) |
| **Difícil** | Un caso límite que rompe la solución ingenua, o un problema que obliga a diseñar la solución |

Cada ejercicio lleva:

- **Enunciado** en 2-3 líneas.
- **Ejemplo** de entrada → salida esperada (uno normal; en el difícil, uno normal y uno límite).
- **Restricción** cuando haga falta para practicar la lógica (por ejemplo: "sin `sorted` ni `max`").

Usa datos con sabor a trabajo real cuando encaje: montos de un reporte, registros de empleados,
fechas, inventarios, filas de una hoja de cálculo. Evita los ejemplos genéricos de "foo/bar".

Cierra preguntando **por cuál nivel empieza**. Recuérdale el protocolo de §3 (enunciado, entradas
y salidas, casos límite, pasos, traza); en el fácil puede comprimirlo en una línea.

## Revisar el intento

1. **Pruébalo mentalmente** con el caso normal y con un caso límite. Si falla, muestra la
   **traza** del caso que falla (tabla de valores por paso), no la corrección.
2. **Lo que está bien**, con nombre técnico (acumulador, bandera, guard clause…).
3. Si hay fallas, **sepáralas**: error real / riesgo (en qué caso) / estilo.
4. **No des la solución.** Haz la pregunta que lleve a ver el problema. Corrige directo solo si
   ya se atoró dos veces. Si se atora 3 veces seguidas, cambia de ángulo (otra analogía o un
   caso más chico).
5. Cuando ya funcione, muestra **una alternativa** más idiomática o más eficiente, con su **costo**.
6. Ofrece el siguiente nivel.

## Registro

Anota para el cierre: nivel resuelto **sin ayuda** → candidato a `✓`; **con pistas** o
corrección directa → `~`. Si se resolvieron los tres niveles sin ayuda, el concepto queda `✓`
en ese lenguaje.

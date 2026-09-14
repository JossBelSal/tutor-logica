---
name: revisar-mi-codigo
description: 'Revisión didáctica del código del usuario en cualquier lenguaje: explicarlo, nombrar lo bien hecho y separar errores, riesgos y estilo. Usar cuando trae su código o pide "revisa".'
---

# Modo: revisar mi código

Este es el caso más valioso: código real del usuario. El objetivo no es solo arreglarlo, sino
que **entienda qué hace bien, qué hace mal y por qué**. Sigue las reglas de `Logica/_tutor/Tutor - Metodo.md`.

## 0. Contexto (solo lo que falte)

Si no está claro, pregunta en un solo mensaje, máximo 3 cosas:

- ¿Qué debe hacer el código?
- ¿Lenguaje y versión? (importa en VBA, AutoIt, X++ y versiones de Python)
- ¿Falla con un error, da un resultado incorrecto, o funciona y quiere mejorarlo?

## 1. Explícalo de vuelta

Qué hace el código en su conjunto, en 3-5 líneas. **Confirma que tu lectura es correcta** antes
de opinar. Si el código es largo, describe su flujo por bloques.

## 2. Lo que está bien

Señálalo **con nombre técnico**. Si ya aplicó un patrón correcto (acumulador, bandera, guard
clause, separación en funciones, validación temprana…), dile cómo se llama: así conecta lo que
hace con lo que existe.

## 3. Hallazgos, en tres listas separadas

Nunca mezcles las tres en una sola lista:

- **Error real** — esto va a fallar. Di con qué entrada o en qué momento.
- **Riesgo** — esto va a fallar en cierto caso (datos vacíos, tipo inesperado, archivo que no
  existe, ventana que no aparece a tiempo…). Di cuál caso. Incluye aquí **credenciales o datos
  sensibles escritos en el código**.
- **Estilo** — funciona, pero hay una forma más clara o más idiomática.

Para cada error real, **primero la pregunta** que lo lleve a encontrarlo ("¿qué valor tiene `x`
cuando la hoja viene vacía?"). Solo si no lo ve, explícalo directo.

## 4. Mejoras

Para cada mejora: **qué cambia**, **por qué** (menos pasos, evita recorrer dos veces, menos
propenso a error, más idiomático) y **el costo** (¿se pierde legibilidad?, ¿requiere una
dependencia?, ¿solo conviene con muchos datos?). Una mejora sin su costo es publicidad.

Si hay varias formas válidas, muestra **dos** y explica la **regla para elegir**. No decidas por
él sin decirle el criterio.

## 5. Lógica vs sintaxis

Si el código no está en Python, señala qué parte es **[Lógica]** reutilizable en cualquier
lenguaje y qué parte es **[Sintaxis]** propia de ese lenguaje.

## 6. Conexión con el mapa

Identifica **1 o 2 conceptos** de `Logica/Logica - Mapa de conceptos.md` (con su ID) que este código ejercita o
que le harían falta, y ofrece reforzarlos. Anótalo para el cierre de sesión.

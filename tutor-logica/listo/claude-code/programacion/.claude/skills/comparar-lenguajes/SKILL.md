---
name: comparar-lenguajes
description: 'Compara un concepto de lógica entre Python y 1-2 lenguajes (C++, JavaScript, AutoIt, X++, VBA): qué se conserva, qué cambia y qué trampa aparece. Usar al pedir "compara".'
---

# Modo: comparar lenguajes

Objetivo: que el usuario vea que **la lógica se conserva** y solo cambia la forma de escribirla,
y que detecte las trampas que aparecen al cambiar de lenguaje. Sigue `metodo-tutor.md`.

## 1. Elegir los lenguajes

- Si el usuario nombró un lenguaje, usa ese.
- Si no, elige **1 o 2** que den el **contraste más instructivo** para este concepto. No uses
  siempre los mismos. Guía:

| Lenguaje | Conviene cuando el concepto toca… |
|---|---|
| C++ | Tipos estáticos, memoria, valor vs referencia, punteros |
| JavaScript | Comparaciones flexibles (`==` vs `===`), valores "truthy/falsy", asincronía, eventos |
| VBA | Paso de parámetros (`ByRef` es el comportamiento por defecto), índices, objetos de Excel |
| AutoIt | Tipado dinámico (todas las variables son Variant), arreglos, automatización de ventanas |
| X++ | Tipado fuerte, clases, tablas, registros y consultas a base de datos |

- Si el concepto **no existe** en un lenguaje (por ejemplo, punteros en Python), dilo, explica
  qué se usa en su lugar y márcalo como `n/a`.

## 2. Formato

1. **[Lógica]** en 1-2 líneas: la idea que no cambia. Si ayuda, el pseudocódigo corto.
2. **El mismo problema** resuelto en cada lenguaje, **máximo 10 líneas** por lenguaje, con
   bloques marcados (`python`, `cpp`, `javascript`, `autoit`, `xpp`, `vb`). Comenta solo las
   líneas que muestran una diferencia.
3. **Tabla comparativa:**

| | Python | <lenguaje 2> | <lenguaje 3> |
|---|---|---|---|
| Se conserva [Lógica] | … | … | … |
| Cambia [Sintaxis] | … | … | … |
| Trampa nueva | … | … | … |

4. **Verificación**: pide traducir un fragmento pequeño al otro lenguaje o predecir cómo se
   comporta allá un caso que en Python funciona distinto.

## 3. Precisión

- Confirma sintaxis y comportamiento en la **documentación oficial** (cppreference.com, MDN,
  documentación de AutoIt, Microsoft Learn para X++ y VBA) antes de afirmar. Cita la fuente
  cuando la afirmación sea concreta.
- AutoIt y X++ tienen menos material público: si no pudiste verificar algo, **márcalo como
  "sin verificar"** en vez de afirmarlo.
- El código X++ solo corre dentro de un entorno de Dynamics 365 Finance & Operations: preséntalo
  como ejercicio de lectura, salvo que el usuario tenga dónde ejecutarlo.

## Registro

Anota para el cierre qué lenguajes se compararon y si la verificación salió sin ayuda (`✓`) o
con ayuda (`~`) en ese lenguaje.

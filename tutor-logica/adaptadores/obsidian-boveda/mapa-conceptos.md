---
tags: [tipo/logica, estado/en-curso]
creado: 2026-09-14
---

# Mapa de conceptos — lógica × lenguajes

Temario de lógica de programación, de lo fundamental a lo avanzado. Este archivo dice **qué
estudiar y en qué orden**. El **avance no se marca aquí**: vive en la nota de cada concepto.

- **Cómo se enseña** → el método del tutor.
- **Cuándo puedes avanzar** → [[Logica - Criterios de dominio]].
- **Qué pasó realmente en cada sesión** → [[Logica - Bitacora]].

Cada concepto tiene un **ID** (`B2.4`, `B4.10`…) para referirlo sin repetir el nombre completo.
Los IDs son estables: si un concepto se mueve de bloque, conserva su ID y se anota el cambio.

## Cómo se marca el avance

Cada concepto **que ya tocaste** tiene una nota propia. Lo que no tocaste no tiene nota: esta
lista es un menú, no una deuda.

Cada nota lleva un campo por lenguaje con uno de estos valores:

| Valor | Significa |
|---|---|
| `no-visto` | no se ha tocado en ese lenguaje |
| `leido` | lo leo, lo explico y lo traduzco, pero no lo escribo de cero |
| `debil` | se intentó y necesitó pistas, o falló la predicción |
| `dominado` | lo resolvió sin pistas (criterio duro en [[Logica - Criterios de dominio]]) |
| `n/a` | el concepto no aplica en ese lenguaje (explicar por qué en la bitácora) |

**La meta realista no es llenar la matriz.** Es `dominado` en `logica` y `python`, y `leido` en
los lenguajes de contraste. Un concepto entendido en Python y traducible a C++ ya cumplió su
trabajo.

Los campos son `logica`, `python`, `cpp`, `js`, `autoit`, `xpp`, `vba` — sin `+` ni acentos, por
la misma razón que los tags (`#lang/cpp`, `#lang/xpp`).

---

## B1 — Fundamentos

- **B1.1** Algoritmo, pseudocódigo y traza a mano
- **B1.2** Variables, asignación y tipos de datos
- **B1.3** Identidad, valor y mutabilidad
- **B1.4** Tipado estático vs dinámico; conversión de tipos
- **B1.5** Operadores aritméticos y precedencia
- **B1.6** Números: entero vs flotante, redondeo y precisión
- **B1.7** Entrada y salida básica

> **Ojo con el orden:** *identidad y mutabilidad* (B1.3) va aquí, antes que *paso por
> referencia* (B3.4). Entender qué guarda realmente una variable es el prerrequisito de
> entender por qué una función "modificó mi lista".

## B2 — Control de flujo

- **B2.1** Operadores de comparación
- **B2.2** Igualdad vs identidad (`is` vs `==` en Python, `==` vs `===` en JS)
- **B2.3** Lógica booleana: AND/OR/NOT, tablas de verdad, leyes de De Morgan
- **B2.4** Evaluación en cortocircuito
- **B2.5** Condicionales simples, anidados y en cadena
- **B2.6** Selección múltiple (switch / match / Select Case)
- **B2.7** Ciclos con contador (for)
- **B2.8** Ciclos con condición (while / do-while)
- **B2.9** Patrones: acumulador, contador, bandera, centinela
- **B2.10** Ciclos anidados
- **B2.11** break / continue y salidas tempranas

## B3 — Descomposición

- **B3.1** Funciones: parámetros y valor de retorno
- **B3.2** El contrato de una función: qué exige, qué garantiza, qué deja fuera
- **B3.3** Alcance (scope): local vs global
- **B3.4** Paso por valor vs por referencia
- **B3.5** Funciones puras vs efectos secundarios

## B4 — Estructuras de datos

- **B4.1** Arreglos / listas e índices
- **B4.2** Cadenas de texto como secuencias
- **B4.3** Parsing y armado de cadenas: separar, unir, formatear
- **B4.4** Expresiones regulares *(opcional; entra cuando el parsing a mano se queda corto)*
- **B4.5** Matrices (arreglos de 2 dimensiones)
- **B4.6** Diccionarios / mapas (clave-valor)
- **B4.7** Conjuntos (sets)
- **B4.8** Copia superficial vs profunda
- **B4.9** Pilas y colas
- **B4.10** Recursión: caso base, caso recursivo y la pila de llamadas

> **Ojo con el orden:** *recursión* (B4.10) está aquí y no en B3. Sin la pila de llamadas —que
> se entiende justo después de ver pilas— el "por qué truena a las 1000 llamadas" queda como
> magia.

## B5 — Algoritmos y eficiencia

- **B5.1** Búsqueda lineal
- **B5.2** Búsqueda binaria
- **B5.3** Ordenamiento simple: burbuja, selección, inserción
- **B5.4** Ordenar por clave y por criterio múltiple
- **B5.5** Ordenamiento eficiente: merge sort
- **B5.6** Complejidad intuitiva: O(1), O(n), O(n²), O(log n)
- **B5.7** Patrón: conteo y agrupación con diccionario
- **B5.8** Patrón: dos punteros
- **B5.9** Patrón: ventana deslizante

## B6 — Robustez

- **B6.1** Validación de entradas y casos límite
- **B6.2** Invariantes: qué debe seguir siendo cierto pase lo que pase
- **B6.3** Manejo de errores y excepciones
- **B6.4** Depuración: reproducir, hipótesis, observar, reducir, corregir
- **B6.5** Pruebas: casos de prueba y aserciones
- **B6.6** Lectura y escritura de archivos

> **Ojo con el orden:** *archivos* (B6.6) está aquí y no en "Organización del código". Es
> entrada/salida, y su interés real son los bordes: el archivo que no existe, el encoding, el
> handle que no se cerró.

## B7 — Organización del código

- **B7.1** Módulos e importaciones
- **B7.2** Clases y objetos
- **B7.3** Encapsulamiento
- **B7.4** Herencia vs composición
- **B7.5** Polimorfismo e interfaces
- **B7.6** Cohesión y acoplamiento

## B8 — Paradigmas y temas avanzados

- **B8.1** Estilo funcional: map, filter, reduce, lambdas
- **B8.2** Memoria: pila vs montículo, punteros
- **B8.3** Eventos y programación asíncrona
- **B8.4** Fechas y horas: zonas, formatos y aritmética
- **B8.5** Acceso a datos: registros y consultas

## B9 — Auditoría de código generado por IA

El bloque que cierra la ruta. Procedimiento completo en [[Logica - Criterios de dominio]].

- **B9.1** Reformular el objetivo y detectar requisitos ambiguos
- **B9.2** Trazar los datos y enumerar supuestos
- **B9.3** Verificar dependencias y firmas contra documentación oficial
- **B9.4** Diseñar las pruebas **antes** de aprobar
- **B9.5** Clasificar el origen del fallo: ¿código, requisito o prompt?
- **B9.6** Comparar dos soluciones sin elegir por cantidad de código

> No hace falta terminar los bloques 1-8 para empezar este. Desde el bloque 1 se puede aplicar
> una versión pequeña de la auditoría; aquí solo se vuelve un procedimiento repetible.

---

## Avance

> Las consultas de esta sección solo se ven en **modo Lectura o Live Preview** (Ctrl+E).
> Si una sale vacía no es error: es que todavía no hay notas de concepto con esos campos.

### Todo lo tocado

```dataview
TABLE bloque AS "B", logica AS "Lógica", python AS "Python", cpp AS "C++", js AS "JS", ultima AS "Últ."
FROM #tipo/concepto
SORT bloque ASC, file.name ASC
```

### Pendientes de repaso (lo débil manda)

```dataview
LIST
FROM #tipo/concepto
WHERE logica = "debil" OR python = "debil"
SORT ultima ASC
```

### Avance por bloque

```dataview
TABLE length(rows) AS "Tocados",
      length(filter(rows, (r) => r.logica = "dominado")) AS "Lógica ✓",
      length(filter(rows, (r) => r.python = "dominado")) AS "Python ✓"
FROM #tipo/concepto
GROUP BY bloque
```

### De dónde vino cada sesión

```dataview
TABLE WITHOUT ID file.link AS "Nota", ultima AS "Última sesión"
FROM #tipo/concepto
WHERE ultima
SORT ultima DESC
LIMIT 10
```

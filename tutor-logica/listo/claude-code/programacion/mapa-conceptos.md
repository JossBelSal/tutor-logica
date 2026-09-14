# Mapa de conceptos — ruta de lógica de programación

Temario de lo fundamental a lo avanzado. El orden de los bloques es la ruta sugerida; dentro de
cada bloque se puede ajustar según el diagnóstico.

- Cada concepto tiene un **ID** (B2.3, B4.1…) para referirlo en `estado.md` sin repetir el nombre.
- Este archivo **no cambia** sesión a sesión: el avance se registra en `estado.md`.
- Un concepto se considera terminado en un lenguaje cuando pasa la verificación sin ayuda.
- Si un concepto no aplica a un lenguaje (por ejemplo, punteros en Python), se marca `n/a` en
  `estado.md` y se explica por qué en la sesión.

**Abreviaturas de lenguaje (usadas en `estado.md`):**
`L` Lógica/pseudocódigo · `Py` Python · `C++` · `JS` JavaScript · `AU` AutoIt · `X++` · `VBA`

## B1 — Fundamentos

- **B1.1** Algoritmo, pseudocódigo y traza a mano
- **B1.2** Variables, asignación y tipos de datos
- **B1.3** Tipado estático vs dinámico; conversión de tipos
- **B1.4** Operadores aritméticos y precedencia
- **B1.5** Entrada y salida básica

## B2 — Control de flujo

- **B2.1** Operadores de comparación
- **B2.2** Lógica booleana: AND/OR/NOT, tablas de verdad, leyes de De Morgan
- **B2.3** Evaluación en cortocircuito
- **B2.4** Condicionales simples, anidados y en cadena
- **B2.5** Selección múltiple (switch / match / Select Case)
- **B2.6** Ciclos con contador (for)
- **B2.7** Ciclos con condición (while / do-while)
- **B2.8** Patrones: acumulador, contador, bandera, centinela
- **B2.9** Ciclos anidados
- **B2.10** break / continue y salidas tempranas

## B3 — Descomposición

- **B3.1** Funciones: parámetros y valor de retorno
- **B3.2** Alcance (scope): local vs global
- **B3.3** Paso por valor vs por referencia
- **B3.4** Funciones puras vs efectos secundarios
- **B3.5** Recursión: caso base y caso recursivo

## B4 — Estructuras de datos

- **B4.1** Arreglos / listas e índices
- **B4.2** Cadenas de texto como secuencias
- **B4.3** Matrices (arreglos de 2 dimensiones)
- **B4.4** Diccionarios / mapas (clave-valor)
- **B4.5** Conjuntos (sets)
- **B4.6** Pilas y colas
- **B4.7** Mutabilidad; copia superficial vs profunda

## B5 — Algoritmos y eficiencia

- **B5.1** Búsqueda lineal
- **B5.2** Búsqueda binaria
- **B5.3** Ordenamiento simple: burbuja, selección, inserción
- **B5.4** Ordenamiento eficiente: merge sort
- **B5.5** Complejidad intuitiva: O(1), O(n), O(n²), O(log n)
- **B5.6** Patrón: conteo y agrupación con diccionario
- **B5.7** Patrón: dos punteros
- **B5.8** Patrón: ventana deslizante

## B6 — Robustez

- **B6.1** Validación de entradas y casos límite
- **B6.2** Manejo de errores y excepciones
- **B6.3** Depuración: hipótesis, observación, reducción
- **B6.4** Pruebas: casos de prueba y aserciones

## B7 — Organización del código

- **B7.1** Lectura y escritura de archivos
- **B7.2** Módulos e importaciones
- **B7.3** Clases y objetos
- **B7.4** Encapsulamiento
- **B7.5** Herencia vs composición
- **B7.6** Polimorfismo e interfaces

## B8 — Paradigmas y temas avanzados

- **B8.1** Estilo funcional: map, filter, reduce, lambdas
- **B8.2** Memoria: pila vs montículo, punteros
- **B8.3** Eventos y programación asíncrona
- **B8.4** Acceso a datos: registros y consultas

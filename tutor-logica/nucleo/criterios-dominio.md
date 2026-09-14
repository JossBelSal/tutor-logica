# Criterios de dominio y auditoría

Este archivo **no es un temario**. El temario es [[Logica - Mapa de conceptos]]. Esto es el
**estándar con el que se decide si un concepto está dominado**, y el procedimiento para auditar
código que no escribiste tú — sobre todo el que genera una IA.

La meta no es memorizar sintaxis. La meta es que la IA deje de ser una caja negra: mirar código
y poder decir qué problema resuelve, cómo se mueve la información, qué supuestos hace, dónde
puede romperse, cómo comprobar que cumple lo que promete y si hay una alternativa mejor.

## Cómo encaja con los demás archivos

- **El método del tutor** → **cómo** se te enseña: primero razonar, luego pistas, y la solución
  completa solo al final. En la bóveda es [[Tutor - Metodo]]; en las demás plataformas,
  `metodo-tutor.md`.
- [[Logica - Mapa de conceptos]] → **qué** estudiar y en qué orden, con los IDs (`B4.10`).
- **Este archivo** → **cuándo** puedes dar un concepto por dominado.
- [[Logica - Bitacora]] → **qué pasó realmente**: qué demostraste, qué quedó débil, qué errores
  enseñaron algo.

Cada módulo de abajo termina con un **"Puedes avanzar cuando:"**. Ese es el criterio duro del
bloque correspondiente del mapa:

| Módulo de este archivo | Conceptos del mapa |
|---|---|
| 1 — Descomponer y pseudocódigo | B1.1 |
| 2 — Flujo de control y trazas | B2.1 – B2.11 |
| 3 — Estado y flujo de datos | B1.3, B3.4, B4.8 |
| 4 — Funciones como contratos | B3.1 – B3.5 |
| 5 — Estructuras y criterio de elección | B4.1 – B4.9 |
| 6 — Casos límite · 7 — Depuración · 8 — Pruebas | B6.1 – B6.5 |
| 9 — Complejidad | B5.1 – B5.9 |
| 10 — Diseño y arquitectura | B7.1 – B7.6 |
| 11 — Auditoría de código de IA | B9.1 – B9.6 |

## Punto de partida

Ya conoces variables, strings, f-strings y tipos de datos básicos. Eso basta para empezar; no
hace falta repasar todo desde cero. Cuando aparezca sintaxis nueva, aprende solo la necesaria
para examinar la idea lógica. Si cambias de lenguaje, la lógica debe seguir siendo reconocible
aunque cambien llaves, sangría, nombres de métodos o tipos.

No marques un tema como dominado porque "te suena" o porque entendiste una explicación. Avanza
cuando puedas demostrarlo con un fragmento nuevo y sin pistas.

---

## Módulo 1 — Descomponer problemas y escribir pseudocódigo

**Objetivo:** pasar de una petición vaga a pasos verificables antes de mirar código.

Practica estas preguntas:

1. ¿Cuál es la entrada?
2. ¿Cuál debe ser la salida?
3. ¿Qué transformaciones ocurren entre ambas?
4. ¿Qué validaciones son necesarias?
5. ¿Qué partes pueden resolverse de forma independiente?
6. ¿Qué información falta en el requisito?

Escribe pseudocódigo en lenguaje natural. No intentes que “parezca código”; debe dejar clara la secuencia y las decisiones.

**Ejercicios:**

- Divide “procesar un archivo de ventas y generar un resumen” en tareas pequeñas.
- Recibe una solución de IA y reconstruye el pseudocódigo que debió existir antes.
- Compara dos descomposiciones del mismo problema y explica cuál separa mejor las responsabilidades.
- Detecta una instrucción ambigua y escribe tres preguntas que habría que resolver antes de programar.

**Puedes avanzar cuando:** tomas un problema nuevo, identificas entradas, salidas, reglas y dudas, y produces pasos que otra persona podría revisar sin ver código.

## Módulo 2 — Flujo de control y trazas manuales

**Objetivo:** seguir el orden real de ejecución en condiciones, bucles y retornos.

Haz trazas manuales con una tabla:

| Paso | Línea o decisión | Valores relevantes | Salida parcial |
|---|---|---|---|

No leas el código “por encima”. Recorre una instrucción a la vez y anota qué rama se tomó y por qué.

**Ejercicios:**

- Predice la salida de fragmentos con `if`, `else`, varios `return` y bucles cortos.
- Encuentra una rama que nunca se ejecuta.
- Cambia una entrada para obligar al programa a recorrer una ruta distinta.
- Explica un error de límite: una iteración de más, una de menos o una condición que nunca termina.
- Corrige el flujo con el menor cambio posible y justifica por qué basta.

**Puedes avanzar cuando:** aciertas la traza de varios casos sin ejecutar el código y puedes señalar exactamente en qué decisión cambia el resultado.

## Módulo 3 — Estado y flujo de datos

**Objetivo:** entender qué datos existen, quién los cambia y cuánto tiempo viven.

Para cada dato importante, identifica:

- dónde nace;
- qué valor inicial tiene;
- quién lo lee;
- quién lo modifica;
- si se copia o se comparte;
- dónde deja de ser necesario;
- qué salida produce.

Pon atención a la mutación: un dato mutable puede cambiar sin que el nombre de la variable cambie. Pregunta también si el orden de las modificaciones altera el resultado.

**Ejercicios:**

- Dibuja el recorrido de un dato desde la entrada hasta la salida.
- Señala todas las líneas que modifican estado.
- Predice qué pasa si dos nombres apuntan al mismo objeto.
- Convierte una secuencia difícil de seguir en transformaciones más explícitas.
- Rompe un programa cambiando el orden de dos actualizaciones y explica la causa.

**Puedes avanzar cuando:** puedes contar la historia completa de un dato y detectar una modificación inesperada o una dependencia oculta del orden.

## Módulo 4 — Funciones como contratos

**Objetivo:** leer cada función como una promesa, no como un bloque de líneas.

El contrato de una función debe aclarar:

- qué recibe;
- qué devuelve;
- qué condiciones deben cumplirse antes de llamarla;
- qué garantiza si esas condiciones se cumplen;
- qué errores puede producir;
- qué efectos secundarios tiene;
- qué cosas quedan fuera de su responsabilidad.

Una función con nombre bonito puede incumplir su contrato. Comprueba el cuerpo, las llamadas y las pruebas.

**Ejercicios:**

- Escribe el contrato de una función existente sin copiar su documentación.
- Busca entradas válidas que contradigan lo que el nombre promete.
- Separa una función que valida, transforma, guarda y notifica en responsabilidades más claras.
- Compara una función con efectos secundarios y otra que devuelve un resultado; explica cuándo conviene cada una.
- Corrige un contrato inconsistente sin recibir la implementación completa.

**Puedes avanzar cuando:** puedes describir una función sin narrar línea por línea, detectar una responsabilidad mezclada y diseñar casos que comprueben su promesa.

## Módulo 5 — Estructuras de datos y criterio de elección

**Objetivo:** elegir estructuras por el tipo de operación, no por costumbre.

Aprende a distinguir, en el lenguaje que estés usando:

- secuencias ordenadas;
- conjuntos de elementos únicos;
- mapas de clave a valor;
- registros u objetos con campos;
- colas y pilas cuando el orden de atención importa.

El criterio debe incluir: orden, duplicados, búsqueda, inserción, recorrido, claridad y tamaño esperado. No existe una estructura “mejor” sin contexto.

**Ejercicios:**

- Decide cómo representar usuarios por identificador, una lista de tareas ordenada y etiquetas sin duplicados.
- Recibe una estructura elegida por IA y cuestiona si conserva el orden o elimina duplicados de forma accidental.
- Compara dos estructuras para la misma tarea y explica el costo de cada una.
- Cambia el requisito —por ejemplo, ahora importan los duplicados— y revisa si la elección sigue siendo válida.
- Detecta datos modelados como strings sueltos que deberían formar un registro coherente.

**Puedes avanzar cuando:** justificas una elección con operaciones y restricciones concretas, y puedes explicar qué requisito haría que cambiaras de estructura.

## Módulo 6 — Casos límite e invariantes

**Objetivo:** pensar en lo que casi nunca aparece en el ejemplo feliz.

Un **caso límite** es una entrada válida o posible en el borde del problema. Un **invariante** es una condición que debe seguir siendo cierta durante o después de una operación.

Revisa, según el problema:

- vacío, cero, uno y valores máximos;
- negativos;
- duplicados;
- orden inesperado;
- datos nulos o incompletos;
- formatos inválidos;
- caracteres especiales;
- fallos parciales;
- reintentos;
- diferencias de zona horaria o precisión.

**Ejercicios:**

- Propón al menos seis casos que el ejemplo principal no cubre.
- Declara tres invariantes y busca una entrada capaz de romperlos.
- Distingue entre “entrada inválida” y “caso válido pero extremo”.
- Modifica un requisito y revisa qué invariantes dejan de servir.
- Encuentra una validación puesta demasiado tarde.

**Puedes avanzar cuando:** puedes atacar una solución sin inventar escenarios absurdos, encuentras bordes relevantes y explicas qué propiedad debe conservarse.

## Módulo 7 — Depuración y lectura de errores

**Objetivo:** localizar causas con evidencia, no adivinar cambios.

Sigue este ciclo:

1. reproduce el fallo;
2. reduce el caso;
3. lee el mensaje desde la primera parte útil del stack trace;
4. formula una hipótesis;
5. cambia o inspecciona una sola cosa;
6. vuelve a probar;
7. registra qué confirmó o descartó la prueba.

Distingue entre síntoma y causa. La línea donde explota el programa puede ser solo el lugar donde una entrada incorrecta se hizo visible.

**Ejercicios:**

- Explica con tus palabras un mensaje de error real.
- Encuentra el primer marco del stack trace que pertenece al proyecto.
- Reduce un fallo grande a la entrada mínima que lo reproduce.
- Propón tres hipótesis ordenadas por probabilidad y una comprobación barata para cada una.
- Corrige el fallo sin silenciarlo ni envolver todo en una captura genérica.

**Puedes avanzar cuando:** puedes pasar del mensaje a una hipótesis comprobable, aislar el caso y explicar por qué la corrección trata la causa.

## Módulo 8 — Pruebas como preguntas ejecutables

**Objetivo:** usar pruebas para verificar comportamiento y revelar supuestos.

Una buena prueba dice:

- dado este estado o entrada;
- cuando ocurre esta acción;
- entonces debe observarse este resultado.

Incluye pruebas del camino feliz, bordes, errores esperados y regresiones. Una prueba que repite la implementación puede aprobar aunque el requisito esté mal entendido.

**Ejercicios:**

- Diseña pruebas antes de pedir código a la IA.
- Convierte cada regla de negocio en al menos una prueba.
- Escribe una prueba que falle por un defecto conocido y comprueba que pasa después de corregirlo.
- Detecta una prueba que no comprueba nada importante.
- Compara pruebas basadas en ejemplos con una propiedad general que siempre deba cumplirse.
- Cambia la implementación sin cambiar el comportamiento y revisa si las pruebas siguen sirviendo.

**Puedes avanzar cuando:** tus pruebas pueden demostrar que una solución incorrecta falla, cubren los riesgos principales y no dependen innecesariamente de detalles internos.

## Módulo 9 — Complejidad y comparación de alternativas

**Objetivo:** comparar soluciones sin caer en “esta se ve más profesional”.

Evalúa:

- tiempo de ejecución al crecer los datos;
- memoria usada;
- número de recorridos;
- llamadas a disco, red o base de datos;
- facilidad para leer, probar y cambiar;
- riesgos añadidos;
- dependencias necesarias.

No optimices por reflejo. Primero pregunta cuál es el tamaño real, qué operación es frecuente y qué restricción importa.

**Ejercicios:**

- Cuenta cuántas veces se recorre una colección.
- Compara una búsqueda repetida en lista con una estructura preparada para búsquedas.
- Identifica una optimización que complica el código sin beneficio relevante.
- Explica el intercambio entre memoria, velocidad y claridad en dos alternativas.
- Predice qué parte será el cuello de botella y diseña una medición para validarlo.

**Puedes avanzar cuando:** eliges entre dos soluciones usando el contexto, puedes estimar cómo escalan y sabes cuándo medir antes de cambiar.

## Módulo 10 — Diseño y arquitectura básica

**Objetivo:** entender cómo se reparten las responsabilidades en un programa pequeño o mediano.

Busca límites claros entre:

- entrada y presentación;
- reglas del negocio;
- acceso a datos o servicios externos;
- configuración;
- manejo de errores;
- registro y observabilidad.

Aprende primero cohesión —mantener juntas las cosas que cambian por la misma razón— y acoplamiento —cuánto depende una parte de detalles de otra—. No necesitas patrones sofisticados para detectar una mezcla incómoda.

**Ejercicios:**

- Dibuja los componentes de un script y las flechas de dependencia.
- Detecta lógica de negocio mezclada con interfaz, archivos o base de datos.
- Propón un límite que permita probar la regla sin usar la dependencia externa.
- Compara una solución de un solo bloque con otra dividida en módulos; explica costos y beneficios.
- Identifica abstracciones prematuras creadas por la IA y simplifícalas.

**Puedes avanzar cuando:** puedes explicar la arquitectura en pocos bloques, justificar sus límites y señalar una dependencia que convendría aislar.

## Módulo 11 — Auditoría de código generado por IA

**Objetivo:** revisar una respuesta de Codex o Claude como trabajo de un colaborador rápido, útil y falible.

Usa esta secuencia cada vez que recibas código importante:

### 1. Reformula el objetivo

Escribe en una frase qué debe lograr la solución y qué queda fuera. Si no puedes hacerlo, todavía no evalúes el código: el requisito no está listo.

### 2. Divide responsabilidades

Enumera las tareas que realiza cada archivo, clase o función. Señala responsabilidades mezcladas, duplicadas o sin dueño.

### 3. Traza los datos

Sigue entradas, transformaciones, almacenamiento y salidas. Marca conversiones, mutaciones, datos sensibles y puntos donde algo puede perderse.

### 4. Enumera supuestos

Anota qué da por hecho el código: formato, permisos, conectividad, versión, volumen, orden, unicidad, zona horaria, existencia de archivos, valores no nulos y comportamiento de servicios externos.

### 5. Detecta requisitos ambiguos

Busca palabras como “rápido”, “seguro”, “reciente”, “válido”, “todos” o “automático”. Conviértelas en reglas medibles o en preguntas para el usuario.

### 6. Identifica riesgos y casos no contemplados

Revisa bordes, concurrencia, fallos parciales, reintentos, seguridad, privacidad, pérdida de datos, compatibilidad y recuperación.

### 7. Verifica dependencias

Comprueba:

- que la librería o API existe;
- que la versión usada ofrece esos métodos;
- que la firma y el comportamiento coinciden con documentación oficial;
- que la licencia y el mantenimiento son aceptables;
- que no se añadió una dependencia para resolver algo trivial;
- que secretos y permisos se manejan correctamente.

No confíes en nombres plausibles inventados por la IA.

### 8. Diseña pruebas antes de aprobar

Asocia cada requisito y riesgo importante con una prueba. Incluye por lo menos un caso feliz, un borde, un error esperado y una regresión si ya hubo un fallo.

### 9. Clasifica el origen del fallo

Cuando algo sale mal, pregunta:

- **¿Fallo del código?** La implementación no cumple un requisito claro.
- **¿Fallo del requisito?** La regla estaba incompleta, era contradictoria o no definía el caso.
- **¿Fallo de la instrucción a la IA?** El requisito existía, pero el prompt no lo comunicó o empujó a una suposición incorrecta.

A veces hay más de un origen. No “arregles el código” hasta saber qué contrato debe cumplir.

**Ejercicios de auditoría:**

- Audita una respuesta de IA sin ejecutarla y escribe tus cinco sospechas principales.
- Verifica una dependencia y una firma de función contra documentación oficial.
- Construye una matriz de requisito → parte del código → prueba.
- Encuentra una ambigüedad que permita dos implementaciones incompatibles.
- Provoca un fallo y clasifica su origen con evidencia.
- Compara dos respuestas de IA sin elegir por cantidad de código: usa claridad, cobertura, riesgos, pruebas y costo de mantenimiento.
- Pide una corrección dando solo el diagnóstico y los criterios de aceptación, no la solución.

**Puedes avanzar cuando:** puedes rechazar o aprobar una solución con razones concretas, pruebas y fuentes; detectas supuestos ocultos; y separas claramente problemas de implementación, requisito y prompt.

---

## Secuencia recomendada

Sigue este orden:

1. Descomposición y pseudocódigo.
2. Flujo de control y trazas.
3. Estado y flujo de datos.
4. Funciones como contratos.
5. Estructuras de datos.
6. Casos límite e invariantes.
7. Depuración y errores.
8. Pruebas.
9. Complejidad.
10. Diseño y arquitectura.
11. Auditoría integral de código generado por IA.

No tienes que “terminar programación” antes de auditar IA. Desde el módulo 1 puedes aplicar una versión pequeña de la auditoría. El módulo 11 reúne todas las piezas y las vuelve un procedimiento repetible.

Ritmo sugerido por módulo:

1. **Entender:** explica el concepto con un ejemplo corto.
2. **Predecir:** analiza código nuevo sin ejecutarlo.
3. **Romper:** busca un caso que revele un defecto.
4. **Corregir:** propone el cambio mínimo y explica el contrato recuperado.
5. **Comparar:** evalúa dos alternativas y sus costos.
6. **Transferir:** repite la idea con otro problema o lenguaje.

## Regla clara para avanzar

Avanza solo si puedes completar, con un ejemplo que no hayas visto antes y sin pistas, estas cuatro acciones:

- predecir el comportamiento;
- explicar el porqué con tus palabras;
- encontrar o proponer un caso que lo rompa;
- justificar una corrección o una alternativa.

Además, debes acertar al menos dos ejercicios separados, no dos variaciones casi idénticas. Si fallas, no reinicies el módulo completo: registra el punto débil y practica exactamente esa pieza.

“Lo entendí al leerlo” no cuenta. “Puedo demostrarlo y defender mi decisión” sí.

## Qué registrar en [[Logica - Bitacora]]

Separa siempre dos capas:

### Lógica reutilizable

Ideas que sobreviven al cambio de lenguaje:

- descomposición;
- contratos;
- flujo de datos;
- invariantes;
- casos límite;
- estrategia de depuración;
- diseño de pruebas;
- criterios para comparar;
- decisiones de arquitectura.

### Sintaxis específica del lenguaje

Detalles que debes consultar o practicar en un lenguaje concreto:

- palabras reservadas;
- forma de declarar tipos;
- métodos de colecciones;
- manejo de errores;
- reglas de alcance;
- módulos e importaciones;
- comportamiento de referencias;
- versión y entorno.

En cada entrada de la bitácora puedes añadir:

```markdown
- **Lógica reutilizable:** ...
- **Sintaxis del lenguaje:** ...
```

No confundas un tropiezo de sintaxis con una falla de razonamiento. Si la idea era correcta pero escribiste mal un método, regístralo como sintaxis. Si el código corre pero resuelve mal el problema, regístralo como lógica.

## Formato recomendado para pedir una sesión

Puedes iniciar con algo así:

> Estoy en el módulo X. Dame un fragmento corto para predecir y auditar. No me des la solución. Primero pídeme que explique el objetivo, trace los datos y proponga casos límite. Evalúa mi respuesta con los criterios de dominio del módulo y registra por separado lógica y sintaxis.

La ruta termina cuando ya no aceptas código porque “se ve bien”, sino porque puedes explicar qué promete, cómo lo comprobaste y bajo qué condiciones dejaría de ser correcto.

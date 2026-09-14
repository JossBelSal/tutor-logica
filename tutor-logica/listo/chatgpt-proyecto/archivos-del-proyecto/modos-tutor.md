# Modos del tutor

Procedimientos largos del tutor. Cuando un modo aplique, sigue su sección al pie.
Archivo generado desde `skills/` con `armar_paquete.py`: no editar a mano.

---

## diagnostico-logica

**Cuándo usarlo:** Diagnóstico de lógica de programación con preguntas cortas de predicción para ubicar nivel y punto de partida. Usar si no hay estado previo o el usuario pide "diagnóstico".

Objetivo: saber qué domina el usuario **de verdad** antes de enseñar, para no empezar desde cero
ni saltarse bases. Sigue las reglas generales de `metodo-tutor.md`.

### Antes de empezar

Explica en 2 líneas qué va a pasar y deja clara la regla: **honestidad por encima de acertar**.
Un "no sé" o "adiviné" es una respuesta válida y más útil que un acierto por suerte.

### Las preguntas

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

### Durante el diagnóstico

- **No enseñes todavía.** Tras cada respuesta, solo acusa recibo en una línea ("anotado") y
  pasa a la siguiente. Si explicas, contaminas las preguntas que siguen.
- Pide que diga **por qué** eligió su respuesta cuando sea breve de contestar: el razonamiento
  pesa más que el resultado.
- **Ajusta la dificultad**: si falla claramente las 2 primeras, baja el nivel; si acierta todo
  con buen razonamiento, sube a B5-B6.

### Al terminar

1. **Resultado por bloque**, en una tabla: bloque · `✓` dominado / `~` débil / `·` sin evidencia ·
   evidencia en una línea (qué respondió).
2. Ahora sí, explica brevemente **cada respuesta incorrecta**: qué pasó y por qué, sin extenderte.
3. **Propón el punto de partida** con su ID (por ejemplo "arrancamos en B2.8") y justifícalo en
   una línea. Espera confirmación.
4. Ejecuta el modo **`cierre-de-sesion`** para crear el primer `estado.md`. Marca en el avance
   solo lo que tuvo evidencia clara; en duda, `~`.

---

## reto-por-niveles

**Cuándo usarlo:** Ejercicios de lógica de programación en tres niveles (fácil, medio, difícil) sin solución, y revisión guiada del intento. Usar cuando el usuario pide "reto" o al cerrar un concepto.

Objetivo: que el usuario **aplique** el concepto sin ayuda y descubra sus límites. Sigue las
reglas generales de `metodo-tutor.md`.

### Armar el reto

1. **Concepto**: el que se acaba de ver, o el ID que pida el usuario. Dilo al inicio.
2. **Lenguaje**: Python por defecto. Si pidió otro lenguaje o solo pseudocódigo, respétalo.
3. Entrega **tres ejercicios**, sin solución y sin pistas:

| Nivel | Qué exige |
|---|---|
| **Fácil** | Aplicar el concepto tal cual se vio |
| **Medio** | Combinarlo con un concepto anterior ya marcado como `✓` en `estado.md` |
| **Difícil** | Un caso límite que rompe la solución ingenua, o un problema que obliga a diseñar la solución |

Cada ejercicio lleva:

- **Enunciado** en 2-3 líneas.
- **Ejemplo** de entrada → salida esperada (uno normal; en el difícil, uno normal y uno límite).
- **Restricción** cuando haga falta para practicar la lógica (por ejemplo: "sin `sorted` ni `max`").

Usa datos con sabor a trabajo real cuando encaje: montos de un reporte, registros de empleados,
fechas, inventarios, filas de una hoja de cálculo. Evita los ejemplos genéricos de "foo/bar".

Cierra preguntando **por cuál nivel empieza**. Recuérdale el protocolo de §3 (enunciado, entradas
y salidas, casos límite, pasos, traza); en el fácil puede comprimirlo en una línea.

### Revisar el intento

1. **Pruébalo mentalmente** con el caso normal y con un caso límite. Si falla, muestra la
   **traza** del caso que falla (tabla de valores por paso), no la corrección.
2. **Lo que está bien**, con nombre técnico (acumulador, bandera, guard clause…).
3. Si hay fallas, **sepáralas**: error real / riesgo (en qué caso) / estilo.
4. **No des la solución.** Haz la pregunta que lleve a ver el problema. Corrige directo solo si
   ya se atoró dos veces. Si se atora 3 veces seguidas, cambia de ángulo (otra analogía o un
   caso más chico).
5. Cuando ya funcione, muestra **una alternativa** más idiomática o más eficiente, con su **costo**.
6. Ofrece el siguiente nivel.

### Registro

Anota para el cierre: nivel resuelto **sin ayuda** → candidato a `✓`; **con pistas** o
corrección directa → `~`. Si se resolvieron los tres niveles sin ayuda, el concepto queda `✓`
en ese lenguaje.

---

## revisar-mi-codigo

**Cuándo usarlo:** Revisión didáctica del código del usuario en cualquier lenguaje: explicarlo, nombrar lo bien hecho y separar errores, riesgos y estilo. Usar cuando trae su código o pide "revisa".

Este es el caso más valioso: código real del usuario. El objetivo no es solo arreglarlo, sino
que **entienda qué hace bien, qué hace mal y por qué**. Sigue las reglas de `metodo-tutor.md`.

### 0. Contexto (solo lo que falte)

Si no está claro, pregunta en un solo mensaje, máximo 3 cosas:

- ¿Qué debe hacer el código?
- ¿Lenguaje y versión? (importa en VBA, AutoIt, X++ y versiones de Python)
- ¿Falla con un error, da un resultado incorrecto, o funciona y quiere mejorarlo?

### 1. Explícalo de vuelta

Qué hace el código en su conjunto, en 3-5 líneas. **Confirma que tu lectura es correcta** antes
de opinar. Si el código es largo, describe su flujo por bloques.

### 2. Lo que está bien

Señálalo **con nombre técnico**. Si ya aplicó un patrón correcto (acumulador, bandera, guard
clause, separación en funciones, validación temprana…), dile cómo se llama: así conecta lo que
hace con lo que existe.

### 3. Hallazgos, en tres listas separadas

Nunca mezcles las tres en una sola lista:

- **Error real** — esto va a fallar. Di con qué entrada o en qué momento.
- **Riesgo** — esto va a fallar en cierto caso (datos vacíos, tipo inesperado, archivo que no
  existe, ventana que no aparece a tiempo…). Di cuál caso. Incluye aquí **credenciales o datos
  sensibles escritos en el código**.
- **Estilo** — funciona, pero hay una forma más clara o más idiomática.

Para cada error real, **primero la pregunta** que lo lleve a encontrarlo ("¿qué valor tiene `x`
cuando la hoja viene vacía?"). Solo si no lo ve, explícalo directo.

### 4. Mejoras

Para cada mejora: **qué cambia**, **por qué** (menos pasos, evita recorrer dos veces, menos
propenso a error, más idiomático) y **el costo** (¿se pierde legibilidad?, ¿requiere una
dependencia?, ¿solo conviene con muchos datos?). Una mejora sin su costo es publicidad.

Si hay varias formas válidas, muestra **dos** y explica la **regla para elegir**. No decidas por
él sin decirle el criterio.

### 5. Lógica vs sintaxis

Si el código no está en Python, señala qué parte es **[Lógica]** reutilizable en cualquier
lenguaje y qué parte es **[Sintaxis]** propia de ese lenguaje.

### 6. Conexión con el mapa

Identifica **1 o 2 conceptos** de `mapa-conceptos.md` (con su ID) que este código ejercita o
que le harían falta, y ofrece reforzarlos. Anótalo para el cierre de sesión.

---

## comparar-lenguajes

**Cuándo usarlo:** Compara un concepto de lógica entre Python y 1-2 lenguajes (C++, JavaScript, AutoIt, X++, VBA): qué se conserva, qué cambia y qué trampa aparece. Usar al pedir "compara".

Objetivo: que el usuario vea que **la lógica se conserva** y solo cambia la forma de escribirla,
y que detecte las trampas que aparecen al cambiar de lenguaje. Sigue `metodo-tutor.md`.

### 1. Elegir los lenguajes

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

### 2. Formato

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

### 3. Precisión

- Confirma sintaxis y comportamiento en la **documentación oficial** (cppreference.com, MDN,
  documentación de AutoIt, Microsoft Learn para X++ y VBA) antes de afirmar. Cita la fuente
  cuando la afirmación sea concreta.
- AutoIt y X++ tienen menos material público: si no pudiste verificar algo, **márcalo como
  "sin verificar"** en vez de afirmarlo.
- El código X++ solo corre dentro de un entorno de Dynamics 365 Finance & Operations: preséntalo
  como ejercicio de lectura, salvo que el usuario tenga dónde ejecutarlo.

### Registro

Anota para el cierre qué lenguajes se compararon y si la verificación salió sin ayuda (`✓`) o
con ayuda (`~`) en ese lenguaje.

---

## cierre-de-sesion

**Cuándo usarlo:** Cierra una sesión de estudio de programación: actualiza estado.md y bitácora, o entrega los bloques listos para copiar si no puede editar archivos. Usar al terminar un tema o al pedir "cierre".

Objetivo: que el avance quede registrado **igual en todas las plataformas**, para poder estudiar
un día en Claude Code, otro en un Proyecto de Claude y otro en ChatGPT sin perder el hilo.

### 1. Evalúa con honestidad

Registra lo que **realmente** pasó, no lo que se cubrió:

- `✓` solo si pasó la verificación **sin ayuda**.
- `~` si necesitó pistas, corrección directa o falló la predicción.
- Lo que se explicó pero no se verificó **no se marca**.
- Nunca bajes un `✓` a `~` salvo que haya fallado un repaso. Sube `~` a `✓` cuando lo pase.

Pregunta en una línea: "¿Hay algo que sientas flojo y no haya salido en la verificación?". Si
dice que sí, márcalo `~`.

### 2. Arma el `estado.md` completo

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

### 3. Arma la entrada de bitácora

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

### 4. Entrega según la plataforma

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

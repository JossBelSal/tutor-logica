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

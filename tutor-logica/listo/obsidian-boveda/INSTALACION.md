# Paquete para obsidian-jbs

Este adaptador tiene como destino una bóveda existente con `Logica/Conceptos/`,
`Logica/Logica - Bitacora.md` y `99-Plantillas/Plantilla - Concepto.md`.
Las rutas de instrucciones se interpretan desde la raíz de la bóveda.

## Generar

Desde la carpeta que contiene el script: `python armar_paquete.py`.
El resultado está en `listo/obsidian-boveda/`. No se sincroniza con GitHub ni con
otra carpeta automáticamente. Revisa tus cambios locales antes de instalar.

## Instalar

1. Copia `CLAUDE.md`, las seis carpetas de `.claude/skills/`, los dos agentes
   y `Logica/_tutor/Tutor - Metodo.md` a las rutas homónimas de la bóveda.
   Revisa cualquier cambio local de esos archivos antes de reemplazarlos.
2. En `AGENTS.md`, sustituye únicamente el bloque entre
   `<!-- tutor:inicio -->` y `<!-- tutor:fin -->` por `AGENTS-tutor.md`.
   Si no existe, agrega ese bloque. No reemplaces el resto de AGENTS.md.
3. Compara el mapa y los criterios generados con las notas existentes; integra
   sus cambios conservando tus anotaciones. No copies la carpeta completa a ciegas.
4. Verifica las referencias en Obsidian. El paquete presupone la plantilla y la
   bitácora indicadas arriba; no las crea ni las reemplaza.

El paquete nunca contiene `estado.md`, notas personales de conceptos ni una
bitácora. No borra archivos de la bóveda. `MANIFIESTO.json` registra la correspondencia entre
las fuentes del adaptador y los archivos distribuidos. Usa el commit de Git
para identificar la versión exacta de esas fuentes.

## Mantenimiento

Edita `adaptadores/obsidian-boveda/` y regenera. Estos son adaptadores
específicos recuperados de obsidian-jbs (0c8bd18103fe3f6ff027e45aa524b29e0d057150).
Las otras tres plataformas conservan por ahora su núcleo y sus cinco modos.
No se afirma que estén unificadas: los cambios pedagógicos comunes deben
revisarse también en `nucleo/` y `skills/` hasta completar esa migración.

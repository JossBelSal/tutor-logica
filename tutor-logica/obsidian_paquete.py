"""Distribución específica para una bóveda existente; no escribe en la bóveda."""
import json
from pathlib import Path

ARCHIVOS = {
    "AGENTS-tutor.md": "AGENTS-tutor.md",
    "CLAUDE.md": "CLAUDE.md",
    "INSTALACION.md": "INSTALACION.md",
    "agentes/dynamics.md": ".claude/agents/dynamics.md",
    "agentes/pythor.md": ".claude/agents/pythor.md",
    "criterios-dominio.md": "Logica/Logica - Criterios de dominio.md",
    "mapa-conceptos.md": "Logica/Logica - Mapa de conceptos.md",
    "metodo-tutor.md": "Logica/_tutor/Tutor - Metodo.md",
    "skills/cierre-de-sesion/SKILL.md": ".claude/skills/cierre-de-sesion/SKILL.md",
    "skills/comparar-lenguajes/SKILL.md": ".claude/skills/comparar-lenguajes/SKILL.md",
    "skills/destilar-sesion/SKILL.md": ".claude/skills/destilar-sesion/SKILL.md",
    "skills/diagnostico-logica/SKILL.md": ".claude/skills/diagnostico-logica/SKILL.md",
    "skills/reto-por-niveles/SKILL.md": ".claude/skills/reto-por-niveles/SKILL.md",
    "skills/revisar-mi-codigo/SKILL.md": ".claude/skills/revisar-mi-codigo/SKILL.md"
}

def validar(raiz: Path) -> None:
    """Comprueba todas las fuentes antes de regenerar listo/."""
    fuente = raiz / "adaptadores" / "obsidian-boveda"
    for origen, destino in ARCHIVOS.items():
        ruta = fuente / origen
        if not ruta.is_file():
            raise ValueError(f"Falta fuente de Obsidian: {ruta}")
        if Path(destino).is_absolute() or ".." in Path(destino).parts:
            raise ValueError(f"Destino fuera del paquete: {destino}")
        texto = ruta.read_text(encoding="utf-8")
        if origen.startswith("skills/"):
            for antigua in ("`metodo-tutor.md`", "`mapa-conceptos.md`",
                            "`criterios-dominio.md`", "`destilar-chat`"):
                if antigua in texto:
                    raise ValueError(f"Referencia sin adaptar en {origen}: {antigua}")
    for nombre in ("diagnostico-logica", "reto-por-niveles"):
        texto = (fuente / "skills" / nombre / "SKILL.md").read_text(encoding="utf-8")
        if "estado.md" in texto:
            raise ValueError(f"{nombre} usa estado.md en una bóveda")
    bloque = (fuente / "AGENTS-tutor.md").read_text(encoding="utf-8")
    if bloque.count("<!-- tutor:inicio -->") != 1 or bloque.count("<!-- tutor:fin -->") != 1:
        raise ValueError("El bloque de AGENTS necesita exactamente un par de marcadores")
    if bloque.index("<!-- tutor:inicio -->") >= bloque.index("<!-- tutor:fin -->"):
        raise ValueError("Marcadores de AGENTS fuera de orden")

def generar(raiz: Path) -> None:
    """Genera solamente listo/obsidian-boveda, sin datos de progreso."""
    validar(raiz)
    fuente = raiz / "adaptadores" / "obsidian-boveda"
    salida = raiz / "listo" / "obsidian-boveda"
    registros = []
    for origen, destino in ARCHIVOS.items():
        datos = (fuente / origen).read_bytes()
        ruta = salida / destino
        ruta.parent.mkdir(parents=True, exist_ok=True)
        ruta.write_bytes(datos)
        registros.append({"fuente": origen, "destino": destino})
    manifiesto = {"formato": 1, "adaptador": "obsidian-boveda", "archivos": registros}
    (salida / "MANIFIESTO.json").write_text(
        json.dumps(manifiesto, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

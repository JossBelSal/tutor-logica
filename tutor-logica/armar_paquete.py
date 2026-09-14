"""Arma los paquetes del tutor para cada plataforma a partir de las fuentes.

Fuentes (lo único que se edita a mano):
    nucleo/        metodo-tutor.md, mapa-conceptos.md, criterios-dominio.md, estado.md
    skills/        una carpeta por modo con su SKILL.md
    adaptadores/   lo específico de cada plataforma destino

Salida (se regenera completa, no editar a mano):
    listo/claude-code/programacion/   carpeta plana lista para Claude Code
    listo/claude-proyecto/            instrucciones + archivos + skills en .zip
    listo/chatgpt-proyecto/           instrucciones + archivos (modos en un solo .md)
    listo/obsidian-boveda/            lo que se copia sobre la bóveda de Obsidian

Uso:
    python armar_paquete.py            arma el paquete
    python armar_paquete.py --check    no escribe nada; falla si listo/ está desfasado
"""

import filecmp
import re
import shutil
import sys
import tempfile
import zipfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
NUCLEO = RAIZ / "nucleo"
SKILLS = RAIZ / "skills"
ADAPT = RAIZ / "adaptadores"
LISTO = RAIZ / "listo"

# Archivos del núcleo que viajan tal cual a las plataformas de carpeta plana y de chat.
ARCHIVOS_NUCLEO = ["metodo-tutor.md", "mapa-conceptos.md", "criterios-dominio.md", "estado.md"]

ORDEN_MODOS = [
    "diagnostico-logica",
    "reto-por-niveles",
    "revisar-mi-codigo",
    "comparar-lenguajes",
    "cierre-de-sesion",
    "destilar-sesion",
]

CARPETAS_LENGUAJE = ["logica", "python", "cpp", "javascript", "autoit", "xpp", "vba"]

MAX_NOMBRE = 64        # límite de claude.ai para `name`
MAX_DESCRIPCION = 200  # límite de claude.ai para `description`

# La bóveda exige frontmatter con tags y fecha, o la nota es invisible para Dataview.
# clave: archivo de nucleo/ · valor: (ruta dentro de la bóveda, tags, fragmento que se anexa)
NOTAS_BOVEDA = {
    "metodo-tutor.md": (
        "Logica/_tutor/Tutor - Metodo.md",
        "[tipo/tutor, estado/en-curso]",
        None,
    ),
    "criterios-dominio.md": (
        "Logica/Logica - Criterios de dominio.md",
        "[tipo/logica, estado/en-curso]",
        None,
    ),
    "mapa-conceptos.md": (
        "Logica/Logica - Mapa de conceptos.md",
        "[tipo/logica, estado/en-curso]",
        "mapa-avance.md",
    ),
}

FECHA_NOTAS = "2026-09-14"  # `creado:` de las notas generadas; fijo para que el build sea estable


def leer(ruta: Path) -> str:
    return ruta.read_text(encoding="utf-8")


def escribir(ruta: Path, texto: str) -> None:
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text(texto, encoding="utf-8", newline="\n")


def separar_frontmatter(texto: str) -> tuple[dict, str]:
    """Devuelve (campos del frontmatter, cuerpo). Solo acepta `clave: valor` de una línea."""
    m = re.match(r"^---\n(.*?)\n---\n", texto, re.S)
    if not m:
        raise ValueError("SKILL.md sin frontmatter")
    campos = {}
    for linea in m.group(1).splitlines():
        clave, sep, valor = linea.partition(":")
        if not sep:
            raise ValueError(f"línea de frontmatter sin ':' → {linea!r}")
        valor = valor.strip()
        if valor[:1] in ('"', "[", "{", "|", ">"):
            # El parser es de una línea: mejor rechazar ruidosamente que aceptar mal.
            raise ValueError(
                f"valor no soportado en '{clave.strip()}': usa texto plano o comillas simples"
            )
        if len(valor) >= 2 and valor[0] == valor[-1] == "'":
            valor = valor[1:-1].replace("''", "'")  # comillas simples de YAML
        campos[clave.strip()] = valor
    return campos, texto[m.end():]


def validar_skill(carpeta: Path, campos: dict) -> list[str]:
    errores = []
    nombre = campos.get("name", "")
    desc = campos.get("description", "")
    if nombre != carpeta.name:
        errores.append(f"name '{nombre}' no coincide con la carpeta '{carpeta.name}'")
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", nombre):
        errores.append(f"name '{nombre}' debe ir en minúsculas con guiones")
    if len(nombre) > MAX_NOMBRE:
        errores.append(f"name mide {len(nombre)} (máx. {MAX_NOMBRE})")
    if not desc:
        errores.append("falta description")
    elif len(desc) > MAX_DESCRIPCION:
        errores.append(f"description mide {len(desc)} (máx. {MAX_DESCRIPCION})")
    return errores


def bajar_titulos(cuerpo: str) -> str:
    """Quita el título '# Modo: …' y baja un nivel los demás, sin tocar bloques de código."""
    salida, en_codigo = [], False
    for linea in cuerpo.splitlines():
        if linea.lstrip().startswith(("```", "~~~")):
            en_codigo = not en_codigo
        elif not en_codigo and re.match(r"^# ", linea):
            continue  # el título lo pone el encabezado del modo
        elif not en_codigo and re.match(r"^#{2,5} ", linea):
            linea = "#" + linea
        salida.append(linea)
    return "\n".join(salida).strip() + "\n"


def envolver_nota_boveda(cuerpo: str, tags: str, anexo: str | None) -> str:
    """Le pone a un archivo del núcleo el frontmatter que la bóveda exige para Dataview."""
    partes = [f"---\ntags: {tags}\ncreado: {FECHA_NOTAS}\n---\n\n", cuerpo.strip(), "\n"]
    if anexo:
        partes.append("\n" + anexo.strip() + "\n")
    return "".join(partes)


def escribir_zip_reproducible(destino: Path, carpeta: Path) -> None:
    """ZIP con fecha fija: el archivo solo cambia si cambia el contenido."""
    with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(carpeta.rglob("*")):
            if f.is_file():
                info = zipfile.ZipInfo(
                    str(Path(carpeta.name) / f.relative_to(carpeta)),
                    date_time=(1980, 1, 1, 0, 0, 0),
                )
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o644 << 16
                z.writestr(info, f.read_bytes())


def diferencias(a: Path, b: Path, prefijo: str = "") -> list[str]:
    """Compara dos árboles por contenido. Devuelve una lista de diferencias legibles."""
    cmp = filecmp.dircmp(a, b)
    fuera = []
    fuera += [f"{prefijo}{n}: sobra en listo/" for n in sorted(cmp.left_only)]
    fuera += [f"{prefijo}{n}: falta en listo/" for n in sorted(cmp.right_only)]
    iguales, distintos, errores = filecmp.cmpfiles(a, b, cmp.common_files, shallow=False)
    fuera += [f"{prefijo}{n}: contenido distinto" for n in sorted(distintos)]
    fuera += [f"{prefijo}{n}: no se pudo comparar" for n in sorted(errores)]
    for sub in sorted(cmp.common_dirs):
        fuera += diferencias(a / sub, b / sub, f"{prefijo}{sub}/")
    return fuera


def construir(destino_raiz: Path, skills: list, modos: str) -> None:
    """Escribe el paquete completo bajo `destino_raiz`. No toca nada fuera de ahí."""
    # 1. Claude Code (carpeta plana, el tutor escribe estado.md y bitacora.md)
    cc = destino_raiz / "claude-code" / "programacion"
    cc.mkdir(parents=True)
    shutil.copy2(ADAPT / "claude-code" / "CLAUDE.md", cc / "CLAUDE.md")
    for archivo in ARCHIVOS_NUCLEO:
        shutil.copy2(NUCLEO / archivo, cc / archivo)
    for carpeta, _, _ in skills:
        shutil.copytree(carpeta, cc / ".claude" / "skills" / carpeta.name)
    for sub in CARPETAS_LENGUAJE:
        # git no versiona carpetas vacías: sin esto el clon no trae la estructura.
        escribir(cc / sub / ".gitkeep", "")

    # 2. Proyectos de chat (no pueden escribir archivos: los modos van en un solo .md)
    for plataforma in ["claude-proyecto", "chatgpt-proyecto"]:
        destino = destino_raiz / plataforma
        archivos = destino / "archivos-del-proyecto"
        archivos.mkdir(parents=True)
        shutil.copy2(ADAPT / plataforma / "instrucciones.md", destino / "instrucciones.md")
        for archivo in ARCHIVOS_NUCLEO:
            shutil.copy2(NUCLEO / archivo, archivos / archivo)
        escribir(archivos / "modos-tutor.md", modos)

    # 3. Skills en .zip para claude.ai  (zip → carpeta-skill/SKILL.md)
    zips = destino_raiz / "claude-proyecto" / "skills-para-subir"
    zips.mkdir()
    for carpeta, _, _ in skills:
        escribir_zip_reproducible(zips / f"{carpeta.name}.zip", carpeta)

    # 4. Bóveda de Obsidian (el avance vive en frontmatter + Dataview, no en estado.md)
    bov = destino_raiz / "obsidian-boveda"
    bov.mkdir(parents=True)
    origen_bov = ADAPT / "obsidian-boveda"
    shutil.copy2(origen_bov / "CLAUDE.md", bov / "CLAUDE.md")
    shutil.copy2(origen_bov / "AGENTS-tutor.md", bov / "AGENTS-tutor.md")
    for agente in sorted((origen_bov / "agentes").glob("*.md")):
        escribir(bov / ".claude" / "agents" / agente.name, leer(agente))
    for carpeta, _, _ in skills:
        escribir(
            bov / ".claude" / "skills" / carpeta.name / "SKILL.md",
            leer(carpeta / "SKILL.md"),
        )
    for archivo, (ruta, tags, anexo) in NOTAS_BOVEDA.items():
        texto_anexo = leer(origen_bov / "fragmentos" / anexo) if anexo else None
        escribir(bov / ruta, envolver_nota_boveda(leer(NUCLEO / archivo), tags, texto_anexo))


def main() -> int:
    modo_check = "--check" in sys.argv[1:]
    sobra = [a for a in sys.argv[1:] if a != "--check"]
    if sobra:
        print(f"Argumento no reconocido: {sobra[0]}\nUso: python armar_paquete.py [--check]")
        return 2

    # 1. Leer y validar skills
    skills, errores = [], []
    for nombre in ORDEN_MODOS:
        carpeta = SKILLS / nombre
        try:
            campos, cuerpo = separar_frontmatter(leer(carpeta / "SKILL.md"))
        except (OSError, ValueError) as e:
            errores.append(f"[{nombre}] {e}")
            continue
        errores += [f"[{nombre}] {e}" for e in validar_skill(carpeta, campos)]
        skills.append((carpeta, campos, cuerpo))
    extras = {p.name for p in SKILLS.iterdir() if p.is_dir()} - set(ORDEN_MODOS)
    if extras:
        errores.append(f"Skills sin registrar en ORDEN_MODOS: {sorted(extras)}")
    if errores:
        print("ERRORES:\n  " + "\n  ".join(errores))
        return 1

    # 2. modos-tutor.md (para las plataformas sin skills)
    partes = [
        "# Modos del tutor\n\n"
        "Procedimientos largos del tutor. Cuando un modo aplique, sigue su sección al pie.\n"
        "Archivo generado desde `skills/` con `armar_paquete.py`: no editar a mano.\n"
    ]
    for carpeta, campos, cuerpo in skills:
        partes.append(
            f"\n---\n\n## {campos['name']}\n\n"
            f"**Cuándo usarlo:** {campos['description']}\n\n{bajar_titulos(cuerpo)}"
        )
    modos = "".join(partes)

    # 3. Construir (en un temporal si es --check, para no tocar listo/)
    if modo_check:
        with tempfile.TemporaryDirectory() as tmp:
            esperado = Path(tmp) / "listo"
            esperado.mkdir()
            construir(esperado, skills, modos)
            if not LISTO.exists():
                print("ERROR: listo/ no existe. Corre `python armar_paquete.py`.")
                return 1
            difs = diferencias(LISTO, esperado)
        if difs:
            print("listo/ está desfasado respecto de las fuentes:")
            print("  " + "\n  ".join(difs))
            print("\nCorre `python armar_paquete.py` y vuelve a commitear.")
            return 1
        print(f"listo/ está sincronizado con las fuentes ({len(skills)} modos).")
        return 0

    if LISTO.exists():
        shutil.rmtree(LISTO)
    LISTO.mkdir()
    construir(LISTO, skills, modos)

    # 4. Resumen
    print("Paquete armado en:", LISTO)
    for carpeta, campos, _ in skills:
        print(f"  modo {campos['name']:<20} descripción: {len(campos['description'])}/{MAX_DESCRIPCION}")
    for plataforma in ["claude-proyecto", "chatgpt-proyecto"]:
        n = len(leer(ADAPT / plataforma / "instrucciones.md"))
        print(f"  instrucciones {plataforma:<17} {n} caracteres")
    print(f"  CLAUDE.md de la bóveda            {len(leer(ADAPT / 'obsidian-boveda' / 'CLAUDE.md'))} caracteres")
    return 0


if __name__ == "__main__":
    sys.exit(main())

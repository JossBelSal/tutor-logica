"""Pruebas de las tres funciones puras de armar_paquete.py.

Ahí vive todo el riesgo de regresión: el parser de frontmatter, la validación de skills y
la degradación de títulos. Correr con:  python -m unittest discover -s pruebas
"""

import sys
import unittest
import zipfile
from pathlib import Path
from tempfile import TemporaryDirectory

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from armar_paquete import (  # noqa: E402
    bajar_titulos,
    escribir_zip_reproducible,
    envolver_nota_boveda,
    separar_frontmatter,
    validar_skill,
)


class SepararFrontmatter(unittest.TestCase):
    def test_lee_clave_valor_simple(self):
        campos, cuerpo = separar_frontmatter("---\nname: uno\n---\n# Título\n")
        self.assertEqual(campos["name"], "uno")
        self.assertEqual(cuerpo, "# Título\n")

    def test_desenvuelve_comillas_simples(self):
        campos, _ = separar_frontmatter("---\ndescription: 'hola: mundo'\n---\ncuerpo\n")
        self.assertEqual(campos["description"], "hola: mundo")

    def test_conserva_los_dos_puntos_del_valor(self):
        campos, _ = separar_frontmatter("---\nd: a: b\n---\nx\n")
        self.assertEqual(campos["d"], "a: b")

    def test_sin_frontmatter_revienta(self):
        with self.assertRaises(ValueError):
            separar_frontmatter("# Solo un título\n")

    def test_comillas_dobles_se_rechazan(self):
        # El parser es de una línea: mejor fallar ruidosamente que colar las comillas al .zip.
        with self.assertRaises(ValueError):
            separar_frontmatter('---\ndescription: "hola"\n---\nx\n')

    def test_lista_se_rechaza(self):
        with self.assertRaises(ValueError):
            separar_frontmatter("---\ntools: [Read, Grep]\n---\nx\n")

    def test_escalar_de_bloque_se_rechaza(self):
        with self.assertRaises(ValueError):
            separar_frontmatter("---\ndescription: |\n  larga\n---\nx\n")

    def test_linea_sin_dos_puntos_se_rechaza(self):
        with self.assertRaises(ValueError):
            separar_frontmatter("---\nsolo-texto\n---\nx\n")


class ValidarSkill(unittest.TestCase):
    def campos(self, **kw):
        base = {"name": "modo-uno", "description": "hace algo útil"}
        base.update(kw)
        return base

    def test_skill_correcta_no_da_errores(self):
        self.assertEqual(validar_skill(Path("modo-uno"), self.campos()), [])

    def test_name_distinto_de_la_carpeta(self):
        errores = validar_skill(Path("otra-carpeta"), self.campos())
        self.assertTrue(any("no coincide con la carpeta" in e for e in errores))

    def test_name_con_mayusculas(self):
        errores = validar_skill(Path("Modo-Uno"), self.campos(name="Modo-Uno"))
        self.assertTrue(any("minúsculas con guiones" in e for e in errores))

    def test_name_con_guion_bajo(self):
        errores = validar_skill(Path("modo_uno"), self.campos(name="modo_uno"))
        self.assertTrue(any("minúsculas con guiones" in e for e in errores))

    def test_description_faltante(self):
        errores = validar_skill(Path("modo-uno"), self.campos(description=""))
        self.assertTrue(any("falta description" in e for e in errores))

    def test_description_de_201_caracteres(self):
        errores = validar_skill(Path("modo-uno"), self.campos(description="x" * 201))
        self.assertTrue(any("description mide 201" in e for e in errores))

    def test_description_de_200_caracteres_pasa(self):
        self.assertEqual(validar_skill(Path("modo-uno"), self.campos(description="x" * 200)), [])


class BajarTitulos(unittest.TestCase):
    def test_quita_el_h1_y_baja_los_demas(self):
        salida = bajar_titulos("# Modo: algo\n\n## Uno\n\n### Dos\n")
        self.assertNotIn("# Modo", salida)
        self.assertIn("### Uno", salida)
        self.assertIn("#### Dos", salida)

    def test_no_toca_almohadillas_dentro_de_un_bloque_de_codigo(self):
        salida = bajar_titulos("## Uno\n\n```python\n# comentario\n## no es título\n```\n")
        self.assertIn("### Uno", salida)
        self.assertIn("\n# comentario", salida)
        self.assertIn("\n## no es título", salida)

    def test_respeta_bloques_con_tildes(self):
        salida = bajar_titulos("## Uno\n\n~~~text\n## adentro\n~~~\n")
        self.assertIn("### Uno", salida)
        self.assertIn("\n## adentro", salida)


class NotaBoveda(unittest.TestCase):
    def test_pone_frontmatter_y_anexo(self):
        salida = envolver_nota_boveda("# Mapa\n\ncuerpo", "[tipo/logica]", "## Avance\n")
        self.assertTrue(salida.startswith("---\ntags: [tipo/logica]\ncreado: "))
        self.assertIn("# Mapa", salida)
        self.assertTrue(salida.rstrip().endswith("## Avance"))

    def test_sin_anexo_no_agrega_nada(self):
        salida = envolver_nota_boveda("cuerpo", "[t]", None)
        self.assertTrue(salida.rstrip().endswith("cuerpo"))


class ZipReproducible(unittest.TestCase):
    def test_mismo_contenido_mismo_zip_aunque_cambie_la_mtime(self):
        with TemporaryDirectory() as tmp:
            raiz = Path(tmp)
            skill = raiz / "modo-uno"
            skill.mkdir()
            (skill / "SKILL.md").write_text("contenido", encoding="utf-8")

            escribir_zip_reproducible(raiz / "a.zip", skill)
            (skill / "SKILL.md").touch(exist_ok=True)
            import os
            os.utime(skill / "SKILL.md", (0, 0))
            escribir_zip_reproducible(raiz / "b.zip", skill)

            self.assertEqual((raiz / "a.zip").read_bytes(), (raiz / "b.zip").read_bytes())

    def test_las_rutas_van_bajo_la_carpeta_de_la_skill(self):
        with TemporaryDirectory() as tmp:
            raiz = Path(tmp)
            skill = raiz / "modo-uno"
            skill.mkdir()
            (skill / "SKILL.md").write_text("x", encoding="utf-8")
            escribir_zip_reproducible(raiz / "a.zip", skill)
            with zipfile.ZipFile(raiz / "a.zip") as z:
                self.assertEqual(z.namelist(), ["modo-uno/SKILL.md"])


if __name__ == "__main__":
    unittest.main()

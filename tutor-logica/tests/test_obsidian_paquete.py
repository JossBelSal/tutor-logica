"""Pruebas sin red, Obsidian ni archivos personales."""
import shutil
import tempfile
import unittest
from pathlib import Path

from obsidian_paquete import ARCHIVOS, generar, validar

RAIZ = Path(__file__).resolve().parents[1]

class PaqueteObsidianTests(unittest.TestCase):
    def setUp(self):
        self.temporal = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporal.cleanup)
        self.raiz = Path(self.temporal.name)
        shutil.copytree(RAIZ / "adaptadores", self.raiz / "adaptadores")

    def test_salida_completa_sin_progreso_personal(self):
        personal = self.raiz / "boveda" / "Logica" / "Logica - Bitacora.md"
        personal.parent.mkdir(parents=True)
        personal.write_text("Historia personal", encoding="utf-8")
        generar(self.raiz)
        salida = self.raiz / "listo" / "obsidian-boveda"
        encontrados = {p.relative_to(salida).as_posix() for p in salida.rglob("*") if p.is_file()}
        self.assertEqual(encontrados, set(ARCHIVOS.values()) | {"MANIFIESTO.json"})
        self.assertFalse(any("estado.md" in p or "Bitacora.md" in p or "/Conceptos/" in p
                             for p in encontrados))
        self.assertEqual(personal.read_text(encoding="utf-8"), "Historia personal")

    def test_fuente_ausente_falla_antes_de_generar(self):
        (self.raiz / "adaptadores/obsidian-boveda/AGENTS-tutor.md").unlink()
        with self.assertRaises(ValueError):
            generar(self.raiz)
        self.assertFalse((self.raiz / "listo").exists())

    def test_referencia_antigua_es_rechazada(self):
        ruta = self.raiz / "adaptadores/obsidian-boveda/skills/diagnostico-logica/SKILL.md"
        ruta.write_text(ruta.read_text(encoding="utf-8") + "\nCrear estado.md\n", encoding="utf-8")
        with self.assertRaises(ValueError):
            validar(self.raiz)

if __name__ == "__main__":
    unittest.main()

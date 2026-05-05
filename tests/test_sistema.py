"""Tests unitarios para el Sistema de Gestión de Notas."""

import pytest
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import estudiantes as mod_est
import notas as mod_notas
import promedio as mod_promedio
import archivo as mod_archivo


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture(autouse=True)
def limpiar_estado():
    """Reinicia el estado global de estudiantes antes de cada test."""
    mod_est.establecer_estudiantes({})
    yield
    mod_est.establecer_estudiantes({})


# ---------------------------------------------------------------------------
# Tests: feat/registro
# ---------------------------------------------------------------------------

class TestRegistro:
    def test_registrar_estudiante_exitoso(self):
        mod_est.registrar_estudiante("001", "Ana García")
        est = mod_est.obtener_estudiante("001")
        assert est["nombre"] == "Ana García"
        assert est["asignaturas"] == {}

    def test_registrar_id_duplicado(self):
        mod_est.registrar_estudiante("001", "Ana García")
        with pytest.raises(ValueError, match="ya existe"):
            mod_est.registrar_estudiante("001", "Otro Nombre")

    def test_registrar_campos_vacios(self):
        with pytest.raises(ValueError, match="vacíos"):
            mod_est.registrar_estudiante("", "Nombre")
        with pytest.raises(ValueError, match="vacíos"):
            mod_est.registrar_estudiante("001", "")

    def test_listar_estudiantes(self):
        mod_est.registrar_estudiante("001", "Ana")
        mod_est.registrar_estudiante("002", "Luis")
        assert len(mod_est.listar_estudiantes()) == 2


# ---------------------------------------------------------------------------
# Tests: feat/notas
# ---------------------------------------------------------------------------

class TestNotas:
    def setup_method(self):
        mod_est.registrar_estudiante("001", "Ana García")

    def test_agregar_nota_valida(self):
        mod_notas.agregar_nota("001", "Matemáticas", 4.5)
        assert mod_notas.obtener_notas("001")["Matemáticas"] == 4.5

    def test_nota_fuera_de_rango_superior(self):
        with pytest.raises(ValueError, match="entre"):
            mod_notas.agregar_nota("001", "Historia", 5.1)

    def test_nota_fuera_de_rango_inferior(self):
        with pytest.raises(ValueError, match="entre"):
            mod_notas.agregar_nota("001", "Historia", -0.1)

    def test_asignatura_vacia(self):
        with pytest.raises(ValueError, match="vacío"):
            mod_notas.agregar_nota("001", "  ", 3.0)

    def test_estudiante_inexistente(self):
        with pytest.raises(KeyError):
            mod_notas.agregar_nota("999", "Arte", 3.0)

    def test_actualizar_nota_existente(self):
        mod_notas.agregar_nota("001", "Física", 3.0)
        mod_notas.agregar_nota("001", "Física", 4.0)
        assert mod_notas.obtener_notas("001")["Física"] == 4.0


# ---------------------------------------------------------------------------
# Tests: feat/promedio
# ---------------------------------------------------------------------------

class TestPromedio:
    def setup_method(self):
        mod_est.registrar_estudiante("001", "Ana García")

    def test_promedio_sin_notas(self):
        assert mod_promedio.calcular_promedio("001") == 0.0

    def test_promedio_con_notas(self):
        mod_notas.agregar_nota("001", "Mat", 4.0)
        mod_notas.agregar_nota("001", "His", 3.0)
        assert mod_promedio.calcular_promedio("001") == 3.5

    def test_estado_aprobado(self):
        mod_notas.agregar_nota("001", "Mat", 3.5)
        assert mod_promedio.obtener_estado("001") == "Aprobado ✓"

    def test_estado_reprobado(self):
        mod_notas.agregar_nota("001", "Mat", 2.9)
        assert mod_promedio.obtener_estado("001") == "Reprobado ✗"

    def test_estado_limite_aprobacion(self):
        mod_notas.agregar_nota("001", "Mat", 3.0)
        assert mod_promedio.obtener_estado("001") == "Aprobado ✓"


# ---------------------------------------------------------------------------
# Tests: feat/archivo
# ---------------------------------------------------------------------------

class TestArchivo:
    def test_guardar_y_cargar(self, tmp_path):
        mod_est.registrar_estudiante("001", "Ana")
        mod_notas.agregar_nota("001", "Mat", 4.0)

        ruta = str(tmp_path / "test_datos.json")
        mod_archivo.guardar_datos(ruta)

        mod_est.establecer_estudiantes({})
        resultado = mod_archivo.cargar_datos(ruta)

        assert resultado is True
        est = mod_est.obtener_estudiante("001")
        assert est["nombre"] == "Ana"
        assert est["asignaturas"]["Mat"] == 4.0

    def test_cargar_archivo_inexistente(self, tmp_path):
        ruta = str(tmp_path / "no_existe.json")
        assert mod_archivo.cargar_datos(ruta) is False

    def test_cargar_json_invalido(self, tmp_path):
        ruta = str(tmp_path / "corrupto.json")
        with open(ruta, "w") as f:
            f.write("{ invalido json ]")
        with pytest.raises(ValueError, match="JSON inválido"):
            mod_archivo.cargar_datos(ruta)

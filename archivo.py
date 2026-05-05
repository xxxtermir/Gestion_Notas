"""Módulo para guardar y cargar datos de estudiantes en formato JSON."""

import json
import os
from estudiantes import listar_estudiantes, establecer_estudiantes

ARCHIVO_DATOS = "datos_estudiantes.json"


def guardar_datos(ruta: str = ARCHIVO_DATOS) -> None:
    """Guarda todos los datos de estudiantes en un archivo JSON.

    Args:
        ruta: Ruta del archivo de destino. Por defecto usa ARCHIVO_DATOS.
    """
    datos = listar_estudiantes()
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=4)
    print(f"Datos guardados en '{ruta}'.")


def cargar_datos(ruta: str = ARCHIVO_DATOS) -> bool:
    """Carga los datos de estudiantes desde un archivo JSON.

    Args:
        ruta: Ruta del archivo a leer. Por defecto usa ARCHIVO_DATOS.

    Returns:
        True si los datos se cargaron exitosamente, False si el archivo no existe.

    Raises:
        ValueError: Si el archivo JSON está corrupto o tiene formato inválido.
    """
    if not os.path.exists(ruta):
        return False
    with open(ruta, "r", encoding="utf-8") as f:
        try:
            datos = json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"El archivo '{ruta}' tiene formato JSON inválido: {e}") from e
    if not isinstance(datos, dict):
        raise ValueError("El archivo JSON no contiene un objeto válido de estudiantes.")
    establecer_estudiantes(datos)
    print(f"Datos cargados desde '{ruta}'.")
    return True

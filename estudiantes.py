"""Módulo para el registro de estudiantes."""

_estudiantes: dict = {}


def registrar_estudiante(estudiante_id: str, nombre: str) -> dict:
    """Registra un nuevo estudiante en el sistema.

    Args:
        estudiante_id: Identificador único del estudiante.
        nombre: Nombre completo del estudiante.

    Returns:
        Diccionario con los datos del estudiante registrado.

    Raises:
        ValueError: Si el ID ya existe o los campos están vacíos.
    """
    estudiante_id = estudiante_id.strip()
    nombre = nombre.strip()

    if not estudiante_id or not nombre:
        raise ValueError("El ID y el nombre no pueden estar vacíos.")
    if " " in estudiante_id:
        raise ValueError("El ID del estudiante no puede contener espacios.")
    if estudiante_id in _estudiantes:
        raise ValueError(f"El estudiante con ID '{estudiante_id}' ya existe.")

    _estudiantes[estudiante_id] = {"nombre": nombre, "asignaturas": {}}
    return _estudiantes[estudiante_id]


def obtener_estudiante(estudiante_id: str) -> dict:
    """Retorna los datos de un estudiante por su ID.

    Args:
        estudiante_id: Identificador único del estudiante.

    Returns:
        Diccionario con los datos del estudiante.

    Raises:
        KeyError: Si el estudiante no existe.
    """
    if estudiante_id not in _estudiantes:
        raise KeyError(f"Estudiante con ID '{estudiante_id}' no encontrado.")
    return _estudiantes[estudiante_id]


def listar_estudiantes() -> dict:
    """Retorna todos los estudiantes registrados."""
    return _estudiantes


def eliminar_estudiante(estudiante_id: str) -> None:
    """Elimina un estudiante del sistema por su ID.

    Args:
        estudiante_id: Identificador único del estudiante.

    Raises:
        KeyError: Si el estudiante no existe.
    """
    if estudiante_id not in _estudiantes:
        raise KeyError(f"Estudiante con ID '{estudiante_id}' no encontrado.")
    del _estudiantes[estudiante_id]


def establecer_estudiantes(datos: dict) -> None:
    """Reemplaza el estado interno con datos cargados desde archivo.

    Args:
        datos: Diccionario con los datos de todos los estudiantes.
    """
    global _estudiantes
    _estudiantes = datos

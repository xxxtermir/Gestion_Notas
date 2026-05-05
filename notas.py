"""Módulo para el ingreso y gestión de notas por asignatura."""

from estudiantes import obtener_estudiante

NOTA_MIN = 0.0
NOTA_MAX = 5.0


def agregar_nota(estudiante_id: str, asignatura: str, nota: float) -> None:
    """Ingresa o actualiza la nota de una asignatura para un estudiante.

    Args:
        estudiante_id: Identificador único del estudiante.
        asignatura: Nombre de la asignatura.
        nota: Calificación entre 0 y 5.

    Raises:
        ValueError: Si la nota está fuera del rango permitido o la asignatura está vacía.
        KeyError: Si el estudiante no existe.
    """
    asignatura = asignatura.strip()
    if not asignatura:
        raise ValueError("El nombre de la asignatura no puede estar vacío.")
    if not (NOTA_MIN <= nota <= NOTA_MAX):
        raise ValueError(f"La nota debe estar entre {NOTA_MIN} y {NOTA_MAX}.")
    nota = round(nota, 2)

    estudiante = obtener_estudiante(estudiante_id)
    estudiante["asignaturas"][asignatura] = nota


def eliminar_nota(estudiante_id: str, asignatura: str) -> None:
    """Elimina la nota de una asignatura para un estudiante.

    Args:
        estudiante_id: Identificador único del estudiante.
        asignatura: Nombre de la asignatura a eliminar.

    Raises:
        KeyError: Si el estudiante o la asignatura no existen.
    """
    asignaturas = obtener_notas(estudiante_id)
    if asignatura not in asignaturas:
        raise KeyError(f"La asignatura '{asignatura}' no existe para este estudiante.")
    del asignaturas[asignatura]


def obtener_notas(estudiante_id: str) -> dict:
    """Retorna las notas de todas las asignaturas de un estudiante.

    Args:
        estudiante_id: Identificador único del estudiante.

    Returns:
        Diccionario {asignatura: nota}.

    Raises:
        KeyError: Si el estudiante no existe.
    """
    return obtener_estudiante(estudiante_id)["asignaturas"]

"""Módulo para calcular el promedio y determinar el estado académico."""

from estudiantes import obtener_estudiante

NOTA_APROBACION = 3.0


def calcular_promedio(estudiante_id: str) -> float:
    """Calcula el promedio de notas de un estudiante.

    Args:
        estudiante_id: Identificador único del estudiante.

    Returns:
        Promedio de las notas registradas, o 0.0 si no hay asignaturas.

    Raises:
        KeyError: Si el estudiante no existe.
    """
    asignaturas = obtener_estudiante(estudiante_id)["asignaturas"]
    if not asignaturas:
        return 0.0
    return round(sum(asignaturas.values()) / len(asignaturas), 2)


def obtener_mejor_asignatura(estudiante_id: str) -> tuple[str, float] | None:
    """Retorna la asignatura con la nota más alta del estudiante.

    Args:
        estudiante_id: Identificador único del estudiante.

    Returns:
        Tupla (asignatura, nota) con la nota más alta, o None si no hay asignaturas.

    Raises:
        KeyError: Si el estudiante no existe.
    """
    asignaturas = obtener_estudiante(estudiante_id)["asignaturas"]
    if not asignaturas:
        return None
    mejor = max(asignaturas, key=lambda k: asignaturas[k])
    return mejor, asignaturas[mejor]


def obtener_estado(estudiante_id: str) -> str:
    """Determina si un estudiante está aprobado o reprobado.

    Args:
        estudiante_id: Identificador único del estudiante.

    Returns:
        'Aprobado' si el promedio es mayor o igual a NOTA_APROBACION, 'Reprobado' en caso contrario.

    Raises:
        KeyError: Si el estudiante no existe.
    """
    promedio = calcular_promedio(estudiante_id)
    return "Aprobado ✓" if promedio >= NOTA_APROBACION else "Reprobado ✗"

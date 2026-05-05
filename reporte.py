"""Módulo para generar el reporte de calificaciones en consola."""

from estudiantes import listar_estudiantes
from promedio import calcular_promedio, obtener_estado

_SEP_ANCHO = 72
_COL_ID = 12
_COL_NOMBRE = 22
_COL_ASIG = 18
_COL_PROM = 8
_COL_EST = 10


def generar_reporte() -> None:
    """Imprime en consola un reporte formateado de todos los estudiantes.

    Muestra ID, nombre, asignaturas con sus notas, promedio y estado académico.
    """
    estudiantes = listar_estudiantes()
    if not estudiantes:
        print("\nNo hay estudiantes registrados.\n")
        return

    separador = "=" * _SEP_ANCHO
    print(f"\n{separador}")
    print("  REPORTE DE CALIFICACIONES - SISTEMA DE GESTIÓN DE NOTAS")
    print(separador)
    print(
        f"  {'ID':<{_COL_ID}} {'Nombre':<{_COL_NOMBRE}} "
        f"{'Asignatura':<{_COL_ASIG}} {'Nota':>{_COL_PROM}} "
        f"{'Prom':>{_COL_PROM}} {'Estado':<{_COL_EST}}"
    )
    print("-" * _SEP_ANCHO)

    for est_id, datos in estudiantes.items():
        nombre = datos["nombre"]
        asignaturas = datos["asignaturas"]
        promedio = calcular_promedio(est_id)
        estado = obtener_estado(est_id)

        if not asignaturas:
            print(
                f"  {est_id:<{_COL_ID}} {nombre:<{_COL_NOMBRE}} "
                f"{'—':<{_COL_ASIG}} {'—':>{_COL_PROM}} "
                f"{promedio:>{_COL_PROM}.2f} {estado:<{_COL_EST}}"
            )
        else:
            items = list(asignaturas.items())
            for i, (asig, nota) in enumerate(items):
                if i == 0:
                    print(
                        f"  {est_id:<{_COL_ID}} {nombre:<{_COL_NOMBRE}} "
                        f"{asig:<{_COL_ASIG}} {nota:>{_COL_PROM}.2f} "
                        f"{promedio:>{_COL_PROM}.2f} {estado:<{_COL_EST}}"
                    )
                else:
                    print(
                        f"  {'':<{_COL_ID}} {'':<{_COL_NOMBRE}} "
                        f"{asig:<{_COL_ASIG}} {nota:>{_COL_PROM}.2f} "
                        f"{'':{_COL_PROM}} {'':<{_COL_EST}}"
                    )
        print("-" * _SEP_ANCHO)

def generar_resumen_asignaturas() -> None:
    """Imprime el promedio grupal por asignatura de todos los estudiantes."""
    estudiantes = listar_estudiantes()
    if not estudiantes:
        print("\nNo hay datos para mostrar.\n")
        return

    totales: dict[str, list[float]] = {}
    for datos in estudiantes.values():
        for asig, nota in datos["asignaturas"].items():
            totales.setdefault(asig, []).append(nota)

    separador = "=" * 40
    print(f"\n{separador}")
    print("  PROMEDIO GRUPAL POR ASIGNATURA")
    print(separador)
    for asig, notas in sorted(totales.items()):
        prom = round(sum(notas) / len(notas), 2)
        print(f"  {asig:<25} {prom:.2f}")
    print(f"{separador}\n")
        1 for eid in estudiantes if "Aprobado" in obtener_estado(eid)
    )
    reprobados = len(estudiantes) - aprobados
    print(f"\n  Total de estudiantes: {len(estudiantes)}")
    print(f"  Aprobados: {aprobados}  |  Reprobados: {reprobados}")
    print(f"{separador}\n")

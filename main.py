"""Punto de entrada principal del Sistema de Gestión de Notas."""

import sys
from estudiantes import registrar_estudiante, listar_estudiantes
from notas import agregar_nota
from promedio import calcular_promedio, obtener_estado
from reporte import generar_reporte
from archivo import guardar_datos, cargar_datos


def _input_float(mensaje: str) -> float:
    """Solicita un número flotante al usuario con validación de formato."""
    while True:
        try:
            return float(input(mensaje).strip())
        except ValueError:
            print("  Entrada inválida. Ingrese un número.")


def menu_registro() -> None:
    """Flujo para registrar un nuevo estudiante."""
    print("\n--- Registrar Estudiante ---")
    est_id = input("ID del estudiante: ").strip()
    nombre = input("Nombre completo: ").strip()
    try:
        registrar_estudiante(est_id, nombre)
        print(f"  Estudiante '{nombre}' registrado exitosamente.")
    except ValueError as e:
        print(f"  Error: {e}")


def menu_notas() -> None:
    """Flujo para ingresar una nota a un estudiante."""
    print("\n--- Ingresar Nota ---")
    est_id = input("ID del estudiante: ").strip()
    asignatura = input("Nombre de la asignatura: ").strip()
    nota = _input_float("Nota (0.0 - 5.0): ")
    try:
        agregar_nota(est_id, asignatura, nota)
        print(f"  Nota {nota:.2f} registrada en '{asignatura}'.")
    except (ValueError, KeyError) as e:
        print(f"  Error: {e}")


def menu_promedio() -> None:
    """Muestra el promedio y estado académico de un estudiante."""
    print("\n--- Consultar Promedio ---")
    est_id = input("ID del estudiante: ").strip()
    try:
        promedio = calcular_promedio(est_id)
        estado = obtener_estado(est_id)
        print(f"  Promedio: {promedio:.2f}  |  Estado: {estado}")
    except KeyError as e:
        print(f"  Error: {e}")


def menu_archivo() -> None:
    """Flujo para guardar o cargar datos desde archivo JSON."""
    print("\n--- Gestión de Archivo ---")
    print("  1. Guardar datos")
    print("  2. Cargar datos")
    opcion = input("Seleccione: ").strip()
    if opcion == "1":
        guardar_datos()
    elif opcion == "2":
        try:
            if not cargar_datos():
                print("  No se encontró archivo de datos.")
        except ValueError as e:
            print(f"  Error al cargar: {e}")
    else:
        print("  Opción inválida.")


def main() -> None:
    """Función principal que ejecuta el menú interactivo del sistema."""
    print("\n========================================")
    print("  SISTEMA DE GESTIÓN DE NOTAS")
    print("========================================")

    # Intentar cargar datos previos al iniciar
    try:
        cargar_datos()
    except (ValueError, OSError):
        pass

    opciones = {
        "1": ("Registrar estudiante", menu_registro),
        "2": ("Ingresar nota", menu_notas),
        "3": ("Consultar promedio", menu_promedio),
        "4": ("Ver reporte general", generar_reporte),
        "5": ("Guardar / Cargar datos", menu_archivo),
        "6": ("Salir", None),
    }

    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        for key, (desc, _) in opciones.items():
            print(f"  {key}. {desc}")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "6":
            guardar_datos()
            print("¡Hasta luego!\n")
            sys.exit(0)
        elif opcion in opciones:
            _, accion = opciones[opcion]
            accion()
        else:
            print("  Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    main()

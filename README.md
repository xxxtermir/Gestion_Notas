# Sistema de Gestión de Notas

Aplicación de consola en Python para gestionar calificaciones estudiantiles.

## Integrantes del grupo

| Rol | Nombre | ID |
|---|---|---|
| Tech Lead | _por definir_ | — |
| Dev Backend | _por definir_ | — |
| Dev Integración | _por definir_ | — |

## Funcionalidades

| Feature | Rama | Descripción |
|---|---|---|
| Registro | `feat/registro` | Registrar estudiante con nombre e ID |
| Notas | `feat/notas` | Ingresar notas por asignatura (0–5) |
| Promedio | `feat/promedio` | Calcular promedio y estado (aprobado/reprobado) |
| Reporte | `feat/reporte` | Reporte en consola con tabla formateada |
| Archivo | `feat/archivo` | Guardar y cargar datos en archivo `.json` |

## Requisitos

- Python 3.10 o superior
- No se requieren dependencias externas para ejecutar el sistema

Para los tests:

```bash
pip install pytest
```

## Instalación y uso

```bash
# 1. Clonar el repositorio
git clone <url-del-repositorio>
cd sistema-notas

# 2. (Opcional) Crear entorno virtual
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Linux / macOS

# 3. Ejecutar el sistema
python main.py
```

## Estructura del proyecto

```
sistema-notas/
├── main.py              # Punto de entrada y menú interactivo
├── estudiantes.py       # feat/registro
├── notas.py             # feat/notas
├── promedio.py          # feat/promedio
├── reporte.py           # feat/reporte
├── archivo.py           # feat/archivo
├── tests/
│   └── test_sistema.py  # Tests unitarios con pytest
├── .github/
│   └── workflows/
│       └── ci.yml       # CI/CD con GitHub Actions
├── .gitignore
└── README.md
```

## Ejecutar tests

```bash
pytest tests/ -v
```

## CI/CD

El repositorio incluye un workflow de GitHub Actions (`.github/workflows/ci.yml`) que ejecuta los tests automáticamente en cada push y pull request contra `main`, sobre Python 3.10, 3.11 y 3.12.

## Flujo de trabajo Git

```bash
# Nunca trabajar directo en main — siempre crear una rama
git checkout -b feat/nombre-feature

# Commits pequeños y descriptivos
git add .
git commit -m "feat: descripción clara del cambio"

# Subir la rama y crear Pull Request
git push origin feat/nombre-feature
```

> **Regla de oro:** nunca hacer `push` directo a `main`.

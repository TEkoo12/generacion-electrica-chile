"""Funciones de carga y revisión inicial de los datos de generación bruta mensual."""

import pandas as pd


def cargar_datos(ruta: str) -> pd.DataFrame:
    """Carga el archivo CSV y devuelve un DataFrame sin transformar."""
    return pd.read_csv(ruta)


def revisar_estructura(datos: pd.DataFrame) -> None:
    """Muestra dimensiones, columnas, tipos, primeros registros, nulos y duplicados."""
    print("Dimensiones:", datos.shape)
    print("Columnas:", datos.columns.tolist())

    print("\nTipos de datos originales:")
    print(datos.dtypes)

    print("\nPrimeros cinco registros:")
    print(datos.head())

    print("\nValores nulos:")
    print(datos.isna().sum())

    print("\nFilas duplicadas:", datos.duplicated().sum())


def convertir_tipos(datos: pd.DataFrame) -> pd.DataFrame:
    """Convierte fecha a datetime y generación a numérico (inválidos pasan a NaN)."""
    datos = datos.copy()
    datos["fecha"] = pd.to_datetime(datos["fecha"], format="%Y-%m", errors="coerce")
    datos["generacion_bruta_gwh"] = pd.to_numeric(
        datos["generacion_bruta_gwh"], errors="coerce"
    )
    return datos


def revisar_calidad(datos: pd.DataFrame) -> None:
    """Revisa fechas inválidas o repetidas, valores negativos o iguales a cero."""
    print("\nFechas inválidas:", datos["fecha"].isna().sum())
    print("Fechas repetidas:", datos["fecha"].duplicated().sum())
    print("Valores negativos:", (datos["generacion_bruta_gwh"] < 0).sum())
    print("Valores iguales a cero:", (datos["generacion_bruta_gwh"] == 0).sum())


def resumen_estadistico(datos: pd.DataFrame) -> None:
    """Muestra el resumen estadístico de la generación bruta mensual."""
    print("\nResumen estadístico:")
    print(datos["generacion_bruta_gwh"].describe())

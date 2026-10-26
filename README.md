# Datos

Esta carpeta debe contener el archivo `generacion_bruta_mensual.csv`.

## Descripción

| Campo | Detalle |
|---|---|
| Archivo | `generacion_bruta_mensual.csv` |
| Columnas | `fecha` (formato AAAA-MM), `generacion_bruta_gwh` (GWh) |
| Período | Enero de 2018 a septiembre de 2026 |
| Frecuencia | Mensual |
| Registros | 105 filas |

## Cómo obtenerlo

1. Entrar al portal Energía Abierta de la Comisión Nacional de Energía (CNE), sección Electricidad:
   https://energiaabierta.cl/categorias-estadistica/electricidad/
2. Descargar el conjunto de datos de generación bruta de energía eléctrica (fecha de descarga utilizada en el proyecto: 23-10-2026).
3. Preparar un CSV con solo dos columnas, `fecha` (AAAA-MM) y `generacion_bruta_gwh`, con un registro por mes.
4. Guardarlo como `datos/generacion_bruta_mensual.csv`.

> Si el archivo ya está en este repositorio, no es necesario repetir estos pasos.

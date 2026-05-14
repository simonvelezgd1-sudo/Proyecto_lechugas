# Proyecto_lechugas
Proyecto de  cultivos de lechugas de estados unidos, graficacion y analisis de datos en enfoque empresarial.
# Análisis de Variables Ambientales en el Crecimiento de la Lechuga (Lactuca sativa)

## 📌 Descripción del Proyecto
Este proyecto analiza el impacto de factores como el pH, la temperatura y los nutrientes en el crecimiento de cultivos de lechuga. El objetivo es identificar los rangos óptimos para maximizar la productividad agrícola mediante un enfoque de ingeniería de datos.

##  Stack Tecnológico
*   **Base de Datos:** SQL Server.
*   **Infraestructura:** Docker (Contenedores para persistencia de datos).
*   **Lenguaje:** Python 3.x.
*   **Librerías principales:** Pandas (Limpieza), Matplotlib/Seaborn (Visualización).

##  Arquitectura del Proyecto
1.  **Ingesta:** Los datos fueron extraídos de un dataset de Kaggle.
2.  **Infraestructura:** Se configuró un contenedor de SQL Server mediante **Docker** para la gestión robusta de los datos.
3.  **Procesamiento:** Limpieza de datos (Data Cleaning) y transformación utilizando Python.
4.  **Análisis SQL:** Ejecución de queries para segmentar el crecimiento por niveles de pH y temperatura.

##  Hallazgos Clave
*   El pH óptimo para el crecimiento acelerado se identificó entre **[Insertar dato, ej: 6.0 y 7.0]**.
*   Se observó una correlación positiva entre la temperatura estable y el desarrollo foliar.

##  Cómo ejecutar el proyecto
1. Levantar el contenedor: `docker-compose up -d`
2. Ejecutar el notebook de limpieza: `python scripts/limpieza.py`
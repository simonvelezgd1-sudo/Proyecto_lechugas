# Proyecto_lechugas
Proyecto de cultivos de lechugas de estados unidos, graficacion y analisis de datos en enfoque empresarial.

# Análisis de Variables Ambientales en el Crecimiento de la Lechuga (Lactuca sativa)

## 📌 Descripción del Proyecto
Este proyecto analiza el impacto de factores como el pH, la temperatura y los nutrientes en el crecimiento de cultivos de lechuga. El objetivo es identificar los rangos óptimos para maximizar la productividad y proporcionar recomendaciones empresariales basadas en datos.

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

## 🔬 Hallazgos Críticos

### 🌡️ Temperatura (Factor Limitante Principal)
- **Rango Óptimo:** 22°C (crecimiento en 17 días - etapa más productiva)
- **Umbral de Colapso:** >32°C (cultivos colapsan después de esta temperatura)
- **Impacto del Estrés Térmico:** Retraso de hasta **30%** en el crecimiento de cultivos
- **Comportamiento:** Se registran picos muy altos en crecimiento con temperaturas medias entre 18-24°C, con decadencia progresiva conforme aumenta la temperatura

### 💧 Análisis Humedad-Temperatura (Punto de Inflexión Crítico)
- **Hallazgo Inusual:** Diferencia de 6 días de crecimiento entre humedad del 74% (19 días) vs 73% (25 días)
- **Correlación Identificada:** Incremento de 1% en temperatura atrofia significativamente el crecimiento
- **Conclusión:** La fluctuación térmica genera estrés en la planta, independientemente de cambios mínimos en humedad
- **Rango Crítico:** Humedad 73-74% con variación de temperatura ±1°C

### pH y Nutrientes
- **Independencia Térmica:** El nivel de pH es independiente a la temperatura
- **Rango Ideal TDS/PPM:** Los nutrientes disueltos están en su rango ideal, proporcionando parámetros óptimos de absorción
- **Observación:** Niveles elevados de pH pueden afectar la absorción de nutrientes (TDS/PPM)

## 📊 Recomendaciones Empresariales

### Control de Clima Crítico
1. Mantener temperatura constante en **22°C** para máxima productividad
2. Evitar variaciones bruscas de temperatura superiores a ±1°C
3. Implementar alertas automáticas si temperatura excede 30°C
4. Monitoreo continuo de humedad en rango 73-74%

### Optimización de Infraestructura
- Invertir en sistemas de control climático de precisión
- Validar resultados con múltiples ciclos de cultivo
- Generar reportes SQL comparativos por temporada

##  Cómo ejecutar el proyecto
1. Levantar el contenedor: `docker-compose up -d`
2. Ejecutar el notebook de limpieza: `python scripts/limpieza.py`

## 📈 Próximas Mejoras
- Integrar análisis de datos en tiempo real
- Crear dashboard interactivo para monitoreo de variables
- Automatizar alertas basadas en umbrales críticos identificados

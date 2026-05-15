# 🚀 Guía de Ejecución - Proyecto Lechugas

## 📋 Requisitos Previos

### Sistema Operativo
- **Windows 10+**, macOS 10.14+, o **Linux (Recomendado)**
- 2GB RAM mínimo
- 500MB de espacio en disco

### Software Requerido
- **Python 3.7+** (recomendado 3.9 o superior)
- **pip** (gestor de paquetes de Python)
- **Git** (para clonar el repositorio)

---

## 📥 Paso 1: Clonar el Repositorio

### Opción A: Desde GitHub (Recomendado)

```bash
# Clonar el repositorio completo
git clone https://github.com/simonvelezgd1-sudo/Proyecto_lechugas.git

# Entrar al directorio
cd Proyecto_lechugas

# Verificar estructura
ls -la
```

### Opción B: Descargar ZIP
1. Ir a: https://github.com/simonvelezgd1-sudo/Proyecto_lechugas
2. Hacer clic en `Code` → `Download ZIP`
3. Extraer el archivo descargado

---

## 🔧 Paso 2: Configurar el Entorno de Python

### 2A. Crear Entorno Virtual (Recomendado)

```bash
# En Windows
python -m venv venv
venv\Scripts\activate

# En macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 2B. Verificar Instalación de Python

```bash
# Verificar versión de Python
python --version

# Verificar pip
pip --version
```

---

## 📦 Paso 3: Instalar Dependencias

### Opción A: Instalación Rápida (Recomendada)

```bash
# Instalar todos los paquetes requeridos
pip install pandas matplotlib seaborn numpy scipy scikit-learn

# Verificación
pip list
```

### Opción B: Desde requirements.txt (Si existe)

```bash
# Si existe archivo requirements.txt
pip install -r requirements.txt
```

### Paquetes Instalados

```
pandas          2.0+      # Manipulación de datos
matplotlib      3.5+      # Gráficas estáticas
seaborn         0.12+     # Visualizaciones estadísticas
numpy           1.23+     # Cálculos numéricos
scipy           1.9+      # Estadística avanzada
scikit-learn    1.2+      # Machine Learning (opcional)
```

---

## ▶️ Paso 4: Ejecutar el Script de Visualización

### Ejecución Básica

```bash
# Desde el directorio raíz del proyecto
python generate_visualizations.py
```

### Salida Esperada

```
======================================================================
GENERADOR DE REPORTES VISUALES - PROYECTO LECHUGAS
======================================================================

✓ Datos cargados: 990 registros
✓ Plantas analizadas: 22

✓ Gráfica 1 guardada: 01_temperatura_vs_crecimiento.png
✓ Gráfica 2 guardada: 02_ph_vs_crecimiento.png
✓ Gráfica 3 guardada: 03_humedad_temperatura_heatmap.png
✓ Gráfica 4 guardada: 04_tds_vs_crecimiento.png
✓ Gráfica 5 guardada: 05_distribucion_temperatura.png
✓ Gráfica 6 guardada: 06_matriz_correlacion.png

======================================================================
ESTADÍSTICAS GENERALES DEL DATASET
======================================================================
  • Temperatura Promedio: 30.12°C
  • Temperatura Mínima: 20.10°C
  • Temperatura Máxima: 33.50°C
  • pH Promedio: 6.35
  • pH Rango: 6.00 - 6.80
  • Humedad Promedio: 64.42%
  • Crecimiento Promedio: 24.23 días
  • Crecimiento Máximo: 47 días
  • TDS/PPM Promedio: 601.34 ppm

======================================================================
CORRELACIONES MÁS IMPORTANTES CON CRECIMIENTO
======================================================================
  • temp_c: -0.512 (Fuerte negativa)
  • humedad: 0.284 (Moderada positiva)
  • ph_nivel: 0.087 (Débil positiva)
  • tds_ppm: -0.031 (Débil negativa)

======================================================================
✓ PROCESO FINALIZADO EXITOSAMENTE
✓ Todas las gráficas han sido guardadas en el directorio 'reportes/'
======================================================================
```

---

## 📂 Paso 5: Ubicar los Reportes Generados

### Estructura de Carpetas

```
Proyecto_lechugas/
├── reportes/                           # Carpeta con gráficas
│   ├── 01_temperatura_vs_crecimiento.png
│   ├── 02_ph_vs_crecimiento.png
│   ├── 03_humedad_temperatura_heatmap.png
│   ├── 04_tds_vs_crecimiento.png
│   ├── 05_distribucion_temperatura.png
│   └── 06_matriz_correlacion.png
├── Proyecto-analisis-lechugas/
│   └── data/scripts/
│       ├── lettuce_dataset_updated.csv  # Datos source
│       ├── limpieza.py                  # Script original
│       └── consultas.sql                # Queries SQL
├── generate_visualizations.py           # Script principal
├── VISUALIZACIONES_REPORT.md            # Este archivo
├── GUIA_EJECUCION.md                    # Manual de uso
└── README.md
```

---

## 🖥️ Paso 6: Ver y Exportar Gráficas

### En Windows
```bash
# Abrir carpeta de reportes
explorer reportes

# O abrir imagen específica
start reportes/01_temperatura_vs_crecimiento.png
```

### En macOS
```bash
# Abrir carpeta
open reportes

# O abrir imagen específica
open reportes/01_temperatura_vs_crecimiento.png
```

### En Linux
```bash
# Abrir carpeta
nautilus reportes  # Gnome
dolphin reportes   # KDE

# O abrir imagen específica
eog reportes/01_temperatura_vs_crecimiento.png
```

---

## 🔧 Solución de Problemas

### ❌ Error: "Python no encontrado"

```bash
# Solución: Usar python3 en lugar de python
python3 generate_visualizations.py

# O verificar PATH
where python      # Windows
which python      # macOS/Linux
```

### ❌ Error: "ModuleNotFoundError: No module named 'pandas'"

```bash
# Solución: Instalar pandas
pip install pandas

# O reinstalar todos los paquetes
pip install --upgrade pandas matplotlib seaborn numpy
```

### ❌ Error: "FileNotFoundError: lettuce_dataset_updated.csv"

```bash
# Verificar que el CSV existe
ls Proyecto-analisis-lechugas/data/scripts/

# Si no existe, descargarlo nuevamente del repositorio
git pull origin main
```

### ❌ Error: "Permission denied" en Linux/macOS

```bash
# Hacer script ejecutable
chmod +x generate_visualizations.py

# O ejecutar con python explícitamente
python3 generate_visualizations.py
```

### ⚠️ Advertencia: "FutureWarning" o "DeprecationWarning"

```
Esto es NORMAL y se puede ignorar. Indica que se usarán
cambios en futuras versiones. No afecta la funcionalidad.
```

---

## 📊 Personalización del Script

### Modificar Colores

```python
# En generate_visualizations.py, línea ~45
cmap='RdYlGn_r'  # Cambiar a: 'viridis', 'plasma', 'inferno'
```

### Cambiar Resolución de Salida

```python
# Línea ~65
plt.savefig(..., dpi=300, ...)  # Cambiar 300 a 150, 600, etc.
# 150 DPI = Rápido (web)
# 300 DPI = Estándar (impresión)
# 600 DPI = Alta (publicación)
```

### Agregar Filtros de Datos

```python
# Al inicio del script, después de cargar df_clean
# Solo plantas con temperatura óptima
df_clean = df_clean[(df_clean['temp_c'] >= 20) & (df_clean['temp_c'] <= 25)]
```

### Generar Gráficas Adicionales

```python
# Agregar al final del script
fig, ax = plt.subplots(figsize=(12, 7))
ax.hist(df_clean['dias_crecimiento'], bins=30, color='skyblue', edgecolor='black')
ax.set_xlabel('Días de Crecimiento')
ax.set_ylabel('Frecuencia')
ax.set_title('Distribución de Días de Crecimiento')
plt.savefig('reportes/07_distribucion_crecimiento.png', dpi=300, bbox_inches='tight')
plt.close()
```

---

## 🔄 Automatización (Opcional)

### Ejecutar Diariamente (Windows - Programador de Tareas)

```batch
# Crear archivo run_daily.bat
@echo off
cd C:\ruta\a\Proyecto_lechugas
python generate_visualizations.py
pause
```

Luego en Programador de Tareas:
1. Crear Tarea Básica
2. Ejecutar: `C:\ruta\a\run_daily.bat`
3. Frecuencia: Diaria a las 6:00 AM

### Ejecutar Diariamente (Linux/macOS - Cron)

```bash
# Editar crontab
crontab -e

# Agregar línea:
0 6 * * * cd /ruta/a/Proyecto_lechugas && python3 generate_visualizations.py
```

---

## 📈 Próximos Pasos

### 1. Análisis Temporal
```bash
python análisis_temporal.py  # (próximamente)
```

### 2. Predicción con Machine Learning
```bash
python predictor_ml.py  # (próximamente)
```

### 3. Dashboard Interactivo
```bash
streamlit run dashboard.py  # (próximamente)
```

### 4. Integración con Base de Datos
```bash
python sync_sql_server.py  # (próximamente)
```

---

## 💡 Tips y Mejores Prácticas

### ✅ Recomendaciones

- ✓ Crear carpeta `reportes/` antes de ejecutar
- ✓ Usar entorno virtual para evitar conflictos
- ✓ Ejecutar mensualmente para detectar tendencias
- ✓ Guardar gráficas con fecha: `backup_2026-05-15/`
- ✓ Documentar cambios en parámetros
- ✓ Mantener backup del CSV original

### ❌ Evitar

- ✗ Editar el CSV sin respaldo
- ✗ Cambiar nombres de columnas
- ✗ Ejecutar script en carpeta protegida (Program Files)
- ✗ Usar Python sin entorno virtual en producción
- ✗ Ignorar warnings (podrían ser errores futuros)

---

## 📞 Soporte y Contacto

### Recursos
- **Documentación:** [README.md](README.md)
- **Informe Detallado:** [VISUALIZACIONES_REPORT.md](VISUALIZACIONES_REPORT.md)
- **Código Fuente:** [generate_visualizations.py](generate_visualizations.py)

### Reportar Errores
1. Verificar todos los pasos de esta guía
2. Ejecutar con `python -u` para debug verboso
3. Copiar el error completo en GitHub Issues

### Preguntas Frecuentes

**P: ¿Cuánto tiempo toma ejecutarse?**  
R: 30-60 segundos con dataset completo

**P: ¿Necesito actualizar datos manualmente?**  
R: No. El script lee automáticamente el CSV más reciente

**P: ¿Se pueden exportar a PDF?**  
R: Sí. Cambiar `.png` por `.pdf` en línea 65

**P: ¿Qué hacer si falta el archivo CSV?**  
R: Ejecutar `git pull` para sincronizar repositorio

---

## 📚 Referencias Técnicas

### Paquetes Utilizados
- **pandas:** Manipulación de datos tabulares
- **matplotlib:** Visualización base
- **seaborn:** Análisis estadístico visual
- **numpy:** Cálculos numéricos

### Métodos Utilizados
- Scatter Plots: Relaciones entre variables
- Heatmaps: Distribuciones multidimensionales
- Boxplots: Análisis de cuartiles
- Correlación de Pearson: Fuerza de relaciones

---

**Última actualización:** 2026-05-15  
**Versión:** 1.0  
**Autor:** Equipo Proyecto Lechugas  
**Licencia:** MIT

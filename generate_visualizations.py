import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pathlib import Path

# Configurar estilo
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (16, 10)
plt.rcParams['font.size'] = 11

# Crear directorio de reportes
Path("reportes").mkdir(exist_ok=True)

# Leer datos
df = pd.read_csv('Proyecto-analisis-lechugas/data/scripts/lettuce_dataset_updated.csv')

# Renombrar columnas para facilitar uso
df_clean = df.rename(columns={
    'Temperature (°C)': 'temp_c',
    'Humidity (%)': 'humedad',
    'pH Level': 'ph_nivel',
    'Growth Days': 'dias_crecimiento',
    'TDS Value (ppm)': 'tds_ppm'
})

print("=" * 70)
print("GENERADOR DE REPORTES VISUALES - PROYECTO LECHUGAS")
print("=" * 70)
print(f"\n✓ Datos cargados: {len(df_clean)} registros")
print(f"✓ Plantas analizadas: {df_clean['Plant_ID'].nunique()}")

# ============================================================================
# GRÁFICA 1: Temperatura vs Crecimiento (SCATTER)
# ============================================================================
fig, ax = plt.subplots(figsize=(12, 7))
scatter = ax.scatter(df_clean['temp_c'], df_clean['dias_crecimiento'], 
                     c=df_clean['humedad'], cmap='RdYlGn_r', 
                     alpha=0.6, s=100, edgecolors='black', linewidth=0.5)

# Añadir línea de referencia en 22°C (óptima)
ax.axvline(x=22, color='green', linestyle='--', linewidth=2, label='Óptimo: 22°C', alpha=0.7)
ax.axvline(x=32, color='red', linestyle='--', linewidth=2, label='Umbral crítico: 32°C', alpha=0.7)

ax.set_xlabel('Temperatura (°C)', fontsize=12, fontweight='bold')
ax.set_ylabel('Días de Crecimiento', fontsize=12, fontweight='bold')
ax.set_title('Impacto de la Temperatura en el Crecimiento de Lechugas\n(Colores indican nivel de humedad)', 
             fontsize=14, fontweight='bold', pad=20)
ax.grid(True, alpha=0.3)
ax.legend(fontsize=10, loc='upper right')

# Colorbar
cbar = plt.colorbar(scatter, ax=ax)
cbar.set_label('Humedad (%)', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig('reportes/01_temperatura_vs_crecimiento.png', dpi=300, bbox_inches='tight')
print("\n✓ Gráfica 1 guardada: 01_temperatura_vs_crecimiento.png")
plt.close()

# ============================================================================
# GRÁFICA 2: pH vs Crecimiento (SCATTER con zonas ideales)
# ============================================================================
fig, ax = plt.subplots(figsize=(12, 7))
scatter = ax.scatter(df_clean['ph_nivel'], df_clean['dias_crecimiento'], 
                     c=df_clean['temp_c'], cmap='coolwarm', 
                     alpha=0.6, s=100, edgecolors='black', linewidth=0.5)

# Zonas de pH ideal
ax.axvspan(5.5, 6.5, alpha=0.2, color='green', label='Rango Ideal (5.5-6.5)')
ax.axvline(x=5.5, color='darkgreen', linestyle='--', linewidth=1.5, alpha=0.7)
ax.axvline(x=6.5, color='darkgreen', linestyle='--', linewidth=1.5, alpha=0.7)

ax.set_xlabel('Nivel de pH', fontsize=12, fontweight='bold')
ax.set_ylabel('Días de Crecimiento', fontsize=12, fontweight='bold')
ax.set_title('Impacto del pH en el Crecimiento de Lechugas\n(Colores indican temperatura)', 
             fontsize=14, fontweight='bold', pad=20)
ax.grid(True, alpha=0.3)
ax.legend(fontsize=10, loc='upper right')

# Colorbar
cbar = plt.colorbar(scatter, ax=ax)
cbar.set_label('Temperatura (°C)', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig('reportes/02_ph_vs_crecimiento.png', dpi=300, bbox_inches='tight')
print("✓ Gráfica 2 guardada: 02_ph_vs_crecimiento.png")
plt.close()

# ============================================================================
# GRÁFICA 3: Humedad vs Temperatura (HEATMAP)
# ============================================================================
fig, ax = plt.subplots(figsize=(14, 8))

# Crear tabla de pivote para heatmap
temp_bins = pd.cut(df_clean['temp_c'], bins=8)
humedad_bins = pd.cut(df_clean['humedad'], bins=8)
pivot_table = pd.crosstab(humedad_bins, temp_bins, values=df_clean['dias_crecimiento'], aggfunc='mean')

sns.heatmap(pivot_table, annot=True, fmt='.1f', cmap='RdYlGn', 
            cbar_kws={'label': 'Promedio de Días de Crecimiento'},
            ax=ax, linewidths=0.5)

ax.set_xlabel('Rango de Temperatura (°C)', fontsize=12, fontweight='bold')
ax.set_ylabel('Rango de Humedad (%)', fontsize=12, fontweight='bold')
ax.set_title('Matriz de Crecimiento: Temperatura vs Humedad\n(Valores = Promedio de días de crecimiento)', 
             fontsize=14, fontweight='bold', pad=20)
plt.xticks(rotation=45)
plt.yticks(rotation=0)
plt.tight_layout()
plt.savefig('reportes/03_humedad_temperatura_heatmap.png', dpi=300, bbox_inches='tight')
print("✓ Gráfica 3 guardada: 03_humedad_temperatura_heatmap.png")
plt.close()

# ============================================================================
# GRÁFICA 4: TDS/Nutrientes vs Crecimiento
# ============================================================================
fig, ax = plt.subplots(figsize=(12, 7))
scatter = ax.scatter(df_clean['tds_ppm'], df_clean['dias_crecimiento'], 
                     c=df_clean['temp_c'], cmap='viridis', 
                     alpha=0.6, s=100, edgecolors='black', linewidth=0.5)

ax.set_xlabel('TDS/PPM (Nutrientes disueltos)', fontsize=12, fontweight='bold')
ax.set_ylabel('Días de Crecimiento', fontsize=12, fontweight='bold')
ax.set_title('Impacto de Nutrientes (TDS/PPM) en el Crecimiento\n(Colores indican temperatura)', 
             fontsize=14, fontweight='bold', pad=20)
ax.grid(True, alpha=0.3)

# Colorbar
cbar = plt.colorbar(scatter, ax=ax)
cbar.set_label('Temperatura (°C)', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig('reportes/04_tds_vs_crecimiento.png', dpi=300, bbox_inches='tight')
print("✓ Gráfica 4 guardada: 04_tds_vs_crecimiento.png")
plt.close()

# ============================================================================
# GRÁFICA 5: Distribución de Crecimiento por Rango de Temperatura
# ============================================================================
fig, ax = plt.subplots(figsize=(14, 8))

# Crear rangos de temperatura
df_clean['temp_rango'] = pd.cut(df_clean['temp_c'], 
                                bins=[0, 18, 22, 25, 32, 40],
                                labels=['< 18°C', '18-22°C', '22-25°C', '25-32°C', '> 32°C'])

# Crear boxplot
df_clean.boxplot(column='dias_crecimiento', by='temp_rango', ax=ax)
ax.set_xlabel('Rango de Temperatura', fontsize=12, fontweight='bold')
ax.set_ylabel('Días de Crecimiento', fontsize=12, fontweight='bold')
ax.set_title('Distribución del Crecimiento por Rango de Temperatura', 
             fontsize=14, fontweight='bold', pad=20)
plt.suptitle('')  # Remover título automático
ax.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('reportes/05_distribucion_temperatura.png', dpi=300, bbox_inches='tight')
print("✓ Gráfica 5 guardada: 05_distribucion_temperatura.png")
plt.close()

# ============================================================================
# GRÁFICA 6: Correlación entre variables
# ============================================================================
fig, ax = plt.subplots(figsize=(10, 8))

# Seleccionar columnas numéricas
cols = ['temp_c', 'humedad', 'ph_nivel', 'tds_ppm', 'dias_crecimiento']
corr_matrix = df_clean[cols].corr()

sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', 
            center=0, vmin=-1, vmax=1, square=True, ax=ax,
            cbar_kws={'label': 'Coeficiente de Correlación'})

ax.set_title('Matriz de Correlación: Variables Ambientales vs Crecimiento', 
             fontsize=14, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig('reportes/06_matriz_correlacion.png', dpi=300, bbox_inches='tight')
print("✓ Gráfica 6 guardada: 06_matriz_correlacion.png")
plt.close()

# ============================================================================
# ESTADÍSTICAS GENERALES
# ============================================================================
print("\n" + "=" * 70)
print("ESTADÍSTICAS GENERALES DEL DATASET")
print("=" * 70)

stats = {
    'Temperatura Promedio': f"{df_clean['temp_c'].mean():.2f}°C",
    'Temperatura Mínima': f"{df_clean['temp_c'].min():.2f}°C",
    'Temperatura Máxima': f"{df_clean['temp_c'].max():.2f}°C",
    'pH Promedio': f"{df_clean['ph_nivel'].mean():.2f}",
    'pH Rango': f"{df_clean['ph_nivel'].min():.2f} - {df_clean['ph_nivel'].max():.2f}",
    'Humedad Promedio': f"{df_clean['humedad'].mean():.2f}%",
    'Crecimiento Promedio': f"{df_clean['dias_crecimiento'].mean():.2f} días",
    'Crecimiento Máximo': f"{df_clean['dias_crecimiento'].max():.0f} días",
    'TDS/PPM Promedio': f"{df_clean['tds_ppm'].mean():.2f} ppm"
}

for key, value in stats.items():
    print(f"  • {key}: {value}")

# ============================================================================
# Correlación destacada
# ============================================================================
print("\n" + "=" * 70)
print("CORRELACIONES MÁS IMPORTANTES CON CRECIMIENTO")
print("=" * 70)

corr_with_growth = corr_matrix['dias_crecimiento'].sort_values(ascending=False)
for var, corr_val in corr_with_growth.items():
    if var != 'dias_crecimiento':
        strength = "Fuerte" if abs(corr_val) > 0.5 else "Moderada" if abs(corr_val) > 0.3 else "Débil"
        direction = "positiva" if corr_val > 0 else "negativa"
        print(f"  • {var}: {corr_val:.3f} ({strength} {direction})")

print("\n" + "=" * 70)
print("✓ PROCESO FINALIZADO EXITOSAMENTE")
print("✓ Todas las gráficas han sido guardadas en el directorio 'reportes/'")
print("=" * 70 + "\n")

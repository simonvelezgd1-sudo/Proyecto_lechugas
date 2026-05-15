imimport pandas as pd
import matplotlib.pyplot as plt
import glob
import os


archivos_csv = glob.glob('*.csv')

print(f"--- PROCESADOR AUTOMÁTICO DE CULTIVOS ---")
print(f"Archivos detectados: {len(archivos_csv)}\n")

for archivo in archivos_csv:
    try:
        
        df = pd.read_csv(archivo)
        
        
        columnas_nuevas = {
            'temperature_c': 'temp_c',
            'dias de crecimiento': 'dias_crecimiento',
            'ph': 'ph_nivel',
            'nivel_ph': 'ph_nivel'
        }
        df = df.rename(columns=columnas_nuevas)
        
        
        columnas_requeridas = ['temp_c', 'ph_nivel', 'dias_crecimiento']
        if not all(col in df.columns for col in columnas_requeridas):
            print(f"[!] Saltando {archivo}: No tiene las columnas necesarias.")
            continue

        
        df = df.dropna()

        
        print(f"Analizando: {archivo}")
        print(f"   - Registros: {len(df)}")
        print(f"   - Temperatura Promedio: {df['temp_c'].mean():.2f}°C")
        print(f"   - pH Promedio: {df['ph_nivel'].mean():.2f}")

        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
        fig.suptitle(f'Reporte de Análisis: {archivo}', fontsize=16)

        
        ax1.scatter(df['temp_c'], df['dias_crecimiento'], alpha=0.4, color='seagreen')
        ax1.set_title('Temperatura vs Crecimiento')
        ax1.set_xlabel('Temperatura (°C)')
        ax1.set_ylabel('Días')
        ax1.grid(True, alpha=0.3)

        
        ax2.scatter(df['ph_nivel'], df['dias_crecimiento'], alpha=0.4, color='royalblue')
        ax2.axvline(x=5.5, color='red', linestyle='--', label='Min Ideal')
        ax2.axvline(x=6.5, color='red', linestyle='--', label='Max Ideal')
        ax2.set_title('Nivel de pH vs Crecimiento')
        ax2.set_xlabel('pH')
        ax2.grid(True, alpha=0.3)

        
        nombre_salida = f"REPORTE_{archivo.replace('.csv', '.png')}"
        plt.tight_layout(rect=[0, 0.03, 1, 0.95]) 
        plt.savefig("/home/velez/proyecto_lechugas_python/REPORTES/" + nombre_salida)
        plt.close()
        
        print(f"   [OK] Reporte guardado: {nombre_salida}\n")

    except Exception as e:
        print(f"   [X] Error procesando {archivo}: {e}\n")

print("--- PROCESO FINALIZADO ---")



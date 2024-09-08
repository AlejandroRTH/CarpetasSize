import os
import pandas as pd

def get_folder_size(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if os.path.isfile(fp):
                total_size += os.path.getsize(fp)
    return total_size

def analyze_folder_structure(root_folder):
    folder_data = []
    for dirpath, dirnames, filenames in os.walk(root_folder):
        print(f"\rProcesando carpeta: {dirpath}", end='')  # Mostrar la carpeta en la que se está trabajando
        folder_size = get_folder_size(dirpath)
        folder_data.append({
            "Carpeta": dirpath,
            "Tamaño (Bytes)": folder_size
        })
    
    df = pd.DataFrame(folder_data)
    df['Tamaño (MB)'] = df['Tamaño (Bytes)'] / (1024 * 1024)
    df['Tamaño (GB)'] = df['Tamaño (MB)'] / 1024

    # Formatear las columnas de MB y GB a dos decimales
    df['Tamaño (MB)'] = df['Tamaño (MB)'].map('{:.2f}'.format)
    df['Tamaño (GB)'] = df['Tamaño (GB)'].map('{:.2f}'.format)

    return df

# Ruta a la carpeta que deseas analizar
root_folder = r"C:\ProgramData\Microsoft\VisualStudio\Packages"  # Cambia esto a la ruta de la carpeta que deseas analizar

# Análisis de la carpeta
df = analyze_folder_structure(root_folder)

# Mostrar el DataFrame
print("\nAnálisis completo. Resultados:")
print(df)

# Intentar guardar en archivo Excel con manejo de errores
try:
    df.to_excel("Folder_Size.xlsx", index=False)
    print("\nArchivo Excel 'Folder_Size.xlsx' creado exitosamente.")
except Exception as e:
    print(f"\nError al crear el archivo Excel: {e}")

import os
import pandas as pd
from funciones import clscr

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
    
    # Obtener las carpetas del nivel raíz
    root_subfolders = [os.path.join(root_folder, d) for d in os.listdir(root_folder) if os.path.isdir(os.path.join(root_folder, d))]

    # Filtrar las carpetas que superan los 5 GB
    large_folders = []
    for folder in root_subfolders:
        folder_size = get_folder_size(folder)
        if folder_size > 5 * 1024 * 1024 * 1024:  # 5 GB en bytes
            large_folders.append(folder)
    
    # Analizar solo las carpetas grandes
    for folder in large_folders:
        # Truncar la ruta si es demasiado larga (e.g., más de 80 caracteres)
        short_path = (folder[:75]) if len(folder) > 75 else folder
        
        folder_size = get_folder_size(folder)
        # Mostrar la carpeta en la que se está trabajando y actualizar en una sola línea
        print(f"Procesando carpeta: {short_path} ... {folder_size}")
        # print(f"\rProcesando carpeta: {short_path} {folder_size}", end='', flush=True)
        
        # Analizar las subcarpetas de las carpetas grandes
        for dirpath, dirnames, filenames in os.walk(folder):
            # Truncar la ruta si es demasiado larga (e.g., más de 80 caracteres)
            short_path = (dirpath[:75]) if len(dirpath) > 75 else dirpath
            
            folder_size = get_folder_size(dirpath)
            # Mostrar la carpeta en la que se está trabajando y actualizar en una sola línea
            print(f"Procesando subcarpeta: {short_path} ... {folder_size}")
            # print(f"\rProcesando subcarpeta: {short_path} {folder_size}", end='', flush=True)
            folder_data.append({
                "Carpeta": dirpath,
                "Tamaño (Bytes)": folder_size
            })
    
    df = pd.DataFrame(folder_data)

    df['Tamaño (MB)'] = df['Tamaño (Bytes)'] / (1024 * 1024)
    df['Tamaño (GB)'] = df['Tamaño (MB)'] / 1024

    return df

clscr()

# Ruta a la carpeta que deseas analizar
root_folder = r"C:\\ProgramData"  # Cambia esto a la ruta de la carpeta que deseas analizar

# Análisis de la carpeta
df = analyze_folder_structure(root_folder)

# Mostrar el DataFrame
print("\n\n\nAnálisis completo. Resultados:")
print(df)

# Intentar guardar en archivo Excel con manejo de errores
try:
    df.to_excel("Folder_Size.xlsx", index=False)
    print("\nArchivo Excel 'Folder_Size.xlsx' creado exitosamente.")
except Exception as e:
    print(f"\nError al crear el archivo Excel: {e}")

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
        folder_size = get_folder_size(dirpath)
        folder_data.append({
            "Carpeta": dirpath,
            "Tamaño (Bytes)": folder_size
        })
    
    df = pd.DataFrame(folder_data)
    df['Tamaño (MB)'] = df['Tamaño (Bytes)'] / (1024 * 1024)
    return df

# Ruta a la carpeta que deseas analizar
root_folder = "c:\gestionrecibos"  # Cambia esto a la ruta de la carpeta que deseas analizar

# Análisis de la carpeta
df = analyze_folder_structure(root_folder)

# Mostrar el DataFrame
print(df)

# Si prefieres guardarlo en un archivo Excel
df.to_excel("Folder_Size.xlsx", index=False)

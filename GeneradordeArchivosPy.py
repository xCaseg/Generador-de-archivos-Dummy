import random
import os
import string

#-------------------------------------------------- Funciones auxiliares --------------------------------------------------#

def contenido_aleatorio_lineas(cantidad=5, largo_linea=40):
    return '\n'.join(''.join(random.choices(string.ascii_letters + string.digits, k=largo_linea)) for _ in range(cantidad))

def contenido_aleatorio_csv(filas=5, columnas=3):
    contenido = []
    header = [f"Columna{i+1}" for i in range(columnas)]
    contenido.append(','.join(header))
    for _ in range(filas):
        fila = [f"Dato{random.randint(1, 100)}" for _ in range(columnas)]
        contenido.append(','.join(fila))
    return '\n'.join(contenido)

#----------------------------------------- Funciones para generar archivos dummy -------------------------------------------#

def genera_txt(nombre_archivo):
    with open(nombre_archivo, 'w') as f:
        f.write("Este es un archivo de texto dummy con contenido aleatorio.\n\n")
        f.write(contenido_aleatorio_lineas())

def genera_pdf(nombre_archivo):
    with open(nombre_archivo, 'wb') as f:
        contenido = "%PDF-1.4\n% Dummy PDF\n1 0 obj\n<< /Type /Catalog >>\nendobj\n"
        contenido += "2 0 obj\n<< /Length 44 >>\nstream\n"
        contenido += contenido_aleatorio_lineas(3, 30)
        contenido += "\nendstream\nendobj\ntrailer\n<< /Root 1 0 R >>\n%%EOF"
        f.write(contenido.encode('utf-8'))

def genera_excel(nombre_archivo):
    with open(nombre_archivo, 'w') as f:
        f.write(contenido_aleatorio_csv())

#---------------------------------------------------------------------------------------------------------------------------#


#--------------------------------------------------- Main program ----------------------------------------------------------#

# Ruta donde guardar archivos
ruta_destino = input("Ingrese la ruta donde desea guardar los archivos (ej: C:/archivos_dummy): ").strip()

# Crear ruta si no existe
if not os.path.exists(ruta_destino):
    os.makedirs(ruta_destino)

# Cantidades por tipo de archivo
archivos_pdf = int(input("Cantidad de archivos PDF a generar: "))
archivos_excel = int(input("Cantidad de archivos Excel (CSV) a generar: "))
archivos_txt = int(input("Cantidad de archivos TXT a generar: "))

archivos_cantidad = archivos_pdf + archivos_excel + archivos_txt
print(f"Cantidad total de archivos: {archivos_cantidad}")

# Generar archivos
contador = 1

for i in range(archivos_txt):
    nombre = os.path.join(ruta_destino, f"dummy_txt_{contador}.txt")
    genera_txt(nombre)
    contador += 1

for i in range(archivos_pdf):
    nombre = os.path.join(ruta_destino, f"dummy_pdf_{contador}.pdf")
    genera_pdf(nombre)
    contador += 1

for i in range(archivos_excel):
    nombre = os.path.join(ruta_destino, f"dummy_excel_{contador}.csv")
    genera_excel(nombre)
    contador += 1

print("Archivos generados correctamente.")

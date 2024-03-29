import os
import pandas as pd
from tkinter import messagebox
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment
import csv

def verificar_archivos() -> bool:
    if not os.path.exists('src/datos'):
        os.makedirs('src/datos')
        messagebox.showinfo("Aviso", "Se ha creado el directorio 'datos' correctamente.")
        
    if not os.path.exists('src/datos/tipos.txt'):
        with open('src/datos/tipos.txt', 'w') as archivo_tipos:
            archivo_tipos.write("SELECCIONE TIPO\n")
            archivo_tipos.write("MONITOR\n")
            archivo_tipos.write("CPU\n")
            archivo_tipos.write("UPS\n")
            archivo_tipos.write("ROUTER\n")
            archivo_tipos.write("SWITCH\n")
            archivo_tipos.write("IMPRESORA\n")
            archivo_tipos.write("TELEFONO\n")
            archivo_tipos.write("UBIQUITI\n")
            archivo_tipos.write("LECTOR BARRA\n")
            archivo_tipos.write("BATERIA LECTOR\n")
            archivo_tipos.write("SCANNER\n")
            archivo_tipos.write("LAPTOP\n")
            messagebox.showinfo("Aviso", "Se ha creado el archivo 'tipos.txt' correctamente.")
            #pass
        
    if not os.path.exists('src/datos/marcas.txt'):
        with open('src/datos/marcas.txt', 'w') as archivo_marcas:
            archivo_marcas.write("SELECCIONE MARCA\n")
            archivo_marcas.write("HP\n")
            archivo_marcas.write("DELL\n")
            archivo_marcas.write("LENOVO\n")
            archivo_marcas.write("ACER\n")
            archivo_marcas.write("AOC\n")
            archivo_marcas.write("SAMSUNG\n")
            archivo_marcas.write("LG\n")
            archivo_marcas.write("CISCO\n")
            archivo_marcas.write("MICRO TIK\n")
            archivo_marcas.write("CISCO\n")
            archivo_marcas.write("NANOSTATION M2\n")
            archivo_marcas.write("PSION\n")
            archivo_marcas.write("GRANDSTREAM\n")
            archivo_marcas.write("APC\n")
            archivo_marcas.write("TRIPP LITE\n")
            messagebox.showinfo("Aviso", "Se ha creado el archivo 'marcas.txt' correctamente.")
            #pass
    
    if not os.path.exists('src/datos/dañados.csv'):
        with open('src/datos/dañados.csv', 'w', newline='') as archivo_dañados:
            writer = csv.writer(archivo_dañados, delimiter=';')
            writer.writerow(["FECHA","TIPO", "MARCA", "MODELO", "SERIE", "ACTIVO"])
            messagebox.showinfo("Aviso", "Se ha creado el archivo 'dañados.csv' correctamente.")
            #pass
        return True
    
    return False

def guardar_datos(tipo, marca, modelo, num_serie, num_activo) -> bool:
    try:
        with open('dañados.csv', mode='a', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow([tipo, marca, modelo, num_serie, num_activo])
        return True
    except Exception as e:
        print(f"Ha ocurrido un error al guardar los datos: {e}")
        return False

def cargar_tipos_marcas() -> tuple:
    with open('src/datos/tipos.txt', 'r') as file:
        tipos = [line.strip() for line in file.readlines()]
    with open('src/datos/marcas.txt', 'r') as file:
        marcas = [line.strip() for line in file.readlines()]
    return tipos, marcas

def convertir_excel() -> None:
    pass

def limpiar_fields() -> None:
    pass

def actualizar_cbs() -> None:
    pass

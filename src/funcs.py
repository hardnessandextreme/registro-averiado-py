import os
import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment
import csv

def verificar_archivos() -> bool:
    if not os.path.exists('datos'):
        os.makedirs('datos')

    if not os.path.exists('datos/tipos.txt') or not os.path.exists('datos/marcas.txt'):
        with open('datos/tipos.txt', 'w'):
            pass
        with open('datos/marcas.txt', 'w'):
            pass
        return True
    return False

def guardar_datos() -> None:
    pass

def convertir_excel() -> None:
    pass

def limpiar_fields() -> None:
    pass

def actualizar_cbs() -> None:
    pass

import time
from tkinter import Tk, Label, Button, messagebox, ttk, Entry
from src.funcs import guardar_datos, convertir_excel, verificar_archivos, cargar_tipos_marcas


def inicializar_componentes() -> Tk:
    tipos, marcas = cargar_tipos_marcas()
    
    ventana = Tk()
    ventana.title("Registro de Equipos Dañados")
    ventana.resizable(False, False)

    etiqueta_tipo = Label(ventana, text="Tipo:")
    etiqueta_tipo.grid(row=0, column=0, padx=10, pady=10)
    combo_tipo = ttk.Combobox(ventana, values=tipos, state="readonly")
    combo_tipo.current(0)
    combo_tipo.grid(row=0, column=1, padx=10, pady=10)

    etiqueta_marca = Label(ventana, text="Marca:")
    etiqueta_marca.grid(row=1, column=0, padx=10, pady=10)
    combo_marca = ttk.Combobox(ventana, values=marcas, state="readonly")
    combo_marca.current(0)
    combo_marca.grid(row=1, column=1, padx=10, pady=10)

    etiqueta_modelo = Label(ventana, text="Modelo:")
    etiqueta_modelo.grid(row=2, column=0, padx=10, pady=10)
    entry_modelo = Entry(ventana, width=30)
    entry_modelo.grid(row=2, column=1, padx=10, pady=10)

    etiqueta_num_serie = Label(ventana, text="Número de Serie:")
    etiqueta_num_serie.grid(row=3, column=0, padx=10, pady=10)
    entry_num_serie = Entry(ventana, width=30)
    entry_num_serie.grid(row=3, column=1, padx=10, pady=10)

    etiqueta_num_activo = Label(ventana, text="Número de Activo:")
    etiqueta_num_activo.grid(row=4, column=0, padx=10, pady=10)
    entry_num_activo = Entry(ventana, width=30)
    entry_num_activo.grid(row=4, column=1, padx=10, pady=10)

    label_estado = Label(ventana, text="")
    label_estado.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
    
    fecha_today = time.strftime("%d-%m-%Y")
    label_fecha = Label(ventana, text=fecha_today)
    label_fecha.grid(row=7, column=0, columnspan=2, padx=10, pady=10)
    
    def guardar_datos_click(fecha: str, tipo: str, marca: str, modelo: str, num_serie: str, num_activo: str) -> None:
        fecha = label_fecha.cget(key="text")
        tipo = combo_tipo.get()
        marca = combo_marca.get()
        modelo = entry_modelo.get().upper()
        num_serie = entry_num_serie.get().upper()
        num_activo = "8042000 " + entry_num_activo.get().upper()

        if modelo == "" or num_serie == "" or num_activo == "":
            label_estado.config(text="Todos los campos son obligatorios")
            return

        if guardar_datos(fecha, tipo, marca, modelo, num_serie, num_activo):
            label_estado.config(text="Datos guardados correctamente")
        else:
            label_estado.config(text="Error al guardar los datos")
    
    
    boton_guardar = Button(ventana, text="Guardar", command=guardar_datos_click)
    boton_guardar.grid(row=5, column=0, padx=10, pady=10)

    boton_convertir_excel = Button(ventana, text="Convertir Excel")
    boton_convertir_excel.grid(row=5, column=1, padx=10, pady=10)

    return ventana
    
def abrir_ventana() -> None:
    if verificar_archivos():
        messagebox.showinfo("Aviso", "Se han creados los archivos necesarios.")
    
    ventana = inicializar_componentes()
    ventana.mainloop()
    
def main() -> None:
    abrir_ventana()
    
if __name__ == "__main__":
    main()
from tkinter import Tk, Label, Button, messagebox, ttk, Entry

def inicializar_componentes() -> None:
    ventana = Tk()
    ventana.title("Registro de Equipos Dañados")
    ventana.resizable(False, False)

    etiqueta_tipo = Label(ventana, text="Tipo:")
    etiqueta_tipo.grid(row=0, column=0, padx=10, pady=10)
    combo_tipo = ttk.Combobox(ventana, values="-", state="readonly")
    combo_tipo.current(0)
    combo_tipo.grid(row=0, column=1, padx=10, pady=10)

    etiqueta_marca = Label(ventana, text="Marca:")
    etiqueta_marca.grid(row=1, column=0, padx=10, pady=10)
    combo_marca = ttk.Combobox(ventana, values="-", state="readonly")
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
    
    boton_guardar = Button(ventana, text="Guardar")
    boton_guardar.grid(row=5, column=0, padx=10, pady=10)

    boton_convertir_excel = Button(ventana, text="Convertir Excel")
    boton_convertir_excel.grid(row=5, column=1, padx=10, pady=10)

def main() -> None:
    inicializar_componentes()

if __name__ == "__main__":
    main()
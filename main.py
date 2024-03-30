from src.components import abrir_ventana

def main() -> None:
    try:
        abrir_ventana()
    except Exception as E:
        print(f"Ha ocurrido un error: {E}")

if __name__ == "__main__":
    main()
    
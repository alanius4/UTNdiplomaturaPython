import tkinter as tk
from USUARIO.gui_app import Frame, barra_menu



# Definimos nuestra ventana, su titulo e inclusive un icono
def main():
    root = tk.Tk()
    root.title("Mis series favoritas")
    root.iconbitmap("img/series.ico")
    root.resizable(0, 0)
    barra_menu(root)

    app = Frame(root=root)
    app.mainloop()


if __name__ == "__main__":
    main()

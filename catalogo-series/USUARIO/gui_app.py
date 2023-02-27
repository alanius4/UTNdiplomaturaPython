import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from serie_dao import crear_tabla, borrar_tabla
from serie_dao import Serie, guardar, listar, editar, eliminar
#from catalogo_series import main


def barra_menu(root):
    root = tk
    barra_menu = tk.Menu(root)
    root.config(menu=barra_menu, width=300, height=300)

     # Creacion de menu de inicio y agregado de tearoff para evitar linea punteada
    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    # Con el siguiente codigo agregamos un elemento a la barra de menu
    barra_menu.add_cascade(label="Inicio", menu=menu_inicio)
    # Este menu de inicio tiene opciones
    menu_inicio.add_command(label="Crear Registro en BD", command=crear_tabla)
    menu_inicio.add_command(label="Eliminar Registro en BD", command=borrar_tabla)
    menu_inicio.add_command(label="Salir", command=root.destroy)


# Creacion del Frame (elementos de nuestra ventana)
class Frame:

    observadores = []

    def notificar(self):
        for observador in self.observadores:
            observador.update()

    def _init_(self, root=None):
        super()._init_(root, width=480, height=320)
        self.root = root
        self.pack()
        self.config(bg="white")
        self.id_serie = None
        self.campos_serie()
        self.deshabilitar_campos()
        self.tabla_series()
        self.estado = None
        self.mi_nombre = tk.StringVar()
        self.mi_duracion = tk.StringVar()
        self.mi_genero = tk.StringVar()
        self.mi_temporada = tk.StringVar()
        
    def selt_estado(self,value):
        self.estado = value
        self.notificar()

    def get_estado(self, ):
        return self.estado

    # Creamos un metodo que contendra todos los campos de nuestras series a registrar

    def campos_serie(self):
        # labels de cada campo
        self.label_nombre = tk.Label(self, text="Nombre: ")
        self.label_nombre.config(font=("Arial", 10, "bold"))
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10)

        # Configuracion formato y posicion de los demas campos
        self.label_duracion = tk.Label(self, text="Duración: ")
        self.label_duracion.config(font=("Arial", 10, "bold"))
        self.label_duracion.grid(row=1, column=0, padx=10, pady=10)

        self.label_genero = tk.Label(self, text="Género: ")
        self.label_genero.config(font=("Arial", 10, "bold"))
        self.label_genero.grid(row=2, column=0, padx=10, pady=10)

        self.label_temporada = tk.Label(self, text="Temporada: ")
        self.label_temporada.config(font=("Arial", 10, "bold"))
        self.label_temporada.grid(row=3, column=0, padx=10, pady=10)

        # Diseño los espacio de entry de cada campo: nombre, duracion, genero, temporada.
        # Coloco su posicion en mi Frame, y los espacios entre los entry.
        # Declaramos objetos para enviar datos al campo u obtener datos desde el campo.

        mi_nombre = self.mi_nombre
        self.entry_nombre = tk.Entry(self, textvariable=mi_nombre)
        self.entry_nombre.config(width=50, font=("Arial", 10))
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

        mi_duracion = self.mi_duracion
        self.entry_duracion = tk.Entry(self, textvariable=mi_duracion)
        self.entry_duracion.config(width=50, font=("Arial", 10))
        self.entry_duracion.grid(row=1, column=1, padx=10, pady=10, columnspan=2)

        mi_genero = self.mi_genero
        self.entry_genero = tk.Entry(self, textvariable=mi_genero)
        self.entry_genero.config(width=50, font=("Arial", 10))
        self.entry_genero.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

        mi_temporada = self.mi_temporada
        self.entry_temporada = tk.Entry(self, textvariable=mi_temporada)
        self.entry_temporada.config(width=50, font=("Arial", 10))
        self.entry_temporada.grid(row=3, column=1, padx=10, pady=10, columnspan=2)

        # Botones de nuestro Frame (NUEVO - GUARDAR - CANCELAR )
        # Diseño del mismo: color de fondo, color de letra, y tipo de cursor al tocar.

        # NUEVO: Este boton habilitara los campos para completar.
        self.boton_nuevo = tk.Button(self, text="Nuevo", command=self.habilitar_campos)
        self.boton_nuevo.config(
            width=20,
            font=("Arial", 10, "bold"),
            fg="white",
            bg="#040100",
            cursor="hand2",
            activebackground="#AAA1A0",
        )
        self.boton_nuevo.grid(row=0, column=3, padx=10, pady=10)

        # GUARDAR: guarda la info y deshabilita el campo.

        self.boton_guardar = tk.Button(self, text="Guardar", command=self.guardar_datos)
        self.boton_guardar.config(
            width=20,
            font=("Arial", 10, "bold"),
            fg="white",
            bg="#040100",
            cursor="hand2",
            activebackground="#AAA1A0",
        )
        self.boton_guardar.grid(row=1, column=3, padx=10, pady=10)

        # CANCELAR: este campo deshabilitara los campos para completar y los limpiara.
        self.boton_cancelar = tk.Button(
            self, text="Cancelar", command=self.deshabilitar_campos
        )
        self.boton_cancelar.config(
            width=20,
            font=("Arial", 10, "bold"),
            fg="white",
            bg="#040100",
            cursor="hand2",
            activebackground="#AAA1A0",
        )
        self.boton_cancelar.grid(row=2, column=3, padx=10, pady=10)

        # metodo para habilitar los campos.

    def habilitar_campos(self):
        self.mi_nombre.set("")
        self.mi_duracion.set("")
        self.mi_genero.set("")
        self.mi_temporada.set("")

        # entrys
        self.entry_nombre.config(state="normal")
        self.entry_duracion.config(state="normal")
        self.entry_genero.config(state="normal")
        self.entry_temporada.config(state="normal")

        # botones
        self.boton_guardar.config(state="normal")
        self.boton_cancelar.config(state="normal")

        # Mediante set y los objetos creados en los entrys mediante StringVar, creamos la nueva funcion
        # en deshabilitar campos. Con esto lograremos que al presionar "Cancelar" se limpien los registros de entrada.

        
        

    def deshabilitar_campos(self):
        self.id_serie = None
        self.mi_nombre.set("")
        self.mi_duracion.set("")
        self.mi_genero.set("")
        self.mi_temporada.set("")


        # # entrys
        self.entry_nombre.config(state="disabled")
        self.entry_duracion.config(state="disabled")
        self.entry_genero.config(state="disabled")
        self.entry_temporada.config(state="disabled")

        # botones
        self.boton_guardar.config(state="disabled")
        self.boton_cancelar.config(state="disabled")

    # Ahora queremos obtener los datos que ingresamos, por lo que usaremos "get".
    # Asi mismo, al presionar Guardar, queremos que se limpien los campos de ingreso.

    @deshabilitar_campos #(linea 180)
    def guardar_datos(self):
        serie = Serie(
            self.mi_nombre.get(),
            self.mi_duracion.get(),
            self.mi_genero.get(),
            self.mi_temporada.get(),
        )

        if self.id_serie == None:
            guardar(serie)
        else:
            editar(serie, self.id_serie)

        self.tabla_series()

        self.deshabilitar_campos()

    # DISEñO DE LA TABLA QUE ESTARA EN EL FRAME, GUARDANDO LOS DATOS INGRESADOS.
    # Importaremos ttk.
    # Identificaremos las columnas y su posicion en el Frame.
    # Generaremos ingreso de los primeros valores para su formato en columnas.

    def tabla_series(self):
        # Recuperar lista de peliculas
        self.lista_series = listar()
        self.lista_series.reverse()
        self.tabla = ttk.Treeview(
            self, column=("Nombre", "Duracion", "Genero", "Temporada")
        )
        self.tabla.grid(row=5, column=0, columnspan=5, sticky="nse")

        # scrollbar para la tabla si excede 10 registros
        self.scroll = ttk.Scrollbar(self, orient="vertical", command=self.tabla.yview)
        self.scroll.grid(row=5, column=5, sticky="nse")
        self.tabla.configure(yscrollcommand=self.scroll.set)

        # COLUMNAS
        self.tabla.heading("#0", text="ID")
        self.tabla.heading("#1", text="NOMBRE")
        self.tabla.heading("#2", text="DURACION_EN_CAPITULOS")
        self.tabla.heading("#3", text="GENERO")
        self.tabla.heading("#4", text="TEMPORADA")

        # Iterar la lista de peliculas
        for s in self.lista_series:
            self.tabla.insert("", 0, text=s[0], values=(s[1], s[2], s[3], s[4]))

        # botones
        # EDITAR: Este boton habilitara para editar los campos.
        self.boton_editar = tk.Button(self, text="Editar", command=self.editar_datos)
        self.boton_editar.config(
            width=20,
            font=("Arial", 10, "bold"),
            fg="white",
            bg="#040100",
            cursor="hand2",
            activebackground="#AAA1A0",
        )
        self.boton_editar.grid(row=6, column=1, padx=10, pady=10)

        # ELIMINAR: este campo eliminara un registro de la tabla.
        self.boton_eliminar = tk.Button(
            self, text="Eliminar", command=self.eliminar_datos
        )
        self.boton_eliminar.config(
            width=20,
            font=("Arial", 10, "bold"),
            fg="white",
            bg="#040100",
            cursor="hand2",
            activebackground="#AAA1A0",
        )
        self.boton_eliminar.grid(row=6, column=2, padx=10, pady=10)

    def editar_datos(self):
        try:
            self.id_serie = self.tabla.item(self.tabla.selection())["text"]
            self.nombre_serie = self.tabla.item(self.tabla.selection())["values"][0]
            self.duracion_serie = self.tabla.item(self.tabla.selection())["values"][1]
            self.genero_serie = self.tabla.item(self.tabla.selection())["values"][2]
            self.temporada_serie = self.tabla.item(self.tabla.selection())["values"][3]

            self.habilitar_campos()

            self.entry_nombre.insert(0, self.nombre_serie)
            self.entry_duracion.insert(0, self.duracion_serie)
            self.entry_genero.insert(0, self.genero_serie)
            self.entry_temporada.insert(0, self.temporada_serie)

        except:
            titulo = "edicion de datos"
            mensaje = "no ha seleccionado ningun registro"
            messagebox.showerror(titulo, mensaje)

    def eliminar_datos(self):
        try:
            self.id_serie = self.tabla.item(self.tabla.selection())["text"]
            eliminar(self.id_serie)

            self.tabla_series()
            self.id_serie = None

        except:
            titulo = "Eliminar un Registro"
            mensaje = "No ha seleccionado ningun registro"
            messagebox.showerror(titulo, mensaje)




class observador_campos_des:
            def _init_(self):
                raise NotImplementedError("Campos deshabilitados")
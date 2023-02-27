from conexion_db import ConexionDB
from tkinter import messagebox

# Creamos una funcion para crear una tabla.


def crear_tabla():
    conexion = ConexionDB()

    # Creacion de codigo sql para ejecutar dentro de la base de datos.

    sql = """
    CREATE TABLE series(
        id_serie INTEGER,
        nombre VARCHAR(100),
        duracion_en_capitulos VARCHAR(10),
        genero VARCHAR(100),
        temporada VARCHAR(10),
        PRIMARY KEY(id_serie AUTOINCREMENT)
    )"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = "Crear Registro"
        mensaje = "Se creo la tabla en la base de datos"
        messagebox.showinfo(titulo, mensaje)

    except:
        titulo = "Crear Registro"
        mensaje = "La tabla ya esta creada"
        messagebox.showwarning(titulo, mensaje)


def borrar_tabla():
    conexion = ConexionDB()

    sql = "DROP TABLE series"
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = "Borrar Registro"
        mensaje = "Se borro la tabla en la base de datos con exito"
        messagebox.showinfo(titulo, mensaje)

    except:
        titulo = "Crear Registro"
        mensaje = "No hay tabla para eliminar"
        messagebox.showerror(titulo, mensaje)


class Serie:
    def __init__(self, nombre, duracion_en_capitulos, genero, temporada):
        self.id_serie = None
        self.nombre = nombre
        self.duracion_en_capitulos = duracion_en_capitulos
        self.genero = genero
        self.temporada = temporada

    def __str__(self):
        return f"Serie[{self.nombre},{self.duracion_en_capitulos},{self.genero},{self.temporada}]"


def guardar(serie):
    conexion = ConexionDB()

    sql = f"""INSERT INTO series (nombre, duracion_en_capitulos,genero,temporada)
    VALUES('{serie.nombre}','{serie.duracion_en_capitulos}','{serie.genero}','{serie.temporada}')"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = "Conexion al Registro"
        mensaje = "La tabla series no esta creada en la base de datos"
        messagebox.showerror(titulo, mensaje)


def listar():
    conexion = ConexionDB()

    lista_series = []
    sql = "SELECT * FROM series"

    try:
        conexion.cursor.execute(sql)
        lista_series = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        titulo = "Conexion al Registro"
        mensaje = "Crea la tabla en la Base de datos"
        messagebox.showwarning(titulo, mensaje)

    return lista_series


# ---------------------------------------------------------
def editar(serie, id_serie):
    conexion = ConexionDB()

    sql = f"""UPDATE series
    SET nombre = '{serie.nombre}', duracion_en_capitulos = '{serie.duracion_en_capitulos}',
    genero = '{serie.genero}', temporada ='{serie.temporada}'
    WHERE id_serie = {id_serie}"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()

    except:
        titulo = "Edicion de datos"
        mensaje = "No se ha podido editar este registro"
        messagebox.showerror(titulo, mensaje)


def eliminar(id_serie):
    conexion = ConexionDB()
    sql = f"DELETE FROM series WHERE id_serie = {id_serie}"

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()

    except:
        titulo = "Eliminar datos"
        mensaje = "No se ha podido eliminar este registro"
        messagebox.showerror(titulo, mensaje)

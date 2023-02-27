import sqlite3


class ConexionDB:
    def __init__(self):
        # Colocamos la ruta, si el archivo no existe lo crea, si existe se conecta. (CARPETA/ARCHIVO)
        self.base_datos = "database/series.db"
        # creamos el atributo que va a generar la conexion
        self.conexion = sqlite3.connect(self.base_datos)
        self.cursor = self.conexion.cursor()

    # Para cerrar la base de datos generamos un metodo.
    # Va a realizar los cambios dentro de la base de datos.

    def cerrar(self):
        self.conexion.commit()
        self.conexion.close()

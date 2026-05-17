import mysql.connector

def crear_conexion():
    try:
        conexion=mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='base_datos',
            port='3307'
            )
        return conexion
    except mysql.connector.Error as err:
        print('error al conectar a la base de datos:{}'.format(err))
        return None
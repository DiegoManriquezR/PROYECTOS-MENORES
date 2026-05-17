import mysql.connector
from mysql.connector import Error

class BD:
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                port=3306,
                database='trabajadores',
                user='root',
                password=''
            )
        except Error as ex:
            print('ERROR AL CONECTAR CON MySQL: {0}'.format(ex))
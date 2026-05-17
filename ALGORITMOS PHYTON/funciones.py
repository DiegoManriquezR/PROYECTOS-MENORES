import bcrypt  
from bd.conexion import conexion
from mysql.connector import Error


def registrar_usuario(rut, nombre, apellido, passw):
    conex = conexion()  
    if conex is not None:
        cursor = conex.cursor()

        
        hashed_password = bcrypt.hashpw(passw.encode('utf-8'), bcrypt.gensalt())

        
        sql = "INSERT INTO inicio (rut, nombre, apellido, passw) VALUES (%s, %s, %s, %s)"
        val = (rut, nombre, apellido, hashed_password)

        try:
            cursor.execute(sql, val)  
            conex.commit() 
            print("Usuario registrado exitosamente")
        except Error as error:
            print(f"Error al registrar usuario: {error}")
        finally:
            cursor.close() 
            conex.close() 
    else:
        print("No se pudo establecer la conexión a la base de datos.")

def inicio_sesion(rut, passw):
    conex = conexion()
    try:
        cursor = conex.cursor()
        sql = "SELECT passw, nombre FROM inicio WHERE rut = %s"
        val = (rut,)
        cursor.execute(sql, val)
        result = cursor.fetchone()
 
        if result:
            hashed_password_db = result[0].encode('utf-8')
            hashed_password_input = bcrypt.hashpw(passw.encode('utf-8'), hashed_password_db)  

            if hashed_password_input == hashed_password_db:  
                return result[1]  
        return None 
    except Exception as e:
        print("Error durante la autenticación:", e)
        return None
    finally:
        conex.close()

def guardar_indicadores(resultados_consultados):
    conex = conexion()
    try:
        cursor = conex.cursor()
        sql = "INSERT INTO indicadores (uf, ivp, ipc, utm, dolar, euro, fecha) VALUES (%s, %s, %s, %s, %s, %s, %s)"     
        val = (
            resultados_consultados['uf']['valor'], 
            resultados_consultados['ivp']['valor'], 
            resultados_consultados['ipc']['valor'], 
            resultados_consultados['utm']['valor'], 
            resultados_consultados['dolar']['valor'], 
            resultados_consultados['euro']['valor'], 
            resultados_consultados['fecha']  
        )
        cursor.execute(sql, val)
        conex.commit()
        print("Indicadores guardados exitosamente")
    except Error as error:
        print(f"Error al guardar indicadores: {error}")
    finally:
        cursor.close()
        conex.close()

    


    
    

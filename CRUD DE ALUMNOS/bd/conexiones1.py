import mysql.connector
from mysql.connector import Error

class BD:
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                port = 3307,
                database='trabajadores',
                user='root',
                password=''
            )
        except Error as ex:
            print("Error al conectar con MySQL: {0}".format(ex))
            
    
    def listar_usuarios(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM usuarios")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al conectar con MySQL: {0}".format(ex))
                
    
    def registrar_usuario(self, usuario):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO usuarios (nombre_usuario, rol_usuario) VALUES ('{0}', '{1}')"
                cursor.execute(sql.format(usuario[0], usuario[1]))
                self.conexion.commit()
                print("Usuario Registrado!! \n")
            except Error as ex:
                print("Error al conectar con MySQL: {0}".format(ex))
                
    def eliminar_usuario(self, id_eliminar):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM usuarios WHERE id_usuario = '{0}'"
                cursor.execute(sql.format(id_eliminar))
                self.conexion.commit()
                print("Usuario Eliminado!! \n")
            except Error as ex:
                print("Error al conectar con MySQL: {0}".format(ex))
                
    def editar_usuario(self, usuario):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "UPDATE usuarios SET nombre_usuario = '{0}', rol_usuario = '{1}' WHERE id_usuario = {2}"
                cursor.execute(sql.format(usuario[0], usuario[1], usuario[2]))
                self.conexion.commit()
                print("Usuario editado exitosamente.\n")
            except Error as ex:
                print(f"Error al conectar con MySQL: {ex}")

    def listar_productos(self):
     if self.conexion.is_connected():
        try:
            cursor = self.conexion.cursor()
            cursor.execute("SELECT * FROM productos")  
            resultados = cursor.fetchall()
            return resultados
        except Error as ex:
            print("Error al conectar con MySQL: {0}".format(ex))


    def registrar_producto(self, producto):
     if self.conexion.is_connected():
        try:
            cursor = self.conexion.cursor()
            sql = "INSERT INTO productos (nombre_producto, categoria_producto) VALUES ('{0}', '{1}')"
            cursor.execute(sql.format(producto[0], producto[1]))
            self.conexion.commit()
            print("Producto Registrado!! \n")
        except Error as ex:
            print("Error al conectar con MySQL: {0}".format(ex))

                    
    def eliminar_producto(self, id_eliminar):
     if self.conexion.is_connected():
        try:
            cursor = self.conexion.cursor()
            sql = "DELETE FROM productos WHERE id_producto = '{0}'" 
            cursor.execute(sql.format(id_eliminar))
            self.conexion.commit()
            print("Producto Eliminado!! \n")
        except Error as ex:
            print("Error al conectar con MySQL: {0}".format(ex))

                    
    def editar_producto(self, producto):
     if self.conexion.is_connected():
        try:
            cursor = self.conexion.cursor()
            sql = "UPDATE productos SET nombre_producto = '{0}', categoria_producto = '{1}' WHERE id_producto = {2}"
            cursor.execute(sql.format(producto[0], producto[1], producto[2]))
            self.conexion.commit()
            print("Producto editado exitosamente.\n")
        except Error as ex:
            print(f"Error al conectar con MySQL: {ex}")


    def listar_categorias(self):
      if self.conexion.is_connected():
        try:
            cursor = self.conexion.cursor()
            cursor.execute("SELECT * FROM categorias")  
            resultados = cursor.fetchall()
            return resultados
        except Error as ex:
            print("Error al conectar con MySQL: {0}".format(ex))


    def registrar_categoria(self, categoria):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO categorias (nombre, descripcion) VALUES ('{0}', '{1}')"
                cursor.execute(sql.format(categoria[0], categoria[1]))
                self.conexion.commit()
                print("Categoría Registrada!! \n")
            except Error as ex:
                print("Error al conectar con MySQL: {0}".format(ex))
                    
    def eliminar_categoria(self, id_eliminar):
      if self.conexion.is_connected():
        try:
            cursor = self.conexion.cursor()
            sql = "DELETE FROM categorias WHERE id_categoria = '{0}'"  # Cambiar "productos" por "categorias"
            cursor.execute(sql.format(id_eliminar))
            self.conexion.commit()
            print("Categoría Eliminada!! \n")
        except Error as ex:
            print("Error al conectar con MySQL: {0}".format(ex))

                    
    def editar_categoria(self, categoria):
     if self.conexion.is_connected():
        try:
            cursor = self.conexion.cursor()
            sql = "UPDATE categorias SET nombre = '{0}' WHERE id_categoria = '{1}'"
            cursor.execute(sql.format(categoria[0], categoria[1]))
            self.conexion.commit()
            print("Categoría editada exitosamente.\n")
        except Error as ex:
            print(f"Error al conectar con MySQL: {ex}")


    def listar_proveedores(self):
      if self.conexion.is_connected():
        try:
            cursor = self.conexion.cursor()
            cursor.execute("SELECT * FROM proveedores") 
            resultados = cursor.fetchall()
            return resultados
        except Error as ex:
            print("Error al conectar con MySQL: {0}".format(ex))

    def registrar_proveedor(self, proveedor):
     if self.conexion.is_connected():
        try:
            cursor = self.conexion.cursor()
            sql = "INSERT INTO proveedores (nombre_proveedor, direccion_proveedor, contacto_proveedor, producto_suministrado) VALUES ('{0}', '{1}', '{2}', '{3}')"
            cursor.execute(sql.format(proveedor[0], proveedor[1], proveedor[2], proveedor[3]))
            self.conexion.commit()
            print("Proveedor Registrado!! \n")
        except Error as ex:
            print("Error al conectar con MySQL: {0}".format(ex))


    def editar_proveedor(self, proveedor):
     if self.conexion.is_connected():
        try:
            cursor = self.conexion.cursor()
            sql = "UPDATE proveedores SET nombre_proveedor = '{0}', direccion_proveedor = '{1}', contacto_proveedor = '{2}', producto_suministrado = '{3}' WHERE id_proveedor = {4}"
            cursor.execute(sql.format(proveedor[0], proveedor[1], proveedor[2], proveedor[3], proveedor[4]))
            self.conexion.commit()
            print("Proveedor editado exitosamente.\n")
        except Error as ex:
            print(f"Error al conectar con MySQL: {ex}")


    def eliminar_proveedor(self, id_eliminar):
      if self.conexion.is_connected():
        try:
            cursor = self.conexion.cursor()
            sql = "DELETE FROM proveedores WHERE id_proveedor = '{0}'"  # Cambiar "categorias" por "proveedores"
            cursor.execute(sql.format(id_eliminar))
            self.conexion.commit()
            print("Proveedor Eliminado!! \n")
        except Error as ex:
            print("Error al conectar con MySQL: {0}".format(ex))

                

    def cerrar_conexion(self):
            if self.conexion and self.conexion.is_connected():
                self.conexion.close()
                print("Conexión cerrada.")


    def listar_transacciones(self):
     if self.conexion.is_connected():
        try:
            cursor = self.conexion.cursor()
            cursor.execute("SELECT * FROM transacciones") 
            resultados = cursor.fetchall()
            return resultados
        except Error as ex:
            print("Error al conectar con MySQL: {0}".format(ex))

    def registrar_transaccion(self, transaccion):
     if self.conexion.is_connected():
        try:
            cursor = self.conexion.cursor()
            sql = "INSERT INTO transacciones (tipo, fecha, cantidad, descripcion) VALUES ('{0}', '{1}', '{2}', '{3}')"
            cursor.execute(sql.format(transaccion[0], transaccion[1], transaccion[2], transaccion[3]))
            self.conexion.commit()
            print("Transacción Registrada!! \n")
        except Error as ex:
            print("Error al conectar con MySQL: {0}".format(ex))
            
    def eliminar_transaccion(self, id_eliminar):
     if self.conexion.is_connected():
        try:
            cursor = self.conexion.cursor()
            sql = "DELETE FROM transacciones WHERE id_transaccion = '{0}'"  # Cambiar "proveedores" por "transacciones"
            cursor.execute(sql.format(id_eliminar))
            self.conexion.commit()
            print("Transacción Eliminada!! \n")
        except Error as ex:
            print("Error al conectar con MySQL: {0}".format(ex))
            
    def editar_transaccion(self, transaccion):
     if self.conexion.is_connected():
        try:
            cursor = self.conexion.cursor()
            sql = "UPDATE transacciones SET fecha_transaccion = '{0}', monto_transaccion = '{1}', tipo_transaccion = '{2}', proveedor_id = '{3}' WHERE id_transaccion = {4}"
            cursor.execute(sql.format(transaccion[0], transaccion[1], transaccion[2], transaccion[3], transaccion[4]))
            self.conexion.commit()
            print("Transacción editada exitosamente.\n")
        except Error as ex:
            print(f"Error al conectar con MySQL: {ex}")

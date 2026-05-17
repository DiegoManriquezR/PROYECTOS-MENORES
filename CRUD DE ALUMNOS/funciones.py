from bd.conexion import crear_conexion


def insertar_producto(codigo,nombre,modelo,precio,cantidad):
    conexion=crear_conexion()
    if conexion is not None:
      cursor=conexion.cursor()
      sql='INSERT INTO productos(codigo,nombre,modelo,precio,cantidad) VALUES (%s,%s,%s,%s,%s)'
      datos=(codigo,nombre,modelo,precio,cantidad)
      cursor.execute(sql,datos)  
      conexion.commit()
      cursor.close()
      conexion.close()
      
def mostrar_producto():
    conexion=crear_conexion()
    if conexion is not None:
        cursor=conexion.cursor()
        cursor.execute('SELECT * FROM productoS')
        productos=cursor.fetchall()
        cursor.close()
        conexion.close()
        return productos
    
def actualizar_producto(id,codigo,nombre,modelo,precio,cantidad):
    conexion=crear_conexion()
    if conexion is not None:
        cursor=conexion.cursor()
        sql='UPDATE productoS SET codigo=%s, nombre=%s, modelo=%s, precio=%s, cantidad=%s WHERE id =%s'
        datos=(codigo,nombre,modelo,precio,cantidad,id)
        cursor.execute(sql,datos)
        conexion.commit()
        cursor.close()
        conexion.close()
   
def eliminar_producto(id):
    conexion=crear_conexion()
    if conexion is not None:
        cursor=conexion.cursor()
        sql='DELETE FROM productoS WHERE id =%s'
        datos=(id,)
        cursor.execute(sql,datos)
        conexion.commit()
        cursor.close()
        conexion.close()
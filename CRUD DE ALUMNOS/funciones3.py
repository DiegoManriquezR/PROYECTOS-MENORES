def listar(personas):
    print('PERSONAS:')
    titulos= "{0:3} | {1:14} | {2:16} | {3:19}"
    largo_titulos = len(titulos.format('N°','CODIGO','NOMBRE PERSONA', 'CARGO'))
    print('-' * largo_titulos)
    print(titulos.format('N°','CODIGO','NOMBRE PERSONA','CARGO'))
    print('-' * largo_titulos)
    contador=1
    for per in personas:
        datos="{0:3} | {1:14} | {2:16} | {3:19}"
        print(datos.format(contador, per[0],per[1],per[2]))
        contador +=1
    print('-' * largo_titulos)
    
    
def registro():
    nombre= input('INGRESE EL NOMBRE DE LA PERSONA:')
    cargo= input('INGRESE EL CARGO DE LA PERSONA:')
    persona=(nombre,cargo)
    return persona

def eliminar(personas):
    listar(personas)
    id_eliminar=int(input('INGREAE EL NUMERO DE PERSONAS A ELIMINAR:'))
    existe_id=False
    for per in personas:
        if per[0]==id_eliminar:
            existe_id=True
            break
    if not existe_id:
        id_eliminar=""
    return id_eliminar

def editar(personas):
    listar(personas)
    
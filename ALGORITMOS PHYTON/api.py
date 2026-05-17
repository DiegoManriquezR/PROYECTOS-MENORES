#pip install requests
import requests

def obtener_chiste():
    # realizar una solicitud GET a la API de jokrapi.dev
    url="http://v2.jokeapi.dev/joke/Any"#ruta de la api
    respuesta = requests.get(url)#realiza la solicitud
    #verifica si la solicitud fue exitosa
    if respuesta.status_code==200:
        #obtienen el contenido de respuesta en formato JSON
        chiste=respuesta.json()
        #extrae el chiste
        if chiste ['type']=='single':
            return chiste['joke']
        else:
            return chiste['setup']+ '\n' + chiste['delivery']
    else:
        return 'no se pudo obtener el chiste'
    
    #llama a la funcion para obtener chistye
print(obtener_chiste())



#### encontrar miindicador
### recibiendo varios argumentos
def calcular_media(*args):
        total=0
        for i in args:#6,5,6.3
            total+=i
        resultado=total/len(args)
        return resultado
        

a,b,c=6,5,6.3
promedio=calcular_media(a,b,c,)
print(f'la media de {a},{b},{c} es {promedio:.2F}')
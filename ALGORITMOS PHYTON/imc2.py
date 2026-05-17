for i in range (4):
    print('calculo indice de masa corporal')
    peso=float(input('ingrese su peso en kg.'))
    talla=float(input('ingrese su talla en mt.'))
    imc=peso/talla**2
    if imc>=30:
        print('OBESO, SU IMC ES ',imc)
    elif imc>25:
        print('SOBREPESO, SU IMC ES ',imc)
    elif imc>=20:
        print('NORMAL, SU IMC ES ',imc)
    else:
        print('BAJO PESO, SU IMC ES ',imc)
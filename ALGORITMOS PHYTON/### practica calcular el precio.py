def calcular_imc(peso, talla):
    imc = peso / (talla ** 2)
    categoria = ""
    
    if imc < 20:
        categoria = "Bajopeso"
    elif 20 <= imc < 25:
        categoria = "Normal"
    else:
        categoria = "Sobrepeso"
    
    return imc, categoria

# Ejemplo de uso
peso_persona = float(input("Ingresa el peso en kilogramos: "))
talla_persona = float(input("Ingresa la talla en metros: "))

imc_resultado, categoria_resultado = calcular_imc(peso_persona, talla_persona)

print(f"IMC: {imc_resultado:.2f}")
print(f"Categoría: {categoria_resultado}")
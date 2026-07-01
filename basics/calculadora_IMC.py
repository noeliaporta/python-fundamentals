peso=int(input("INGRESE EL PESO: "))
altura=float(input("INGRESE ALTURA EN CENTIMETROS: "))
resultado=""

imc=peso/(altura)**2

if imc <= 18.5:
    resultado="Peso insuficiente"
elif imc >= 18.5 and imc <= 24.9:
    resultado="sobrepeso"
elif imc>= 30:
    resultado="debilidad"

print(resultado)
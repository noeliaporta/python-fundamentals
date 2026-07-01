
def linea():
        print("#" * 50) #procedimiento
    
linea()

#Argumentos por valor
def doblarNumero(nro):
     nro = nro * 2
     return nro

Numero = 3
print("El valor de la variable numero es :", Numero)
print("El doble del numero es ", doblarNumero(Numero))

print("El valor de la variable es ", Numero, "y no se modifico")

linea()


def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    try:                            #Si econtras tal error no hagas este return....         
       return num1 / num2
    except ZeroDivisionError:
        print("No se puede dividir por cero ")       # ...imprimime este msj 
        return"Operacion erronea"

while True:
    try:
        op1 = (int(input("Introduce el primer numero")))
        op2 = (int(input("Introduce el segundo numero")))
        break 
    except ValueError:
        print("Los valores introducidos no son correctos. Intantalo nuevamente colocando un numero.")

operacion = input("Introduce la operacion a realizar: (suma, restar, multiplicar, dividir)")
if operacion == "suma":
        print(suma(op1, op2))
elif operacion == "resta":
        print(resta(op1, op2))
elif operacion == "dividir":
        print(dividir(op1, op2))
elif operacion == "multiplicar":
        print(multiplicar(op1, op2))
else:
        print("Operacion no contemplada")
linea()
print("Operacion ejecutada, fin del programa.")
linea()

#calculadora()
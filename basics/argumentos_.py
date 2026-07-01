'''''
def saludar(nombre,profesion):
    print(f"Hola" [nombre], "tu profesion es", profesion)  #nombrable
'''

def linea():
   print("#" * 35)
   
linea()
def doblarNumero(nro):
    nro = nro *2
    return nro

miNumero = 3
print("El doble del numero es", doblarNumero(miNumero))
print("El numero sin doblar es", miNumero)
linea()
def doblarNumero2(nros):
    for indice in range(len(nros)): #len(nros)--->3-->rango(3)
      nros[indice] = nros[indice]*2
    return nros
miNumero= [10, 20, 30, 15]

print(miNumero)
print(doblarNumero2(miNumero))
print(miNumero)
linea()


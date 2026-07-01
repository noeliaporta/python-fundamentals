print("################ TUPLA #################")

datos_personales=("Jorge", "17009956", 58, 1965, 25.69)#Creamos una Tupla (Las Tuplas son inmutables)

print(datos_personales[4])#Imprimimos un dato especifico el de las posicion 4

print("############## LISTA ############")

paises=["argentina", "chile", "uruguay", "paraguay"]#Es una lista (se pueden modificar)

print (paises[2])#Imprimo la posicion 2 en la lista
print("############## LISTA ############")

print("############## DICCIONARIO ############")

mascotas = {"pupy": "mi perro",
            "gatty": "gato blanco mio",
            "pipi": "canario del vecino"}#Es un Diccionario

print(mascotas["gatty"])#Imprimo un dato del diccionario solicitando la clave

print("############## DICCIONARIO ############")

print("################ TUPLA #################")

print("Jorge" in datos_personales)#consulto si se encuentra Jorge en la Tupla

print(len(datos_personales))#Imprimo la cantidad de datos total en numero, en la Tupla 

print(datos_personales)#Imprimo la Tupla completa como Tupla

print("################ TUPLA #################")

print("############## LISTA ############")
print(paises)# Imprimo la lista completa 
print("############## LISTA ############") 


print("############## DICCIONARIO ############")
print(mascotas)#Imprimo el diccionario completo
print("############## DICCIONARIO ############")

print("################ empaquetado de Tupla ################## ")
fecha="julio", 25 , 3 , 1965  #A esto se lo llama empaquetado de Tupla

print(fecha)#Imprimo el empaquetado de Tupla
print("################ empaquetado de Tupla ################## ")


print("################ Variables del desempaquetado de Tupla ################## ")
nombre, dia, mes, año=fecha #A esto se lo llama desempaquetado de Tupla

print(nombre)
print(dia)
print(mes)
print(año)
print("################ Variables del desempaquetado de Tupla ################## ")

print("################ Trabajamos con Listas ################## ")

print(paises[:])#Imprimimos la lista completa 
print(paises[0:5])#Imprimimos la lista completa indicando principio y final (en nuestro ej nos imprime los primeros 6 elementos)

paises.extend(["ecuador", "Colombia", "Venezuela"])#Agregamos varios elementos a la lista 

paises.append("mexico")#Agregamos un pais al final 
print(paises[0:7])

print(paises)#Imprimimos toda la lista 

print(paises[-7])#Imprimimos la posicion -7 contando desde -1 de atras para adelante 

print(paises[5], paises[2])#Imprimimos el elemento 2 y 5 de la lista

datos_varios =["Peru", 1, 2, 2, True]

paises.pop()   #.pop retira el último elemento de la lista

print(paises)

paises.append(datos_varios)
print(paises)

lista_Nueva= paises + datos_varios

print(lista_Nueva)

ciudades = ['New York', 'Dallas', 'San Antonio', 'Houston', 'San Francisco']
print(ciudades)
print ( "Ciudad removida : ", ciudades.pop() )#Ciudad removida :  San Francisco

print ( "La ciudad en el indice 2 es : ", ciudades.pop(2) )#La ciudad en el indice 2 es :  San Antonio

 
print(ciudades)

numeros_Primos = [2, 3, 5, 7, 9, 11]

print(numeros_Primos)

numeros_Primos.remove(9)

print(numeros_Primos)

# Updated la lista numeros_primos
print('Updated List: ', numeros_Primos )

# Output: Updated List:  [2, 3, 5, 7, 11]

dic1 ={
    "cuadrados":4,
    "triangulos":3,
    "rectangulo":4,
    "hexagonos":6,
    "pentagono":5,
    "rombo":4,
}

for clave in dic1.keys():
    print(clave)

for valor in dic1.values():
    print(valor)

print(dic1["cuadrados"])
print(dic1.get("hexagonos"))

dic1.update({"cuadrado":5, "octagono":8, "pentagono":7})
print(dic1)

dic1.pop("cuadrados")

print(dic1)
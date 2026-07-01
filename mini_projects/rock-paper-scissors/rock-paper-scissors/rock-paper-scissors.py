import random
def msj():
    print("Puntajes actuales:", "Maquina: ", puntaje_maquina, "Tu: ", puntaje_jugador)
        
intentos_hechos= 0

puntos= int(input("A cúantos puntos deseas jugar? "))
puntaje_jugador = 0
puntaje_maquina = 0

while(puntaje_jugador < puntos and puntaje_maquina < puntos):
    respIngresada= input("Ingrese piedra, papel, tijera para jugar... ")
    opciones = ["Piedra", "Papel", "Tijera"]
    resp_aleatorias= random.choice(opciones)
    print(resp_aleatorias)
    if  respIngresada == resp_aleatorias:
        print("Ambos eligieron lo mismo, ES UN  EMPATE!")
        msj()
    elif resp_aleatorias == "Piedra" and respIngresada == "Papel":
        print("Papel vence a piedra, GANASTE!")
        puntaje_jugador += 1
        msj()
        
    elif resp_aleatorias == "Papel" and respIngresada == "Piedra":
        print("Papel vence a piedra, LA MAQUINA GANO!!")
        puntaje_maquina += 1
        msj()
        
    elif resp_aleatorias == "Papel" and respIngresada == "Tijera":
        print("Tijera vence a papel, GANASTE!!")
        puntaje_jugador +=1
        msj()
        
    elif resp_aleatorias == "Tijera" and respIngresada == "Papel":
        print("Tijera vence a papel, LA MAQUINA GANA")
        puntaje_maquina +=1
        msj()
        
    elif resp_aleatorias == "Tijera" and respIngresada == "Piedra":
        print("Piedra vence a tijera, Ganaste")
        puntaje_jugador += 1
        msj()
        
    elif resp_aleatorias == "Piedra" and respIngresada == "Tijera":
        print("Piedra vence a tijera, la maquina gano")
        puntaje_maquina +=1
        msj()


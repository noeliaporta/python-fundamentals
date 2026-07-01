
#===============================================================================================

print(" ")                                                                             
print("_____ Bienvenido al programa para la fabricacion de Biocombustible  ______")
print(" ")
# Declarar variables que posean todos los datos importantes del proceso como el tiempo que necesita cada uno 

aceite = float(input("Ingrese la cantidad de aceite:(Lts) "))
almacen_alcohol = int(input("Ingrese la cantidad de alcohol:(Lts) "))                #Sugerencia, si el valor de alcohol es muy cercano al valor introducido de aceite, no lo tome

while aceite <= almacen_alcohol:   # signo de aproximacion almacen_alcohol :                   #El valor ingresado de alcohol nod ebe ser muy aproximado al vlaor de aceite ingresado
    print("El valor ingresado de alcohol es mayor o igual al valor ingresado de aceite. Por favor ingrese nuevamente los valores. ")
    aceite = float(input("Ingrese la cantidad de aceite:(Lts) "))
    almacen_alcohol = float(input("Ingrese la cantidad de alcohol:(Lts) "))
    break

alcohol = float(input("Ingrese el tipo de alcohol que desea utilizar: etanol [1] o metanol [2]: "))

if alcohol != 1:
       print("Usted a elegido utilizar alcohol de tipo metanol.")
else:
       print("Usted a elegido utilizar alcohol de tipo etanol.")

encendido = input("Escriba Y para habilitar el almacen de alcohol: ")

while encendido == "Y" :

    time = 10 * almacen_alcohol                                           #10 minutos multiplicado la cantidad de alcohol
    print("\n")
    from random import randint
    Temperatura = int(randint(18, 20))                                    # 18°C o 19C o 20°C_
    Q = float(almacen_alcohol * 0.0024 * Temperatura)                     #Formula para calcular la cantidad de calor
    energia_estado_transicion = Q * time                                  #esta dada por la ley de la conducción de calor de Fourier
    break
else:  
       print("Almacen de alcohol no habilitado, El programa se desactivara. ")
    
Lt_biodiesel = aceite
energia_reactivo = (2 / 8.314) * Temperatura

def condicion_encendido():
    while encendido != "Y":
       print("El programa se desactivara. ")
       break


def linea():
        print("**" * 50)#procedimiento
    
def linea2():
        print("__" * 70)#procedimiento
    
          ##########CATALIZADOR##########
                                                                       # Lo que logramos con el proceso de catalización 
#energia_estado_transicion -                                         # es disminuir la energia de transición 
Energía_activación = energia_estado_transicion - energia_reactivo 
#tiempo_catalizacion =

print("Datos obtenidos del proceso de CATALIZACIÓN ...")
print("La energía del estado de transición vale: ", energia_estado_transicion)
print("La energía de reactivación vale: ", energia_reactivo)
print("Teniendo en cuenta los datos obtenidos podemos definir el valor de la energía de activación, sabiendo que...")
print(" ~ La energía de activación es el resultado de la diferencia entre",
      "la energia del estado de transición y la energía de reactivación ~ ")
print("La energía de activación vale: ", energia_estado_transicion - energia_reactivo )
print(" ")
linea2()
print("Ahora pasaremos al siguiente proceso, por favor ingrese los datos correspondientes...")

# Variables para el proceso de mezclado
print("Dato a tener en cuenta... Todos los componentes que va a utilizar dependen de las cararterísticas del biodiesel que desee fabricar!")
print(" ")

            ################ PROCESO DE MEZCLADO ###################
HIDROXIDO = int(input("Ingrese el tipo de hidróxido que va a utilizar (hidróxido de potasio [1] o hidróxido de sodio [2]): "))
acido_sulfurico = int(input("¿Va a utilizar ácido sulfurico? [1] SI o [2] NO "))  # si su respuesta es si, que se agrege a la mezcla 

linea()
print("¿Sabías que el hidróxido de potasio se mezcla con mayor facilidad y rápidez?,")
print( "a diferencia del hidróxido de sodio que puede llegar a tardar de 24hs a 36hs en mezclarse correctamente.")
linea()
print("A continuación... introduzca en la máquina los componentes seleccionados.(Aquí se hace referencia a la parte física)")
encendido= input("Escriba Y para habilitar el proceso de mezclado: ")
condicion_encendido()
print("IDENTIFICANDO COMPONENTES...")

hidróxido_potasio = int(10)                                                              #Asumimos que el KOH vale 10      
hidróxido_sodio = int(15)                                                                #Asumimos que el KOH vale 15

print("Verificación finalizada, el proceso se iniciará imediatamente.")
linea2()
print("******************* PROCESO DE MEZCLADO DEL ALCOHOL *******************")

tiempo_mezclado = int(1440)                                                              # 1440 minutos equivalen a 24 horas
tiempo_mezclado2 = int(2160)                                                              # 2160 minutos equivalen a 36 horas

if(HIDROXIDO == 1 and acido_sulfurico == 2 ):
    print("Se mezclará el alcohol con el hidróxido de potasio, el proceso tardará:", tiempo_mezclado,
               "minutos")
    print("... ... ..")
    MEZCLADO = int(almacen_alcohol + hidróxido_potasio)
    print("El proceso se llevó a cabo satisfactoriamente.")
    linea2()
elif (HIDROXIDO == 1  and acido_sulfurico == 1 ) :
    print("Se mezclará el alcohol con el hidróxido de potasio y el ácido sulfúrico, el proceso tardará:", tiempo_mezclado, "minutos")
    print("... ... ..")
    MEZCLADO = int(almacen_alcohol + hidróxido_potasio + acido_sulfurico)
    print("El proceso se llevó a cabo satisfactoriamente.") 
    linea2()
elif (HIDROXIDO == 2  and acido_sulfurico == 1 ):
    print("Se va a mezclar el alcohol con el hidróxido de sodio y el ácido sulfúrico, el proceso tardará:", tiempo_mezclado2, "minutos")
    print("... ... ..")
    MEZCLADO = int(almacen_alcohol + hidróxido_sodio + acido_sulfurico)
    print("El proceso se llevó a cabo satisfactoriamente.") 
    linea2()
elif(HIDROXIDO == 2  and acido_sulfurico == 2 ):
    print("Se va a mezclar el alcohol con el hidróxido de sodio, el proceso tardará:", tiempo_mezclado2, "minutos")    
    print("... ... ..")
    MEZCLADO = int(almacen_alcohol + hidróxido_sodio)
    print("El proceso se llevó a cabo satisfactoriamente.")
    linea2()

           ###PROCESO: FILTRADO DE LA ACEITE
print("**************** PROCESO DE FILTRACIÓN DEL ACEITE *******************")
encendido2 = input("Ingrese Y para activar el filtrador y dar inicio al proceso de filtración: ")
time = 15 * aceite                                                                               #15 minútos multiplicado la cantidad de aceite
while encendido2 == "Y":
     linea2()
     print("Se dará inicio al proceso de filtrado.")
     print("Vertiendo la aceite en el filtro")
     print("... ...")
     print("Este proceso tardará aproximadamente ", time, "minútos.")
     print("El proceso de filtrado se llevó a cabo satisfactoriamente. ")
     linea2()
     break
else:
     print("Filtrador no habilitado, no se puede llevar a cabo el proceso de filtración. El programa se desactivará. ")
    
       #################### REACTOR #####################

print("**************** SE INTRODUCE LA MEZCLA DENTRO DEL REACTOR *******************")
encendido3 = input("Ingrese Y para activar el reactor y dar inicio al proceso: ")
while encendido3 == "Y":
             almacen_aceite = aceite
             REACTOR = almacen_aceite + ( 75 * MEZCLADO / 100)                                                  #solo un 75% del mezclado se introduce en el reactor junto con el aceite
             Temperatura_reactor = randint (32, 42)                                                              #Se eleva la temp entre 50° y 65°C (le reste la temp ambiente)
             TEMP = Temperatura + Temperatura_reactor
             print("Temperatura en tiempo real del reactor: ", TEMP,"°c")    
             print("Este proceso puede tardar entre 1hr y media y 2hrs y media")
             print("Se dará inicio al proceso de mezclado...")
             print("... ... ..")
             print("Proceso finalizado.")
             linea()
             break
else:
    print("Reactor no habilitado, no se puede llevar a cabo el proceso de filtración. El programa se desactivará. ")

tiempo_reposo = 15                                                                                                #El tiempo de reposo tarda 15 minútos
print("Se deja en reposo durante", tiempo_reposo," minútos para que se aciente el fluido más denso.")
print("Iniciando tiempo de reposo...")
print("... ...")
print("Tiempo de reposo finalizado.")
linea()
            
       #################### SEPARADOR #####################
input("Escriba Y para comenzar con el proceso de separación del biodiesel y la glicerina: ")
while encendido == "Y":
     print("Se dará inicio al proceso de separación...")   
     print("... ... ..")
     print("Se procede a extraer el producto obtenido, por favor identifique el producto: ...")
     break  
else:
     print("Proceso de separación no habilitado, El programa se desactivará. ")       

color_fluido = int(input("Ingrese el color del fluido, color miel [1] o marron oscuro [2]: "))                        #Este paso es simple verifiación, ya 
densidad_fluido = int(input("Ingrese si el fluido tiene un nivel de densidad reducido [1] o elevado [2]: "))          #que sabemos que la glicerina al 
                                                                                                                      #ser más densa que el biodiesel estará
while color_fluido != 1 and color_fluido != 2 or densidad_fluido != 1 and densidad_fluido != 2:                       #en el fondo del tanque por lo que será
    print("Los datos introducidos no corresponden a los fluidos, por favor intentelo nuevamente. ")                   #lo primero que se extrae
    break


contenidoXbidon = 2                                                                                                   #Los bidones contendrán 2 litros c/u


while color_fluido == 2 and densidad_fluido == 2:                                                                                                            
      contenido = "glicerina"
      print("Las características introducidas pertenecen al fluido denominado GLICERINA. ")                 
      Lt_glicerina = contenido = almacen_alcohol
      bidones = almacen_alcohol / contenidoXbidon
      print("La cantidad de bidones de glicerina que se obtuvieron es de: ", bidones)
      break
      
if color_fluido == 1 and densidad_fluido == 1 :
        contenido = Lt_biodiesel
        print("Las características introducidas pertenecen al fluido denominado BIODIESEL. ")        
        linea2()
        print("Sugerencia: Si lo primero en extraerse es biodiesel, es recomendable dejarlo en reposo nuevamente por más tiempo.") 
        linea2()
        #################### LAVADO ########################
        print("Pasamos el biodiesel al siguiente resipiente y le introducimos agua para dar inicio a su lavado...")
        print("# Primer etapa: se le agregan de 20 a 30 litros de agua que se deja decantar durante 24hs")
        print("Finalizado este tiempo...")
        print("Se debe dejar en reposo para posteriormente drenar el agua ...")
        print("Iniciando proceso de drenado del agua...")
        print("Proceso finalizado.")
        linea()
        print("# Segunda etapa...")
        print("Nuevamente se introduce agua...")
        print("Finaliza el tiempo de lavado...")
        print("Se debe dejar en reposo para posteriormente drenar el agua ...")
        print("Pasa a la siguiente etapa donde se procede a realizar un tercer lavado...")
        linea()
        print("# Tercer etapa...")
        print("Nuevamente se introduce agua...")
        print("Finalizado este tiempo...")
        print("Se debe drenar nuevamente el agua ...")
        print("Luego del 4to o 5to día, se pasa el biodiesel al proceso de secado, donde se procede a evaporar el agua que queda en el biodiesel...")
        linea()
        print("Incrementando la temperatura...")
        Temperatura_secado = randint(80, 120)                                                                       #Se eleva la temp entre 80° y 120°C
        TEMP = Temperatura + Temperatura_secado
        print("Temperatura en tiempo real: ", TEMP, "°C")   
        print("Una vez finalizado el proceso de secado se examina el producto final y se procede a distribuirlo en bidones para su posterior venta.")
        bidones = Lt_biodiesel / contenidoXbidon                                                                  #se determina la cantidad de bidones dependiendo de los
        print("La cantidad de bidones de biodiesel que se obtuvieron es de: ", bidones)                                 #lts de biodiesel que puede contener cada uno 
       
 #Sería mejor que el programa en caso de que el usuario ingrese una cantidad no divisible por dos el programa le indique que el último bidon tiene tanto de biodiesel

#falta introducir el otro 25% de la mezcla en el proceso correspondiente


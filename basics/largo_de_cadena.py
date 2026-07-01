cad1 = input("Ingrese la primer cadena:/n")
cad2 = input("Ingrese la segunda cadena:/n")

if(len(cad1) > len(cad2)):
    print(f"La cadena mas larga es {cad1}")
elif(len(cad1) < len(cad2)):
    print(f"La cadena mas larga es {cad2}")
else:
    print("Tienen el mismo largo.")
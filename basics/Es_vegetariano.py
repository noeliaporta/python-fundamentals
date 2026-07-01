
tipo = input("Hola!! Es usted vegetariano o carnívoro?")


match tipo:
    case "1":
      print("MENÚ VEGETARIANO: "
          "Pizza de muzzarella, Milanesa de soja con papas, Empanada de verdura")
      comida = input("Introduce en ingrediente que deseas: ")
      match comida:
         case "1":
            print("Tome la pizza con muzarella")
         case "2": 
            print()
         case "3":
            print()      
    case "2":
      print("Menú carnivoro/n1- Pizza conpanceta/n2- Milanesa de pollo con papas/n3- Empanada de carne picada")
      comida = input("Introduce el ingrediente que deseas: ")
      match comida:
         case "1":
            print("Tome la pizza con panceta")
         case "2":
            print("Tome la milanesa de pollo con papas")
         case "3":
            print("Tome la empanada de carne picada")
         case _:
            print("No se encuentra en el menú")
    case _:
      print("No es un valor posible")
      
print("Vuelva pronto!")


        
#else:
   # print("MENÚ: ")
   # print("[1] Pizza de muzzarella")


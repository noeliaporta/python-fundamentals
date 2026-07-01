print("MENU DE OPCIONES")
print("[1] Ventas")
print("[2] Pagos")
print("[3] Servicio técnico")
print("[4] Gerencia")

num = input("Elegí tu opción:/n ")

match num:
    case "1":
        print("Elegiste ventas")
    case "2":
        print("Elegiste pagos")
    case "3":
        print("Elegiste servicio técnico")
    case "4":
        print("Elegiste gerencia")
        
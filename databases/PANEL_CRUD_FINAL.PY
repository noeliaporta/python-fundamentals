from tkinter import *
from tkinter import messagebox
import sqlite3
from tkinter.ttk import Combobox

root=Tk()
cursos_seleccionados=[]
#--------------------------funcion Stringvar()------------------------

#para poder rescatar lo que escribe el usuario en los campos de texto
#se usa una serie de variables con la funcion "Stringvar"
#todos menos el cuadro de texto 
miID=StringVar()
miNombre=StringVar()
miPass=StringVar()
miApellido=StringVar()
miDireccion=StringVar()
misCursos =StringVar()
cursosID= StringVar()
id_curso= StringVar()
nombreCurso= StringVar()
nivel= StringVar()

#----------------------------CAMPOS DE TEXTO----------------
miFrame = LabelFrame(root)
miFrame.pack()
#-------------------- Comienzo de campos ingreso texto ------------------------
cuadroID=Entry(miFrame, textvariable=miID)
cuadroID.grid(row=0, column=1, padx=10, pady=10)

cuadroNombre=Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="right")

cuadroApellido=Entry(miFrame, textvariable=miApellido)
cuadroApellido.grid(row=3, column=1, padx=10, pady=10)

cuadroPass=Entry(miFrame, textvariable=miPass)
cuadroPass.grid(row=2, column=1, padx=10, pady=10)
cuadroPass.config(show="*")

cuadroDireccion=Entry(miFrame, textvariable=miDireccion)
cuadroDireccion.grid(row=4, column=1, padx=10, pady=10)

textoComentario=Text(miFrame, width=16, height=5)
textoComentario.grid(row=5, column=1, padx=10,   pady=10)
scrollVert=Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")

########################## Cursos ##############################
cuadroCursos=Listbox(root, listvariable=misCursos)
cuadroCursos.pack()
###############################################################

textoComentario.config(yscrollcommand=scrollVert.set) 

#---------------------FUNCIONES (FUNCION CONECTAR)--------------------
def advertencia():
    messagebox.showwarning("LA BASE DE DATOS YA FUE CREADA ")

def conectarBBDD():
    miConexion = sqlite3.connect("Usuario.db")
    miCursor = miConexion.cursor()

    try:
        miCursor.execute('''
            CREATE TABLE IF NOT EXISTS DATOS(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE VARCHAR(50),
            PASSWORD VARCHAR(50),
            APELLIDO VARCHAR(25),
            DIRECCION VARCHAR(50),
            COMENTARIOS VARCHAR(255),
            ID_CURSO INTEGER,
            NOMBRE_CURSO VARCHAR(255),
            NIVEL VARCHAR(255),
            FOREIGN KEY (ID_CURSO) REFERENCES CURSOS(CURSO_ID))
        ''')
        miCursor.execute('''
            CREATE TABLE CURSOS(
            CURSO_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE_CURSO VARCHAR(255))
        ''')

        messagebox.showinfo("BBDD", "La BBDD fue creada con exito")    
    except:
        messagebox.showwarning("¡¡¡ATENCION! LA TABLA YA EXISTE")
        advertencia()
    finally: 
        miCursor.close()
        miConexion.close()
#---------------------FUNCIONES (FUNCION DESCONECTAR)--------------------
def desconectarBBDD():
    
    valor=messagebox.askquestion("Salir", "¿Deseas salir de  la aplicacion?")

    if valor=="yes":
        root.destroy()

#---------------------FUNCIONES (FUNCION LIMPIAR CAMPO)--------------------
def limpiarCampos():
    miID.set("")
    miNombre.set("")
    miPass.set("")
    miApellido.set("")
    miDireccion.set("")
    textoComentario.delete(1.0, END)
    misCursos.set("")
    nivel.set("")
    #IDCursos.set("")
    id_curso.set("")
    nombreCurso.set("")

#---------------------FUNCIONES (FUNCION LEER)--------------------
def leer():
    miConexion=sqlite3.connect("Usuario.db")
    miCursor = miConexion.cursor()

    miCursor.execute("SELECT * FROM DATOS WHERE ID=?", (miID.get(),))
    datos = miCursor.fetchall()
    id_usuario = miID.get()

    if id_usuario:
        miConexion = sqlite3.connect("Usuario.db")
        miCursor = miConexion.cursor()
        miCursor.execute("SELECT * FROM DATOS WHERE ID=?", (id_usuario,))
        elUsuario = miCursor.fetchall()
        if elUsuario:
            usuario = elUsuario[0]

            miID.set(usuario[0])
            miNombre.set(usuario[1])
            miApellido.set(usuario[2])
            miPass.set(usuario[3])
            miDireccion.set(usuario[4])
            textoComentario.delete(1.0, END)
            textoComentario.insert(1.0, usuario[5])
            id_curso.set(usuario[6])
            cursos_seleccionados = usuario[7]
            misCursos.set(cursos_seleccionados)
            nivel.set(usuario[7])

           # Obtener los cursos asociados al nivel del usuario seleccionado
            nivel_usuario = usuario[7]
            cursos_nivel = obtener_cursos_por_nivel(nivel_usuario)

            if cursos_nivel:
                cuadroCursos.delete(0, END)  # Limpiar el ListBox antes de mostrar los nuevos cursos
                for curso in cursos_nivel:
                    cuadroCursos.insert(END, curso)
            else:
                cuadroCursos.delete(0, END)  # Limpiar el ListBox si no hay cursos disponibles
                cuadroCursos.insert(END, "No hay cursos disponibles para este nivel")
        else:
            limpiarCampos()
    miCursor.close()
    miConexion.close()
#---------------------FUNCIONES (FUNCION CREAR CAMPO)--------------------
selection = cuadroCursos.curselection()
cursos_seleccionados = cuadroCursos.get(selection[0] if selection else [])
def crear():
    miConexion=sqlite3.connect("Usuario.db")
    miCursor = miConexion.cursor()

    try:
        # Obtener el ID del curso seleccionado
        cursos_seleccionados = cuadroCursos.get(cuadroCursos.curselection())
        """""
        miCursor.execute("SELECT CURSO_ID FROM CURSOS WHERE NOMBRE_CURSO = ?", (curso_seleccionado,))
        curso_id = miCursor.fetchone()[0]
        """
        # Agregar los cursos seleccionados a la lista global
        cursos_seleccionados.append(selection)

        datos = (miNombre.get(), miPass.get(), miApellido.get(), miDireccion.get(), textoComentario.get("1.0", END), curso_id, nivel.get())
        miCursor.execute("INSERT INTO DATOS VALUES (NULL, ?, ?, ?, ?, ?, ?)", datos)
        miConexion.commit()

        messagebox.showinfo("BBDD", "Registros insertados con éxito")
    except sqlite3.Error as error:
        messagebox.showinfo("BBDD", "HAY UN ERROR EN LOS REGISTROS: " + str(error))
    finally:
        miCursor.close()
        miConexion.close()
#---------------------FUNCIONES (FUNCION ACTUALIZAR)--------------------
miConexion = sqlite3.connect("Usuario.db")
miCursor = miConexion.cursor()
id_curso = miCursor.fetchone()[0]
nombreCurso = nombreCurso.get()
def actualizar():
    miConexion = sqlite3.connect("Usuario.db")
    miCursor = miConexion.cursor()
    try:
        # Obtener el ID del curso seleccionado
        cursos_seleccionados = [cuadroCursos.get(indice) for indice in cuadroCursos.curselection()]
        miCursor.execute("SELECT CURSO_ID FROM CURSOS WHERE NOMBRE_CURSO = ?", (nombreCurso.get(),))  
# id_curso.get()
        datos = (miNombre.get(), miPass.get(), miApellido.get(), miDireccion.get(), textoComentario.get("1.0", END), misCursos.get(), miID.get(), nombreCurso.get(),  nivel.get())
        miCursor.execute("UPDATE DATOS SET NOMBRE = ?, PASSWORD = ?, APELLIDO = ?, DIRECCION = ?, COMENTARIOS = ?, NOMBRE_CURSO = ? WHERE ID = ?", datos)
        miConexion.commit()

        messagebox.showinfo("BBDD", "Registro actualizado con éxito")
    except sqlite3.Error as error:
        messagebox.showinfo("BBDD", "HAY UN ERROR AL ACTUALIZAR EL REGISTRO: " + str(error))
    finally:
        miCursor.close()
        miConexion.close()
#---------------------FUNCIONES (FUNCION BORRAR CAMPO)--------------------
def borrar():
    miConexion = sqlite3.connect("Usuario.db")
    miCursor = miConexion.cursor()
    try:
    # Obtener el ID del usuario seleccionado
        id_usuario = miID.get()

        # Obtener el ID del curso asociado al usuario seleccionado
        miCursor.execute("SELECT CURSO_ID FROM DATOS WHERE ID = ?", (id_usuario,))
        resultado = miCursor.fetchone()
        id_curso = resultado[0] if resultado else None
       
       # Eliminar el registro del usuario en la tabla "DATOS"
        miCursor.execute("DELETE FROM DATOS WHERE ID = " + id_usuario)
        miConexion.commit()

        if id_curso:
            miCursor.execute("DELETE FROM CURSOS WHERE CURSO_ID = ?", (id_curso,))
            miConexion.commit()

        messagebox.showinfo("BBDD", "Registro borrado con éxito")
    
    except sqlite3.Error as error:
        messagebox.showinfo("BBDD", "HAY UN ERROR AL BORRAR EL REGISTRO: " + str(error))
    finally:
        miCursor.close()
        miConexion.close()
#------------------FUNCION PARA VER LOS USUARIOS--------------------------
def mostrar_usuarios():
    miConexion = sqlite3.connect("Usuario.db")
    miCursor = miConexion.cursor()

    miCursor.execute("SELECT DATOS.ID, DATOS.NOMBRE, DATOS.APELLIDO, CURSOS.NOMBRE_CURSO FROM DATOS INNER JOIN CURSOS ON DATOS.ID_CURSO = CURSOS.ID_CURSO")
    usuarios = miCursor.fetchall()
    miConexion.commit()
    lista_usuarios = Toplevel(root)
    lista_usuarios.title("Lista de Usuarios")
    lista_usuarios.geometry("400x300")

    lista = Listbox(lista_usuarios, width=50)
    lista.pack(pady=10)

    for usuario in usuarios:
        lista.insert(END, f"ID: {usuario[0]} - Nombre: {usuario[1]} - Apellido: {usuario[2]} - Curso: {usuario[3]}")
    miCursor.close()
    miConexion.close()
#---------------------PANEL TKINTER CON MENU--------------------------------
barraMenu = Menu(root)
root.config(menu=barraMenu, padx=20 , pady=20)

bbddMenu=Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=crear)
bbddMenu.add_command(label="Salir", command=desconectarBBDD)

borrarMenu=Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Limpiar Campos", command=limpiarCampos)

bbddMenu.add_command(label="Mostrar usuarios", command=mostrar_usuarios)

ayudaMenu=Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de...")

barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="LIMPIAR", menu=borrarMenu)
barraMenu.add_cascade(label="AYUDA", menu=ayudaMenu)

#----------------------AQUI COMIENZAN LOS LABEL(primer columna) ------------------------
#aqui ponemos los Nombres de los campos
idLabel=Label(miFrame, text="ID : ")
idLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

nombreLabel=Label(miFrame, text="NOMBRE : ")
nombreLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

apellidoLabel=Label(miFrame, text="APELLIDO : ")
apellidoLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

passLabel=Label(miFrame, text="PASSWORD : ")                  #QUE LA PASSWORD SEA EL ÁREA A LA QUE PERTENECE EL USU
passLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame, text="DIRECCION: ")
direccionLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

comentariosLabel=Label(miFrame, text="COMENTARIOS : ")
comentariosLabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)

#--------------------Seleccionar cursos ----------------------
# Dentro de la función seleccionar_nivel, llama a la función mostrar_cursos_seleccionados
def seleccionar_nivel():                                     
    nivel_seleccionado = combo.get()
    cursos_nivel= obtener_cursos_por_nivel(nivel_seleccionado)                               
    cuadroCursos.delete(0, END) #Limpia el cuadro de texto de cursos

    #print("Opción seleccionada:", cursosLabel)
    for curso in cursos_nivel:
        cuadroCursos.insert(END, curso)
    #mostrar_cursos_nivel()

# Crear una lista de opciones 
niveles = ["Core", "Agricultura de Precision III", "Sistemas", "Comportamentales", "Motores", "Agronomía", "Experiencia del cliente"]

# Crear el Combobox con las opciones
combo = Combobox(root, values=niveles)
combo.pack()

cursoCore =["Service ADVISOR™ 5", "Sistemas Eléctricos y Electrónicos 1", "Sistemas Eléctricos y Electrónicos 2", "Sistemas Eléctricos y Electrónicos 3", "Sistemas Eléctricos y Electrónicos 4", "Sistemas Hidráulicos e Hidrostáticos 1", "Sistemas Hidráulicos e Hidrostáticos 2", "Sistemas Hidráulicos e Hidrostáticos 3", "Sistemas Hidráulicos e Hidrostáticos 4", "Service ADVISOR™ - Métodos y Técnicas", "Sistemas Hidráulicos - Métodos y Técnicas", "Sistemas Eléctricos - Métodos y Técnicas", "Sistemas técnicos- Resumen de las redes de comunicación", "Sistemas - Metrología Dimensional Básica"]
cursoAPIII=["AP - Agricultura de Precisión Fundamentos I", "AP - Operación y Ajustes (GreenStar™ 3)", "AP - Sistemas Técnicos (GreenStar™ 3)", "AP - Centro de Operaciones Evaluación Guía de Venta de Valor", "AP - Sistemas Técnicos y Operación y Ajustes (Gen4)", "AP - AutoTrac™ Vision y AutoTrac™ RowSense™ Introducción Técnica y Ventas", "AP - John Deere Machine Sync para monitores de 4ª generación. Introducción técnica (ES)", "AP - Monitores de Generación 4 Introducción a Ventas", "AP - Receptor Starfire 7000 - Introducción a Ventas", "AP - RTK 450 MHz y 900 MHz Introducción Técnica y Ventas", "Contenido de ventas Highspot - Agricultura de precisión", "Guia de ventas Starfire 7000", "AP- Centro de Operaciones Introduccion Tecnica", "PA - AP - AutoTrac™ Controller Introducción Técnica",  "PA - Descripción técnica de conectividad de JDLink™", "PA - Introduccion Tecnica de la Familia de monitores de 4° Generacion"]
cursoSistemas=["Sistemas - Introducción a John Deere Connected Support", "Sistemas - CCMS (DTAC y DPAC) Visión General", "Sistemas - Gestión de SVAP y Expert Alerts para personal de Servicio"]
cursoComportamentales=["Administrativo - Entrega Técnica", "Administrativo - Proceso de Gestión de Casos de Experiencia del Cliente", "Administrativo - Proceso de Verificación de Contactos para Encuestas a Clientes", "Habilidades de Ventas - Cómo Realizar Demostraciones para Clientes", "Proceso - Sistema Cerrado de Orden de Servicio"]
cursoMotores=["Motores - Introducción Básica Motores Diesel", "Motores - Introducción Básica Motores Diesel", "Motores - Visión General de los Sistemas de Admisión y Escape", "Motores - Visión General de los Sistemas de Combustible", "Motores - Visión General de los Sistemas de Enfriamiento", "Motores - Visión General de los Sistemas de Lubricación", "Motores - Visión General de los Sistemas Eléctricos"]
cursoAgronomía=["Fundamentos Agronómicos - Granos vILT"]
cursoExpCliente=["Administrativo - Experiencia del Cliente Introducción", "Administrativo - Experiencia del Cliente Estrategia", "Administrativo - Experiencia del Cliente Pilar Medición", "Administrativo - Experiencia del Cliente Pilar Conocimiento", "Administrativo - Experiencia del Cliente Pilar Cultura", "Administrativo - Experiencia del Cliente Pilar Gobernanza", "Administrativo - Experiencia del cliente Pilar de innovación"]
cursoMotoresN2=["Motor - Diagnostico de Sistemas de Motores", "Motores - Desmontaje y Montaje", "Motores - Evaluación Introducción y Diagnóstico en Sistemas Eléctricos", "Motores - Evaluación Sistemas de Admisión y Escape", "Motores - Evaluación Sistemas de Combustible", "Motores - Evaluación Sistemas de Lubricación y Enfriamiento"]
cursoTR_5E=["Tractores - Serie 5E 4 Cilindros Introducción Técnica", "Tractores - Serie 5E Diagnóstico","Tractores - Serie 5E Introducción Técnica (Realineación)", "Tractores - Serie 5E Sistemas Técnicos"]
cursoTR_6J=["Tractores - Piezas de Desgaste", "Tractores - Serie 6J Tier 0 Introducción Técnica", "Tractores - Serie 6J Introducción Técnica MY19+"]
cursoTR_7J=["Tractores - Piezas de Desgaste", "Tractores - Serie 7J Tier 0 Introducción Técnica", "Tractores - Serie 7J Sistemas Técnicos", "Tractores - Serie 7J Diagnóstico"]
cursoTR_7R=["Tractores - Piezas de Desgaste", "Tractores - Serie 7R Diagnóstico", "Tractores - Serie 7R Sistemas Técnicos"]
cursoTR_8R=["Tractores - Piezas de Desgaste", "Tractores - Serie 8R Diagnóstico", "Tractores - Serie 8R y 8RT Sistemas Técnicos"]
cursoS550=["Cosechadoras de Granos - Fundamentos", "Cosechadoras de Granos - Plataformas HydraFlex™ Draper 700FD Introducción Técnica y Ventas", "Cosechadoras de Granos - Plataformas Maiceras Serie 600C Introducción a Ventas", "Cosechadoras de Granos - Repuestos", "Cosechadoras de Granos - Serie S500 Diagnóstico", "Cosechadoras de Granos - Serie S500 Introducción a Ventas", "Cosechadoras de Granos - Serie S500 Sistemas Técnicos"]
cursoS700=["Cosechadoras de Granos - Fundamentos", "Cosechadoras de Granos - Plataformas HydraFlex™ Draper 700FD Introducción Técnica y Ventas", "Cosechadoras de Granos - Plataformas Maiceras Serie 600C Introducción a Ventas", "Cosechadoras de Granos - Serie S700 Operación y Ajustes", "Cosechadoras de Granos - Serie S700 Sistemas Técnicos", "Cosechadoras de Granos - Serie S700 Soluciones en Ventas","Cosechadoras de Granos - Serie S700 Diagnóstico", "Cosechadoras de Granos - Repuestos"]

cursos= []
cursos.extend(cursoCore)
cursos.extend(cursoAPIII)
cursos.extend(cursoSistemas)
cursos.extend(cursoComportamentales)
cursos.extend(cursoMotores)
cursos.extend(cursoAgronomía)
cursos.extend(cursoExpCliente)
cursos.extend(cursoMotoresN2)
cursos.extend(cursoTR_5E)
cursos.extend(cursoTR_6J)
cursos.extend(cursoTR_7J)
cursos.extend(cursoTR_7R)
cursos.extend(cursoTR_8R)
cursos.extend(cursoS550)
cursos.extend(cursoS700)

#------------------------- Obtener cursos por nivel------------------------
def obtener_cursos_por_nivel(nivel):
    # Retorna una lista de cursos disponibles por nivel
     if nivel == "Core":                 
        return [cursoCore]      
     elif nivel == "Agricultura de Precision III":
          return [cursoAPIII]
     elif nivel == "Sistemas":
        return [cursoSistemas]
     elif nivel == "Comportamentales":
        return [cursoComportamentales]
     elif nivel == "Motores":
        return [cursoMotores]
     elif nivel == "Agronomía":
        return [cursoAgronomía]
     elif nivel == "Experiencia del cliente":
        return [cursoExpCliente]
     elif nivel == "Motores N2":
        return[cursoMotoresN2]
     elif nivel == "TR 5E":
        return[cursoTR_5E]
     elif nivel == "TR 6J":
        return[cursoTR_6J]
     elif nivel == "TR 7J":
        return[cursoTR_7J]
     elif nivel == "TR 7R":
        return[cursoTR_7R]
     elif nivel == "TR 8R":
        return[cursoTR_8R]
     elif nivel == "S550":
        return[cursoS550]
     elif nivel == "S700":
        return[cursoS700]
         
# Al crear un nuevo registro en la tabla DATOS
#datos_cursos = []
miConexion = sqlite3.connect("Usuario.db")
miCursor = miConexion.cursor()

miCursor.execute("INSERT INTO DATOS (NOMBRE, PASSWORD, APELLIDO, DIRECCION, COMENTARIOS, NIVEL) VALUES (?, ?, ?, ?, ?, ?)",
                 (miNombre.get(), miPass.get(), miApellido.get(), miDireccion.get(), textoComentario.get("1.0", END), nivel.get()))

# Obtener el ID del usuario recién insertado
usuario_id = miCursor.lastrowid
for curso in cursos:
    miCursor.execute("SELECT CURSO_ID FROM CURSOS WHERE NOMBRE_CURSO = ?", (curso,))
    resultado = miCursor.fetchone()
    if resultado is None:
        # El curso no existe en la tabla CURSOS, lo insertamos y obtenemos el nuevo ID
        miCursor.execute("INSERT INTO CURSOS (NOMBRE_CURSO) VALUES (?)", (curso,))
        curso_id = miCursor.lastrowid
    else:
        # El curso ya existe en la tabla CURSOS, obtenemos el ID correspondiente
        curso_id = resultado[0]
miCursor.close()  
miConexion.commit()
#------------------Función para seleccionar un nivel-------------------------
def seleccionar_nivel():
    nivel_seleccionado = combo.get()  # Obtener el nivel seleccionado del Combobox
    nivel.set(combo.get())
    mostrar_cursos_nivel()
    # Obtener los cursos asociados al nivel seleccionado
    cursos_nivel = obtener_cursos_por_nivel(nivel_seleccionado)

    # Mostrar los cursos en el ListBox
    cuadroCursos.delete(0, END)  # Limpiar el ListBox antes de mostrar los nuevos cursos
    
    if cursos_nivel:
        for curso in cursos_nivel:
            cuadroCursos.insert(END, curso)
    else:
        cuadroCursos.insert(END, "No hay cursos disponibles para este nivel")

################Asignar la función "seleccionar_nivel" al botón de selección
botonSeleccionar = Button(root, text="Seleccionar", command=seleccionar_nivel)
botonSeleccionar.pack()
#-----------------Funcion para ctualizar los cursos-----------------------
"""""
def actualizar_cursos_nivel(nivel_seleccionado, indices):
    curso_seleccionado = [cursos.get(indice) for indice in indices]
    # Aquí debo actualizar los cursos seleccionados
    # en la base de datos para la opción seleccionada
"""
#----------------Funcion para mostrar los cursos seleccionados-------------
def mostrar_cursos_nivel():
    nivel_seleccionado = nivel.get()
    miConexion= sqlite3.connect("Usuario.db")
    miCursor= miConexion.cursor()

    miCursor.execute("SELECT * FROM CURSOS WHERE NIVEL=?", (nivel_seleccionado,))
    cursos = miCursor.fetchall()
    ventana_cursos = Toplevel(root)
    ventana_cursos.title("Cursos del Nivel ")
    ventana_cursos.geometry("400x300")
    miCursor.close()
    miConexion.close()
 #--------------Función para guardar los cursos seleccionados-------------

    def guardar_cursos():
            cursos_seleccionados = [checkbox["text"] for checkbox in checkboxes]
            misCursos.set(", ".join(cursos_seleccionados))
            ventana_cursos.destroy()
    
    frame_cursos = Frame(ventana_cursos)
    frame_cursos.pack()
    checkboxes = [] # Lista para almacenar los Checkbuttons
    for i, curso in enumerate(cursos):
        checkboxes = Checkbutton(frame_cursos, text=curso)
        checkboxes.append(checkboxes) # Agregar el Checkbutton a la lista checkboxes

    # Botón para guardar los cursos seleccionados
    boton_guardar = Button(ventana_cursos, text="Guardar", command=guardar_cursos)
    boton_guardar.pack(pady=10)

#------------------Función para mostrar los cursos seleccionados-----
def mostrar_cursos_seleccionados(event):
    seleccion = cuadroCursos.curselection()
    if seleccion:
        indice = seleccion[0]
        cursos_seleccionados = cuadroCursos.get(indice)
        cursos_tooltip = ", ".join(cursos_seleccionados[indice])
        cuadroCursos.tooltip = cursos_tooltip
        cuadroCursos.tooltip_show(event.x_root, event.y_root)
#-------------------FUNCION PARA VER LOS CURSOS DE CADA USUARIO--------------
def ver_cursos():
    seleccion = cuadroCursos.curselection()
    if seleccion:
        indice = seleccion[0]
        usuario_seleccionado = cuadroCursos.get(indice)
        id_usuario = usuario_seleccionado.split(" ")[1]
        
        miConexion = sqlite3.connect("Usuario.db")
        miCursor = miConexion.cursor()

        miCursor.execute("SELECT CURSOS FROM DATOS WHERE ID=" + id_usuario)
        cursos = miCursor.fetchone()[0]
        cursos_separados = cursos.split(",")

        ventana_cursos = Toplevel(root)
        ventana_cursos.title("Cursos del Usuario")
        ventana_cursos.geometry("400x300")

        lista_cursos = Listbox(ventana_cursos, width=50)
        lista_cursos.pack(pady=10)

        for curso in cursos_separados:
             lista_cursos.insert(END, curso)
        miCursor.close()
        miConexion.close()
#---------------------CREAMOS UN FRAME CON BOTONES---------------------
miFrame2 = Frame(root)
miFrame2.pack()

botonCrear=Button(miFrame2, text="CREAR", command=crear)
botonCrear.grid(row=1, column=0, padx=10, pady=10)

botonLeer=Button(miFrame2, text="LEER", command=leer)
botonLeer.grid(row=1, column=1, padx=10, pady=10)

botonActualizar=Button(miFrame2, text="ACTUALIZAR", command=actualizar)
botonActualizar.grid(row=1, column=2, padx=10, pady=10)

botonBorrar=Button(miFrame2, text="BORRAR", command=borrar)
botonBorrar.grid(row=1, column=3, padx=10, pady=10)

botonVerCursos = Button(miFrame2, text="VER CURSOS", command=ver_cursos)
botonVerCursos.grid(row=1, column=4, padx=10, pady=10)

root.mainloop()
miCursor.close()
miConexion.close()
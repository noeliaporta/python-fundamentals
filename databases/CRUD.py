from tkinter import *
from tkinter import messagebox
import sqlite3


class CRUD():

    def __init__(self) -> None:            #init es porque esta inicializando a un archivo que esta en otro lado,a esto se le llama heredando
        pass                               #me dice pass porque no hay nada cargado en la funcion
    
    def formDatos():
        #---------------------INICIO DE PANEL TKINTER --------------------------------
        root=Tk()
        root.title("CRUD")
        #=============================================================================
        #---------------------INICIO DEL MENU ----------------------------------------
        barraMenu=Menu(root)
        root.config(menu=barraMenu, padx=20, pady=20)

        bbddMenu=Menu(barraMenu, tearoff=0)# #este comando no deja abrir una ventana
        bbddMenu.add_command(label="Conectar")
        bbddMenu.add_command(label="Salir")

        borrarMenu=Menu(barraMenu, tearoff=0)
        borrarMenu.add_command(label="Limpiar Campos")

        crudMenu=Menu(barraMenu, tearoff=0)
        crudMenu.add_command(label="Crear")
        crudMenu.add_command(label="Leer")
        crudMenu.add_command(label="Actualizar")
        crudMenu.add_command(label="Borrar")

        ayudaMenu=Menu(barraMenu, tearoff=0)
        ayudaMenu.add_command(label="Licencia")
        ayudaMenu.add_command(label="Acerca de...")

        barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
        barraMenu.add_cascade(label="BORRAR", menu=borrarMenu)
        barraMenu.add_cascade(label="CRUD", menu=crudMenu)
        barraMenu.add_cascade(label="AYUDA", menu=ayudaMenu)

        #======================================================================
        #El método grid es uno de los más empleados y fáciles de utilizar a la hora
        # de empaquetar y posicionar objetos. Ya que recibe como parámetros 
        # row y column, es decir filas y columnas, convirtiendo los widgets 
        # en una tabla bidimensional.
        ######################## INGRESO DEL TEXTO #####################
        #---------------AQUI COMIENZAN LOS LABEL(primer columna) ------------------------
        #aqui ponemos los Nombres de los campos
        miFrame=Frame(root)
        miFrame.pack()

        idLabel=Label(miFrame, text="ID : ")
        idLabel.grid(row=0,column=0, sticky="e", padx=10, pady=10)

        idLabel=Label(miFrame, text="Nombre : ")
        idLabel.grid(row=1,column=0, sticky="e", padx=10, pady=10)

        idLabel=Label(miFrame, text="Apellido : ")
        idLabel.grid(row=2,column=0, sticky="e", padx=10, pady=10)

        idLabel=Label(miFrame,text="Usuario : ")
        idLabel.grid(row=3,column=0, sticky="e", padx=10, pady=10)

        idLabel=Label(miFrame,text="Password : ")
        idLabel.grid(row=4,column=0, sticky="e", padx=10, pady=10)

        idLabel=Label(miFrame,text="Email : ")
        idLabel.grid(row=5,column=0, sticky="e", padx=10, pady=10)

        idLabel=Label(miFrame,text="Comentarios : ")
        idLabel.grid(row=6,column=0, sticky="e", padx=10, pady=10)

        #=============================================================================

        #---------------------CREAMOS UN FRAME CON BOTONES---------------------
        miFrame2 = Frame(root)
        miFrame2.pack()

        botonCrear=Button(miFrame2, text="CREAR")
        botonCrear.grid(row=1, column=0, padx=10, pady=10)

        botonLeer=Button(miFrame2, text="LEER")
        botonLeer.grid(row=1, column=1, padx=10, pady=10)

        botonActualizar=Button(miFrame2, text="ACTUALIZAR")
        botonActualizar.grid(row=1, column=2, padx=10, pady=10)

        botonBorrar=Button(miFrame2, text="BORRAR")
        botonBorrar.grid(row=1, column=3, padx=10, pady=10)

        #=============================================================================
        #=============================================================================
        #-------------------- Comienzo de campos cuadros ------------------------
        #--------------------------funcion Stringvar()------------------------
        #para poder rescatar lo que escribe el usuario en los campos de texto
        #creamos una serie de variable con la funcion "Stringvar"
        #todos menos el cuadro de texto 

        miID=StringVar()
        miNombre=StringVar()
        miApellido=StringVar()
        miUsuario=StringVar()
        miPass=StringVar()
        miEmail=StringVar()
        miComentarios=StringVar()


        cuadroID=Entry(miFrame, textvariable=miID)
        cuadroID.grid(row=0, column= 1, padx=10, pady=10 )

        cuadroNombre=Entry(miFrame, textvariable=miNombre)
        cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
        cuadroNombre.config(fg="red", justify="right")

        cuadroApellido=Entry(miFrame, textvariable=miApellido)
        cuadroApellido.grid(row=3, column=1, padx=10, pady=10)

        cuadroUsuario=Entry(miFrame, textvariable=miUsuario)
        cuadroUsuario.grid(row=2, column=1, padx=10, pady=10)

        cuadroPass=Entry(miFrame, textvariable=miPass)
        cuadroPass.grid(row=4, column=1, padx=10, pady=10)
        cuadroPass.config(show="*")

        cuadroEmail=Entry(miFrame, textvariable=miEmail)
        cuadroEmail.grid(row=5, column=1, padx=10, pady=10)

        textoComentario=Text(miFrame, width=16, height=5)
        textoComentario.grid(row=6, column=1, padx=10,   pady=10)
        scrollVert=Scrollbar(miFrame, command=textoComentario.yview)
        scrollVert.grid(row=6, column=2, sticky="nsew")

        textoComentario.config(yscrollcommand=scrollVert.set)


        root.mainloop()


    formDatos()
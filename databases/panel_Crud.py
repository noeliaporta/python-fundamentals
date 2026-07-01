from tkinter import  *
from tkinter import messagebox

############################inicio del panel Tkinder############################################
ventana = Tk()                                                                                    #al no tener ningun valor podemos agrandar o achicar la ventana como queramos
#============================================================================================
##############################Inicio del menu#############################################
barraMenu = Menu(ventana)
ventana.config(menu=barraMenu, padx=20, pady=20)                                                #pad es para determinar el ancho y el alto del menu(x e y)

#base de datos menu
bbddMenu = Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar")                                                          #add command llama a el comando
bbddMenu.add_command(label="Salir")

borrarMenu = Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Limpiar Campos")
''''
crudMenu = Menu(barraMenu, tearoff=0)                    #
crudMenu.add_command(label="Crear")                      #
crudMenu.add_command(label="Leer")                       # BOTONES
crudMenu.add_command(label="Actualizar")                 #
crudMenu.add_command(label="Borrar")                     #

ayudaMenu = Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Acerca de") 
ayudaMenu.add_command(label="Licencia")

barraMenu.add_cascade(label="BBDD", menu=bbddMenu)        #
barraMenu.add_cascade(label="BORRAR", menu=borrarMenu)    # BARRA 
barraMenu.add_cascade(label="CRUD", menu=crudMenu)        #
barraMenu.add_cascade(label="AYUDA", menu=ayudaMenu)      #
'''''
#===========================================================================================
###################### INGRESO DEL TEXTO ##############################
miFrame = Frame(ventana)
miFrame.pack()

idlabel = Label(miFrame, text="ID: ")
idlabel.grid(row=0, column=0, sticky="e", padx=10,pady=10)

nombrelabel = Label(miFrame, text="NOMBRE: ")
nombrelabel.grid(row=1, column=0, sticky="e", padx=10,pady=10)

passlabel = Label(miFrame, text="PASSWORD: ")
passlabel.grid(row=2, column=0, sticky="e", padx=10,pady=10)

apellidolabel = Label(miFrame, text="APELLIDO: ")
apellidolabel.grid(row=3, column=0, sticky="e", padx=10,pady=10)

direccionlabel = Label(miFrame, text="DIRECCION: ")
direccionlabel.grid(row=4, column=0, sticky="e", padx=10,pady=10)

comentariosLabel=Label(miFrame, text="COMENTARIOS: ")
comentariosLabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)

#===========================================================================================
###################### CREAMOS UN FRAME CON BOTONES ##############################

miFrame2 = Frame(ventana)
miFrame2.pack()

botonCrear = Button(miFrame2, text="CREAR")
botonCrear.grid(row=1, column=0, padx=10,pady=10)

botonLeer = Button(miFrame2, text="LEER")
botonLeer.grid(row=1, column=1, padx=10,pady=10)

botonActualizar = Button(miFrame2, text="Actualizar")
botonActualizar.grid(row=1, column=2, padx=10,pady=10)

botonBorrar = Button(miFrame2, text="BORRAR")
botonBorrar.grid(row=1, column=3, padx=10,pady=10)

#==========================================================================================
#==========================================================================================

#---------------------------funsion stringVar()------------------------
#para poder rescatar lo que escribe el usuario en el campo de texto
#creamos una serie de variables con la funcion "StringVar"
# todos menos el cuadro de texto

miID=StringVar()
miNombre=StringVar()
miPass=StringVar()
miApellido=StringVar()
miDireccion=StringVar()
miUsuario=StringVar()
miPass=StringVar()
miEmail=StringVar()
miComentarios=StringVar()

#-------------------------COMIENZO DE CAMPOS------------------

cuadroID=Entry(miFrame, textvariable=miID)
cuadroID.grid(row=0, column=1, padx=10, pady=10)

cuadroNombre=Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="right")

cuadroApellido=Entry(miFrame, textvariable=miApellido)
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)

cuadroUsuario=Entry(miFrame, textvariable=miUsuario)
cuadroUsuario.grid(row=3, column=1, padx=10, pady=10)

cuadroPass=Entry(miFrame, textvariable=miPass)
cuadroPass.grid(row=4, column=1, padx=10, pady=10)
cuadroPass.config(show="*")

cuadroEmail=Entry(miFrame, textvariable=miEmail)
cuadroEmail.grid(row=5, column=1, padx=10, pady=10)
'''''
cuadroComentario=Entry(miFrame, textvariable=miComentarios)
cuadroComentario.grid(row=6, column=1, padx=10, pady=10)
'''
textoComentario=Text(miFrame, width=16, height=5)
textoComentario.grid(row=6, column=1, padx=10, pady=10)
scrollVert=Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=6, column=2, sticky="nsew")

textoComentario.config(yscrollcommand=scrollVert.set)


ventana.mainloop()
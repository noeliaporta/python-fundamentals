'''''
Pasos a tener en cuenta para conectar un base de datos
1- Abrir - Crear conexion ()
2- Creac Cursor
3- Ejecutar Query (Cosulta) SQL
4- Manejar los resultados de la Query (Consulta)
     1- Insertar, Leer, Actualizar, Borrar(Create, Read, Update, Delete)
5- Cerrar Puntero
6- Cerrar Conexion
'''

import sqlite3

miConexion=sqlite3.connect("PrimeraBase.db")   # cuando le escribo un . estoy llamando a una 
                                              # funcion predeterminada de sqlite3
miCursor=miConexion.cursor() 


miCursor.execute("""
       CREATE TABLE PERSONAS(
       ID INTEGER(4) PRIMARY KEY,
       NOMBRE VARCHAR(20),
       APELLIDO VARCHAR(25),
       EMAIL VANCHAR(50),
       CELULAR VANCHAR(150))
""")


######################################### INGRESO DE DATOS ###########################################

#miCursor.execute("INSERT INTO DATOS('NOMBRE', 'APELLIDO', 'EMAIL', 'CELULAR') VALUES ( 'ALBERTO', 'PATRICIO', 'PATO@GMAIL.COM', '022343567')")

#miConexion.commit()
######################################### INGRESO GRUPO DE DATOS ###########################################

grupodatos=['''
    ('Juan', 'Rodriguez', 'rodri@gmail.com', '115555763'),
    ('Juan', 'Rodriguez', 'rodri@gmail.com', '115555763'),
    ('Juan', 'Rodriguez', 'rodri@gmail.com', '115555763')"
           ''']
'''''
miCursor.execute("INSERT INTO DATOS('NOMBRE', APELLIDO', 'EMAIL', 'CELULAR') VALUES('Juan', 'Rodriguez', 'rodri@gmail.com', '115555763')")

miConexion.commit()
'''
"""
for datos in grupodatos:
       print(datos)
"""

#miCursor.execute("SELECT FROM DATOS ")

#miCursor.commit()



miCursor.close()

miConexion.close()

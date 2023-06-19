"""
Opción 1
● Grabar: Corresponde a guardar ciertos datos de un vehículo, entre ellos: Tipo, patente, marca y precio, multas (monto y
fecha), fecha de registro del vehículo y nombre del dueño.
Además, debe verificar que la patente sea correcta, la marca considere entre 2 y 15 caracteres y el precio sea mayor a
$5.000.000.
Opción 2
● Buscar: Corresponde buscar un auto por su patente y mostrar toda su información almacenada."""

"""
Opción 3
● Imprimir certificados: Esta opción permite imprimir los certificados de Emisión de contaminantes, de anotaciones vigentes
y de multas. Estos deben ser previamente ingresados con valores aleatorios entre $1.500 y $3.500. Al imprimir el certificado,
debe mostrar el nombre del certificado, la patente del auto y los datos del dueño actual.
Opción 4
● Salir. Corresponde a salir del programa emitiendo un mensaje de salida. Considere, además, su nombre y apellido y la
versión del programa.
"""
"""
1. Diseñe un menú con las opciones para acceder a cada función requerida.
2. Cree las funciones solicitadas por cada requerimiento
3. Considere el ingreso de datos y el despliegue de información. """


import numpy as np

tipo=[]
Patente=[]
Marca=[]
Precio=[]
Multas=[]
Fregistro=[]
NomDueño=[]



def grabar():
    info=()
    tipo=input("Ingrese el tipo de vehiculo")
    info.append(tipo)

    Patente=input("Ingrese la Patente del vehiculo ")
    info.append(Patente)

    precio=input("Ingresa precio Auto")
    info.append(precio)

    Multas=input("Ingresa la cantidad de Multas")
    info.append(Multas)

    Fregistro=input("Ingrese fecha de registro")
    info.append(Fregistro)

    NomDueño=input("Ingrese Nombre del dueño")
    info.append(NomDueño)




op=0
while op!=4:
    print("------------------------")
    print("Automotora -Auto Seguro-")
    print("1. Grabar")
    print("2. Buscar")
    print("3. imprimer certificado")
    print("4. Salir")
    print("------------------------")

    op=int(input("Ingrese una opcion:"))
    if op==1:
        print("Grabar Datos")
        print("----------------------------------")
        tipo=input("Ingrese el tipo de vehiculo: ")
        Patente=input("Ingrese la Patente del vehiculo: ")
        Marca=input("Ingresela Marca del Vehiculo")
        Precio=int(input("Ingrese Valor del Vehiculo: "))
        Multas=int(input("Ingrese la cantidad de Multas:"))
        Fregistro=input("Indique la Fecha de registro:")
        NomDueño=input("Ingrese nombre del dueño:")
        print("----------------------------------")

    elif op==2:
        print("Buscar")   


    elif op==3:
        print("Imprimir certificado")    

    elif op==4:
        print("Salir")
    break    
    

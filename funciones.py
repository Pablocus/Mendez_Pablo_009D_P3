import time
import os
import msvcrt
import numpy

lista_ruts = []
lista_nombres = []
lista_nombres_mascotas = []
lista_dias = []
lista_id = []
habitaciones = numpy.zeros((2,5),int)

def mostrar_menu():
    os.system('clr')
    print("""¿Que desea hacer?:
        1. Grabar
        2. Buscar
        3. Retirarse
        4. Salir""")
    opc = validar_opcion()
    return opc

def validar_opcion():
    while True:
        try:
            opc = int(input("Ingrese opción: "))
            if opc in(1,2,3,4):
                return opc
            else:
                print("ERROR! OPCIÓN INCORRECTA!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO!")
            
def grabar_mascota():
    if habitaciones == 0:
        rut = validar_rut()
        nom = validar_nombre()
        nom_mas = validar_nombre_mascota()
        dia = validar_dias()
        id = id_mascota()
        
    
        

def validar_rut():
    os.system('clr')
    while True:
        try:
            rut = int(input("Ingrese su rut, sin puntos ni digito verificador: "))
            if rut >= 1000000 and rut <= 99999999:
                return rut
            else:
                print("ERROR! RUT ENTRE 1000000 Y 99999999!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")
            
def validar_nombre():
    while True:
        nom = input("Ingrese su nombre: ")
        if len(nom.strip()) >= 3 and nom.isalpha():
            return nom
        else:
            print("ERROR! DEBE TENER AL MENOS 3 LETRAS!")
            
def validar_nombre_mascota():
    while True:
        nom_mas = input("Ingrese su nombre: ")
        if len(nom_mas.strip()) >= 3 and nom_mas.isalpha():
            return nom_mas
        else:
            print("ERROR! DEBE TENER AL MENOS 3 LETRAS!")
            
def validar_dias():
    while True:
        try:
            dia = int(input("Ingrese la cantidad de dias que se va a quedar su mascota: "))
            if dia >= 1:
                return dia
            else:
                print("ERROR! DEBE SER AL MENOS 1 DIA!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO!")
            
def habitacion():
    os.system('clr')
    print("Habitaciones del Hotel:\n")
    contador = 1
    for x in range(2):
        print(f"Piso {contador}: ", end=" ")
        for y in range(5):
            print(f"habitacion {contador}: {habitaciones[x][y]}", end=" ")
            contador = contador + 1
    print("\n")
            
def id_mascota():
    contador = 1
    while True:
        if contador in lista_id:
            contador = contador + 1
        else:
            break
    id = contador
    return id
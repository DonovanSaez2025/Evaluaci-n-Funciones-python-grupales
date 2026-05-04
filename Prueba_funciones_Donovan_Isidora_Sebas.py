import os
"""1. Crear una función que reciba una lista de números enteros y genere una nueva lista solo con los números pares mayores a 10.
Luego debe mostrar la nueva lista y la cantidad de elementos encontrados. """
#Código Isidora
def numerosParesMayores(listado):
    paresMayor10 = []
    for i in range(0, len(listado)):
        if listado[i] % 2 == 0 and listado[i] > 10:
            paresMayor10.append(str(listado[i]))
    print(f"Números pares mayores a 10: {", ".join(paresMayor10)}")

def ejercicio1():
    limit = int(input("Ingresa un límite de números: "))
    listado = []
    for i in range(0, limit):
        num = int(input("Ingresa un número entero: "))
        listado.append(num)
    numerosParesMayores(listado)


'''Crear una función que reciba una lista de notas (decimales) y genere dos listas: 
una con aprobados (≥ 4.0) y otra con reprobados (< 4.0).
Debe mostrar ambas listas y la cantidad de estudiantes en cada grupo.'''
#Código Sebastián
def revisarNotas(lista):
    aprobados = []
    reprobados = []
    for i in range(0, len(lista)):
        if lista[i] < 4.0:
            reprobados.append(str(lista[i]))
        else:
            aprobados.append(str(lista[i]))
    print(f"\nalumnos reprobados: {len(reprobados)}\nnotas: {" - ".join(reprobados)}")
    print(f"alumnos aprobados: {len(aprobados)}\nnotas: {" - ".join(aprobados)}")

def ejercicio2():
    limite = int(input("Ingrese un limite de notas: "))
    listaNotas = []
    i = 0
    while i < limite:
        nota = float(input("Ingrese la nota de un estudiante: "))
        if nota < 1.0 or nota > 7.0:
            print("Nota inválida")
        else: 
            print("Nota agregada con éxito")
            listaNotas.append(nota)
            i += 1
    revisarNotas(listaNotas) # va a agarra la listaNotas


'''3. Crear una función que reciba una lista de edades y
clasifique a las personas en tres grupos: menores de edad, adultos y adultos mayores (60+). 
Debe mostrar la cantidad de personas en cada grupo.'''
#Código Donovan
def clasificarEdades(listaEdades):
    menoresEdad = 0
    adultos = 0
    adultosMayores = 0
    print("\nClasificando por edades...")
    for i in range(0, len(listaEdades)):
        if listaEdades[i] < 18:
            menoresEdad += 1
        elif listaEdades[i] >= 18 and listaEdades[i] < 60:
            adultos += 1
        else:
            adultosMayores += 1
    if menoresEdad == 0:
        print("Menores de edad: no se han detectado menores de edad.")
    elif menoresEdad == 1:
        print(f"Menores de edad: {menoresEdad} detectado.")
    else:
        print(f"Menores de edad: {menoresEdad} detectados. ")
    if adultos == 0:
        print("Adultos: no se han detectado adultos.")
    elif adultos == 1:
        print(f"Adultos: {adultos} detectado.")
    else:
        print(f"Adultos: {adultos} detectados. ")
    if adultosMayores == 0:
        print("Adultos mayores: no se han detectado adultos mayores.")
    elif adultosMayores == 1:
        print(f"Adultos mayores: {adultosMayores} detectado.")
    else:
        print(f"Adultos mayores: {adultosMayores} detectados. ")

def ejercicio3():
    limite = int(input("Ingresa un límite de valores: "))
    listaEdades = []
    i = 0
    while i < limite:
        edad = int(input("Ingrese la edad de una persona: "))
        if edad < 0 or edad > 123:
            print("Edad imposible.")
        else:
            listaEdades.append(edad)
            print("Registrado correctamente.")
            i+=1
    clasificarEdades(listaEdades)


# Limpiar consola
def limpiarConsola():
    os.system('cls')

#Menu while
while True:
    print("\n--- Ejercicios grupo 6 ---")
    print("--- Ejercicio 1: Isidora Valenzuela ---")
    print("--- Ejercicio 2: Sebastián Bustamante ---")
    print("--- Ejercicio 3: Donovan Sáez ---")
    opcion = int(input("Selecciona un ejercicio (1-3): "))
    if opcion == 1:
        limpiarConsola()
        print("Ejecutando ejercicio 1...")
        ejercicio1()
    elif opcion == 2:
        limpiarConsola()
        print("Ejecutando ejercicio 2...")
        ejercicio2()
    elif opcion == 3:
        limpiarConsola()
        print("Ejecutando ejercicio 3...")
        ejercicio3()
    elif opcion == 0:
        print("Saliendo...")
        break
    else:
        print("Opción inválida.")
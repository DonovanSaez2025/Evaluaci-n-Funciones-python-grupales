import os
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
    #Imprimir menores de edad
    if menoresEdad == 0:
        print("Menores de edad: no se han detectado menores de edad.")
    elif menoresEdad == 1:
        print(f"Menores de edad: {menoresEdad} detectado.")
    else:
        print(f"Menores de edad: {menoresEdad} detectados. ")
    #Imprimir adultos
    if adultos == 0:
        print("Adultos: no se han detectado adultos.")
    elif adultos == 1:
        print(f"Adultos: {adultos} detectado.")
    else:
        print(f"Adultos: {adultos} detectados. ")
    #Imprimir adultos mayores
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
Continue = True
while Continue:
    print("\n--- Ejercicios grupo 6 ---")
    print("--- Ejercicio 3: Donovan Sáez ---")
    opcion = input("Selecciona un ejercicio (1-3): ")
    if opcion == "3":
        limpiarConsola()
        print("Ejecutando ejercicio 3...")
        ejercicio3()
    elif opcion == "0":
        print("Saliendo...")
        Continue = False
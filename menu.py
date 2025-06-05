import datetime
import random

def mostrar_menu():
    print("1.- X tabla de multiplicar")
    print("2.- Par o impar")
    print("3.- If anidado")
    print("4.- Fórmula")
    print("5.- N = control")
    print("6.- Salir")

def tabla_multiplicar():
    print("Seleccionaste x tabla de multiplicar")
    for u in range(1, 11):
        print(f"Tablas de multiplicar del {u}:")
        for e in range(1, 11):
            producto = u * e
            print(f"{u} x {e} = {producto}")
        print()

def par_impar():
    print("Seleccionaste par o impar")
    numero = int(input("Ingresa un número: "))
    if numero % 2 == 0:
        print(f"El número {numero} es par.")
    else:
        print(f"El número {numero} es impar.")

def if_anidado():
    print("Seleccionaste if anidado")
    n1 = int(input("Ingresa tu calificación: "))
    if n1 == 100:
        print("¡Excelente, felicidades!")
    elif 90 <= n1 <= 99:
        print("Muy bien")
    elif 80 <= n1 <= 89:
        print("Bien")
    elif 70 <= n1 <= 79:
        print("Alumno regular")
    else:
        print("Alumno no aprobado")

def formula():
    print("Seleccionaste fórmula")
    # Aquí puedes agregar cualquier fórmula que desees implementar
    x=int(input("ingresa un numero: "))
    a=1
    suma=0
    while a<=x:
        b = 2
        while b<x+2:
            c= pow(a,b)
            suma = suma+c
            resultado = suma/x
            a = a+1
            b = b+1
        print ("el resultado es: ", resultado)

def numero_control():
    print("Seleccionaste número de control")
    year = datetime.datetime.now().year
    print("¿Cuál es tu periodo 1 o 2?")
    print("A = 1 (otra escuela fábrica)")
    print("B = 2 (admisión en el tecnológico)")
    respuesta = input("Ingresa 1 o 2: ")

    if respuesta == "1":
        print("Elegiste la opción 1")
    elif respuesta == "2":
        print("Elegiste la opción B")
    else:
        print("Opción inválida")
        return

    print("¿De qué carrera eres?")
    carreras = [
        "1. Ing. Industrial",
        "2. Ing. TICS",
        "3. Ing. Sistemas Computacionales",
        "4. Ing. Química",
        "5. Ing. Civil",
        "6. Ing. Mecatrónica",
        "7. Ing. Eléctrica",
        "8. Ing. Logística",
        "9. Ing. Administración de Empresas"
    ]
    for carrera in carreras:
        print(carrera)
    
    respuesta2 = input("Ingresa el número de tu carrera: ")

    carrera_elegida = None
    if respuesta2 == "1":
        carrera_elegida = "Ing. Industrial"
    elif respuesta2 == "2":
        carrera_elegida = "Ing. TICS"
    elif respuesta2 == "3":
        carrera_elegida = "Ing. Sistemas Computacionales"
    elif respuesta2 == "4":
        carrera_elegida = "Ing. Química"
    elif respuesta2 == "5":
        carrera_elegida = "Ing. Civil"
    elif respuesta2 == "6":
        carrera_elegida = "Ing. Mecatrónica"
    elif respuesta2 == "7":
        carrera_elegida = "Ing. Eléctrica"
    elif respuesta2 == "8":
        carrera_elegida = "Ing. Logística"
    elif respuesta2 == "9":
        carrera_elegida = "Ing. Administración de Empresas"
    else:
        print("Opción inválida")
        return

    numero_aleatorio = random.randint(1, 999)
    print(f"{year}{respuesta}{respuesta2}{numero_aleatorio}")

def main():
    while True:
        mostrar_menu()
        respuesta = input("Selecciona una opción: ")

        if respuesta == "1":
            tabla_multiplicar()
        elif respuesta == "2":
            par_impar()
        elif respuesta == "3":
            if_anidado()
        elif respuesta == "4":
            formula()
        elif respuesta == "5":
            numero_control()
        elif respuesta == "6":
            print("Seleccionaste la opción de salir")
            print("Cerrando código")
            break
        else:
            print("Opción inválida, por favor intenta de nuevo.")

if __name__ == "__main__":
    main()

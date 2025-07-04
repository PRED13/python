import random

# Generar un número aleatorio entre 1 y 10
numero_secreto = random.randint(1, 10)

# Inicializar la variable de intento del usuario
intento = 0

print("¡Bienvenido al juego de Adivina el Número!")
print("Estoy pensando en un número del 1 al 10. ¿Puedes adivinar cuál es?")

# Bucle hasta que el usuario adivine el número
while intento != numero_secreto:
    intento = int(input("Ingresa tu número: "))

    if intento < numero_secreto:
        print("El número es mayor. Intenta de nuevo.")
    elif intento > numero_secreto:
        print("El número es menor. Intenta de nuevo.")

print(f"¡Felicidades! Adivinaste el número {numero_secreto}.")

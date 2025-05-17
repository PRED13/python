def calculadora(a, b, operacion):
    if operacion == 'suma':
        return a + b
    elif operacion == 'resta':
        return a - b
    elif operacion == 'multiplicacion':
        return a * b
    elif operacion == 'division':
        return a / b if b != 0 else "Error: División por cero"
    else:
        return "Operación no válida"

# Ejemplo de uso
print(calculadora(10, 5, 'suma'))  # 15

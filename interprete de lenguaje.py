def interprete(instrucciones):
    variables = {}

    for linea in instrucciones:
        partes = linea.split()
        comando = partes[0]

        if comando == "SET":
            var, val = partes[1], int(partes[2])
            variables[var] = val

        elif comando == "ADD":
            var, val = partes[1], int(partes[2])
            if var in variables:
                variables[var] += val
            else:
                raise ValueError(f"Variable no definida: {var}")

        elif comando == "MUL":
            var, val = partes[1], int(partes[2])
            if var in variables:
                variables[var] *= val
            else:
                raise ValueError(f"Variable no definida: {var}")

        elif comando == "PRINT":
            var = partes[1]
            if var in variables:
                print(f"{var} = {variables[var]}")
            else:
                raise ValueError(f"Variable no definida: {var}")

        else:
            raise SyntaxError(f"Instrucción no válida: {linea}")

# Prueba
instrucciones = [
    "SET x 10",
    "ADD x 5",
    "MUL x 3",
    "PRINT x"
]
interprete(instrucciones)

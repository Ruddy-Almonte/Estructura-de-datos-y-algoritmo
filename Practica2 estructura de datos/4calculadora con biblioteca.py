
import operator

# Diccionario para mapear el operador a la función correspondiente
operaciones = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

# Solicitar datos
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
operacion = input("Ingresa la operación (+, -, *, /): ")


if operacion in operaciones:
    try:
        resultado = operaciones[operacion](a, b)
        print("Resultado:", resultado)
    except ZeroDivisionError:
        print("Error: División por cero")
else:
    print("Operación no válida")

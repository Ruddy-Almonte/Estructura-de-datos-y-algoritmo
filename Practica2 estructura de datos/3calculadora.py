
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
operacion = input("Ingresa la operación (+, -, *, /): ")

if operacion == "+":
    print("Resultado:", sumar(a, b))
elif operacion == "-":
    print("Resultado:", restar(a, b))
elif operacion == "*":
    print("Resultado:", multiplicar(a, b))
elif operacion == "/":
    print("Resultado:", dividir(a, b))
else:
    print("Operación no válida")



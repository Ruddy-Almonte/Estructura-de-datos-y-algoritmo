
# 10 Sumar números hasta que el usuario ingrese 0

suma = 0
while True:
    numero = float(input("Ingresa un número (0 para salir): "))
    if numero == 0:
        break
    suma += numero
print(f"La suma total es: {suma}")

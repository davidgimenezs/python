def factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)

numero = int(input())
resultado = factorial(numero)
print(resultado)

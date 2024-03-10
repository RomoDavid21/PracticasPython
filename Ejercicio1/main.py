
print("Ingrese un numero entre el 1 y el 100:")

def verificar(numero):
    if numero % 2 == 0:
        return f'El número {numero} es par.'
    else:
        return f'El número {numero} es impar.'

dato = int(input("Ingrese un número: "))

print(verificar(dato))
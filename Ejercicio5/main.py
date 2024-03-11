
def acronimo():
    significado = input("Ingrese el significado completo de una organización o concepto: ")

    acronimo = ''.join(word[0].upper() for word in significado.split())

    print("Acronimo:", acronimo)

acronimo()

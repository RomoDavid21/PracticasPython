def es_palindromo(word):
    return word == word[::-1]

palabras = []
for i in range(5):
    palabra = input(f"Ingrese la palabra #{i + 1}: ")
    palabras.append(palabra.lower()) 

palindromes = []
no_palindromes = []
for palabra in palabras:
    if es_palindromo(palabra):
        palindromes.append(palabra)
    else:
        no_palindromes.append(palabra)

# Mostrar los resultados
print("\nPalíndromos:")
for palindrome in palindromes:
    print(palindrome)

print("\nNo palíndromos:")
for no_palindrome in no_palindromes:
    print(no_palindrome)

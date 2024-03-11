from canciones import *

lista = {
  "Imagine Dragons - Bones": Bones,
  "Imagine Dragons - Enemy": Enemy,
  "Alex Ubago - Sigo Aqui": SigoAqui, 
  "What Could Have Been - Ray Chen y Sting": What,
  "I Wanna Be Your Slave - Måneskin": Slave
}

# Imprime la lista de canciones
print("Lista de canciones:")
for i, song in enumerate(lista, 1):
  print(f"{i}. {song}")

# Pedir al usuario que elija una canción
opcion = int(input("Elige una canción (1-5): "))

# Verificar si la opción del usuario es válida
if opcion < 1 or opcion > 5:
  print("Opción inválida")
else:
 
  titulo = list(lista.keys())[opcion - 1]
  letra = lista[titulo]

  print(f"\nElejiste: '{titulo}' Aqui tienes. \n\n --------------- {titulo}--------------- \n{letra}")

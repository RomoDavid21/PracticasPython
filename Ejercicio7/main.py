import random

numero = random.randrange(1,100)
adivina = int(input("Adivinna un numero entre 1 - 100:  "))


while adivina != numero:
    if (adivina < numero):
        print("Elije un numero mas alto. Intentalo otra vez")
        adivina = int(input("\nAdivina un numero entre 1 - 100:  "))
    else:
        print("Elije un numero mas bajo. Intentalo otra vez")
        guess = int(input("\nAdivina un numero entre 1 - 100:  "))

print("Adivinaste el numero, felicidades.")
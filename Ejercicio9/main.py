
cuenta = float(input("¿Cuánto es la cuenta? "))

personas = int(input("¿Cuantas personas hay en la mesa? "))

propina = input("¿Cuánto vamos a dejar de propina?\n 1) 15%\n 2) 20%\n 3) 25%\n")

if propina == '1':
    porcentaje = 0.18
elif propina == '2':
    porcentaje = 0.20
elif propina == '3':
    porcentaje = 0.25
else:
    print("Opción inválida, vuelva a ingresar los datos.")
    exit()  

total = (cuenta * (1 + porcentaje)) / personas

## Mostramos al usuario el resultado
print("El total a pagar entre ",personas," con una propina del", porcentaje * 100, "% es  de:", total)


bandera=True
while bandera== True:
    nombre = input("Ingresa tu nombre:  ")
    option = input("Tu nombre es correcto?(y/n):  ")
    if(option=="y"):
        bandera = False


bandera=True
while bandera== True:
    fecha = input("Ingresa tu fecha de nacimiento:  ")
    option = input("Tu fecha de nacimiento es correcta?(y/n):  ")
    if(option=="y"):
        bandera = False


bandera=True
while bandera== True:
    direccion = input("Ingresa tu direccion:  ")
    option = input("Tu direccion es correcta?(y/n):  ")
    if(option=="y"):
        bandera = False


bandera=True
while bandera== True:
    objetivo = input("Ingresa una meta personas:  ")
    option = input("Tu meta es correcta?(y/n):  ")
    if(option=="y"):
        bandera = False

#Imprime Datos
print("- Name: ",nombre)
print("- Date of birth: ",fecha)
print("- Address: ",direccion)
print("- Personal Goals: ",objetivo)
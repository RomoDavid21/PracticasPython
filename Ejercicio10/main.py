
email = input("Ingresa tu correo electronico:  ").strip()
usuario = email[:email.index('@')]
dominio = email[email.index('@')+1:]

if dominio == "gmail.com":
    annex = "tu dominio es de google."
elif dominio == "outlook.com":
    annex = "tu dominio es de microsoft."
elif dominio == "hotmail.com":
    annex = "tu dominio es de microsoft."
elif dominio == "uabc.edu.mx":
    annex = "tu dominio es de UABC."
else:
    annex = "tu dominio es genial."

result = "Tu nombre de ususario es: "+usuario+"\nTu dominio es: "+dominio+", "+annex

print(result)
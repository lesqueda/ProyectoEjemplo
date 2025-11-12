usuario = input("Ingrese su usuario: ")
password = input("Ingrese su contraseña: ")

if (usuario == "usuario1" and password == "password"):
    print("el usuario pudo ingresar en el sistema")

elif (usuario != "usuario1" and password == "password"):
    print("El usuario no existe en el sistema")

elif (usuario == "usuario1" and password != "password"):
    print("la contraseña es incorrecta")

else:
    print("el usuario no pudo ingresar en el sistema")
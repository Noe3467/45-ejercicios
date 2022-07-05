"""
Escribí un programa que solicite ingresar un nombre de usuario y una contraseña.
Si el nombre es “Gwenevere” y la contraseña es “excalibur”, mostrar en pantalla
“Usuario y contraseña correctos. Puede ingresar a Camelot”. Si el nombre o la contraseña no coinciden,
mostrar “Acceso denegado”. 
"""

#login nuevo - ejercicio modificado
print("vamos a crear tu login.. Seguì las instrucciones..")

nombreUser = input("ingresà el nombre de usuario con el que querès registrarte: ")
passUser = input("ingresa una conttraseña segura: ")

print("bien, tu usuario fue creado correctamente, volvè a ingresar las credenciales.\n")

print("ingresà tu nombre de usuario: ")
nombreUserLog = input()

print("ingresà la contraseña: ")
passUserLog = input()

if nombreUser == nombreUserLog and passUser == passUserLog:
    print("Usuario y contraseña correctos. Puede ingresar a Camelot")
else:
    print("Acceso denegado, usuario o contraseña incorrecto/s")

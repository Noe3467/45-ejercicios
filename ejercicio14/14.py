"""
Escribí un programa que, dada una cadena de texto por el usuario, imprima True
si la cantidad de caracteres en la cadena es un número impar, o False si no lo es.
"""

texto = input("ingresà un pequeño texto: ")

if len(texto) % 2 == 0:
    print(True)
else:
    print(False)
"""
Escribí un programa que le pida al usuario ingresar dos palabras y las guarde en dos variables,
y que luego imprima True si la primera palabra es menor que la segunda o False si no lo es. 
"""

palabra1 = input("ingresà la primer palabra: ")
palabra2 = input("ingresà la segunda palabra: ")

#mi soluciòn
"""
if len(palabra1) < len(palabra2):
    print(True)
else:
    print(False)
"""

#como ver si la inicial va antes alfabeticamente 
if palabra1 > palabra2:
    print(True)
else:
    print(False)
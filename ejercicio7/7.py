"""
Escribí un programa que solicite al usuario un número y
le reste el 15%, almacenando todo en una única variable.
A continuación, mostrar el resultado final en pantalla. 
"""

numero = float(input("ingresà un nùmero: "))

resta15 = numero - ((numero*15) / 100)

print(f"El nùmero final con un 15% menos es: {resta15}")

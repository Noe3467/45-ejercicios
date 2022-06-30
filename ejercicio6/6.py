"""
Escribí un programa que solicite al usuario ingresar
tres números para luego mostrarle el promedio de los tres. 
"""

i = 0
suma = 0
promedio = 0

for i in range(3):
    num = float(input(f"ingresà el {i+1}ª nùmero: "))
    suma = suma + num

promedio = suma/3

print(f"El promedio de los nùmeros que ingresaste es: {promedio}")

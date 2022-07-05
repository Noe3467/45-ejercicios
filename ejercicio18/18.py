"""
Escribí un programa que solicite al usuario el ingreso de dos números diferentes
y muestre en pantalla al mayor de los dos. 
"""

num1 = float(input("ingresà el primer nùmero: "))
num2 = float(input("ingresà el segundo nùmero: "))

if num1 > num2:
    print(f'El mayor de los nùmeros que ingresaste es: {num1}')
else:
    print(f'El mayor de los nùmeros que ingresaste es: {num2}')

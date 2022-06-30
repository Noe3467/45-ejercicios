"""
Escribí un programa que solicite al usuario el ingreso de
una temperatura en escala Fahrenheit (debe permitir decimales) y
le muestre el equivalente en grados Celsius. La fórmula de conversión
que se usa para este cálculo es: _Celsius = (5/9) * (Fahrenheit-32)_
"""

fahrenheit = float(input("ingresà la temperatura en grados Fahrenheit: "))
celsius = (5/9) * (fahrenheit - 32)

print(f"La temperatura {fahrenheit}ºF equivale a {celsius} ºC")


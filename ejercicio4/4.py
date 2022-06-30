"""
Escribí un programa que solicite al usuario ingresar la cantidad de kilómetros
recorridos por una motocicleta y la cantidad de litros de combustible que consumió
durante ese recorrido. Mostrar el consumo de combustible por kilómetro.
"""

kilometros = float(input("ingresà la cantidad de kilòmetros que recorriste con tu motocicleta: "))
combustible = float(input("ingresà la cantidad de combustible que utilizaste en todo lo que recorriste (en litros): "))

resultado = combustible/kilometros

print(f"El consumo de combustible por kilòmetro fue de {resultado} litros")

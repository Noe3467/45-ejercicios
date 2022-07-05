"""
Escribí un programa para solicitar al usuario tres números y mostrar en pantalla al menor de los tres. 
"""

numero1 = float(input('ingresà el primer nùmero: '))
numero2 = float(input('ingresà el segundo nùmero: '))
numero3 = float(input('ingresà el tercer nùmero: '))

if (numero1 < numero2) and (numero1 < numero3):
    print(f'El menor de los nùmeros que ingresaste es: {numero1}')

elif (numero2 < numero1) and (numero2 < numero3):
    print(f'El menor de los nùmeros que ingresaste es: {numero2}')

else:
    print(f'El menor de los nùmeros que ingresaste es: {numero3}')
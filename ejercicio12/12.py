"""
Escribí un programa para solicitar al usuario el ingreso de un número entero y que
luego imprima un valor de verdad dependiendo de si el número es par o no.
Recordar que un número es par si el resto, al dividirlo por 2, es 0. 
"""
numero = int(input("ingresà un nùmero: "))

if numero %2 == 0:
    print(f"El nùmero {numero} es PAR")
    
else:
    print(f"El nùmero {numero} es IMPAR")

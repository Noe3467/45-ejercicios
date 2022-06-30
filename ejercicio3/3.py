"""
Escribí un programa que solicite al usuario dos números
y los almacene en dos variables. En otra variable,
almacená el resultado de la suma de esos dos números
y luego mostrá ese resultado en pantalla.
A continuación, el programa debe solicitar al usuario que
ingrese un tercer número, el cual se debe almacenar en
una nueva variable. Por último, mostrá en pantalla el resultado de
la multiplicación de este nuevo número por el resultado de la suma anterior. 
"""

numero1 = float(input("Ingresà el primer nùmero para sumar: "))
numero2 = float(input("ingresà el segundo nùmero para sumar: "))
numero3 = int(input("ingresà el tercer nùmero para multiplicarlo por la suma de los dos anteriores: "))

suma = numero1 + numero2
multiplicacion = suma * numero3

print(f"El resultado de {numero1} + {numero2} = {suma} y la operaciòn final al multiplicarlo por {numero3} es: {multiplicacion}")

"""
Escribí un programa que solicite al usuario que ingrese cuántos shows musicales ha visto en
el último año y almacene ese número en una variable. A continuación mostrar en pantalla un valor
de verdad (True o False) que indique si el usuario ha visto más de 3 shows. 
"""
show = int(input("ingresà la cantidad de shows musicales que viste este año: "))

if show > 3:
    print(True)
else:
    print(False)
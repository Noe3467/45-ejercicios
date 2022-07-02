"""
Escribí un programa que le solicite al usuario su edad y la guarde en una variable.
Que luego solicite la cantidad de artículos comprados en una tienda y la guarde en otra variable.
Finalmente, mostrar en pantalla un valor de verdad (True o False) que indique
si el usuario es mayor de 18 años de edad y además compró más de 1 artículo. 
"""

edad = int(input("ingresà tu edad: "))
articulos = int(input("ingresà la cantidad de artìculos que compraste: "))

if (edad >= 18) & (articulos >1):
    print(True)
    print(f"Sos mayor de edad, tenès {edad} años y compraste {articulos} artìculos")

if (edad >= 18) & (articulos ==1):
    print(False)
    print(f"Sos mayor de edad, tenès {edad} años pero compraste solo 1 artìculo")

if (edad < 18) & (articulos >1):
    print(False)
    print(f"Sos menor de edad, tenès {edad} años y compraste {articulos} artìculos")
elif (edad < 18) & (articulos ==1):
    print(False)
    print(f"Sos menor de edad, tenès {edad} años y compraste solo 1 artìculo")

if (edad >=18) & (articulos < 1):
    print(False)
    print(f"Sos mayor de edad, tenès {edad} años pero no compraste al menos un artìculo")

if (edad < 18) & (articulos <1):
        print(False)
        print("¡No solo sos menor de edad sino que no compraste ningùn artìculo!")







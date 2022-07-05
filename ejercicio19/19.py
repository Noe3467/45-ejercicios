"""
Escribí un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje “Es vocal”.
Verificar si el usuario ingresó un string de más de un carácter y, en ese caso,
informarle que no se puede procesar el dato. 
"""

letra = (input('ingresà una letra: '))

if len(letra)>1:
    print("no se puede procesar el dato.")

elif letra == "a" or letra == "A":
    print(f"La letra {letra} es vocal")

elif letra == "e" or letra == "E":
    print(f"La letra {letra} es vocal")

elif letra == "i" or letra == "I":
    print(f"La letra {letra} es vocal")

elif letra == "o" or letra == "O":
    print(f"La letra que {letra} es vocal")

elif letra == "u" or letra == "U":
    print(f"La letra {letra} es vocal")


else:
    print(f"La letra {letra} no es una vocal")
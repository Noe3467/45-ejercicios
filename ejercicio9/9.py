"""
Escribí un programa que solicite al usuario el ingreso de un texto y
almacene ese texto en una variable. A continuación, mostrar en pantalla
la primera letra del texto ingresado. Luego, solicitar al usuario que ingrese
un número positivo menor a la cantidad de caracteres que tiene el texto que ingresó
(por ejemplo, si escribió la palabra “HOLA”, tendrá que ser un número entre 0 y 4)
y almacenar este número en una variable llamada indice.
Mostrar en pantalla el carácter del texto ubicado en la posición dada por indice. 
"""
texto = input("ingresà un texto corto--> ")
print(f"La letra con la que comienza el texto es: {texto[0]}")

print("El texto que ingresaste tiene, ",(len(texto)), " caracteres")

indice = int(input("ingresà un nùmero menor a la cantidad de caracteres que tiene tu texto: "))
print(f"El caracter que ocupa la posicion {indice} en tu texto es: ", texto[indice])

"""
Escribí un programa que le solicite al usuario ingresar una fecha formada por 8 números,
donde los primeros dos representan el día, los siguientes dos el mes y los últimos cuatro el año
(DDMMAAAA). Este dato debe guardarse en una variable con tipo int (número entero).
Finalmente, mostrar al usuario la fecha con el formato DD / MM / AAAA.
"""
fecha = int(input("ingresa una fecha usando 2 nùmeros para el dìa, dos nùmeros para el mes y cuatro para formar el año sin espacios ni puntos ni comas o caracteres especiales: "))

dia = fecha // 1000000
mes = (fecha // 10000) % 100
año = fecha % 10000
print(dia, "/" , mes, "/" , año)

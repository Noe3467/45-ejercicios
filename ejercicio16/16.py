"""
Escribí un programa para pedir al usuario su nombre y luego el nombre de otra persona,
almacenando cada nombre en una variable. Luego mostrar en pantalla un valor de verdad que indique si:
los nombres de ambas personas comienzan con la misma letra ó si terminan con la misma letra.
Por ejemplo, si los nombres ingresados son María y Marcos, se mostrará True,
ya que ambos comienzan con la misma letra. Si los nombres son Ricardo y Gonzalo se mostrará True,
ya que ambos terminan con la misma letra. Si los nombres son Florencia y Lautaro se mostrará False,
ya que no coinciden ni la primera ni la última letra. 
"""

nombre = input("ingresà tu nombre: ")
nombreAjeno = input("ingresà el nombre de otra persona: ")

if (nombre[0] == nombreAjeno[0]) & (nombre[-1] == nombreAjeno[-1]):
    print(True)
    print(f"ambos nombres comienzan y terminan con la misma letra.")

elif (nombre[0] == nombreAjeno[0]) or (nombre[-1] == nombreAjeno[-1]):
        print(True)
        print(f"ambos nombres comienzan o terminan con la misma letra.")

else:
        print(False)
        print(f"los nombres que ingresaste comienzan o terminan con letras distintas.")

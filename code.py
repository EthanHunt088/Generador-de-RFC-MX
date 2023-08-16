import os

nombre = input("Escriba su Nombre: ")
ap = input("Escriba su Primer Apellido: ")
am = input("Escriba su Segundo Apellido: ")
print(f"Escriba solo dos digitos en los siguientes apartados")

añonac = input("Año de nacimiento: ")
mesnac = input("Mes de nacimiento: ")
dianac = input("Dia de nacimiento: ")

palabra = list(ap.upper())

temp=""

for letra in palabra:
   if letra == "A":
       temp+="A"
   elif letra == "E":
       temp+="E"
   elif letra == "I":
       temp+="I"
   elif letra == "O":
       temp+="O"
   elif letra == "U":
       temp+="U"

if palabra[0] == "A" or palabra[0] == "E" or palabra[0] == "I" or palabra[0] == "O" or palabra[0] == "U":
   vocal = temp[1]
else:

   vocal = temp[0]
rfc = ap[0] + vocal + am[0] + nombre[0] + añonac + mesnac + dianac
print(rfc.upper())
#os.system ('pause')

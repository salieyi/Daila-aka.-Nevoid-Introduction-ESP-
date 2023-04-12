from os import system
import time

print("Bienvenido a 22Pj: Daila")
time.sleep(3)
Nombre= input("Ingrese su nombre: ")
print("Tu nombre es", Nombre, ", ¿sí o no?")
RespuestaDada= input()
Sí= True
No= False

if RespuestaDada == Sí:
  print("Con que ", Nombre, ", ¿eh? ...")
  
if RespuestaDada == No:
  NombreRe= input("Ingrese su nombre (Ni se te ocurra equivocarte de nuevo): ")
  print("Tu nombre es ", NombreRe , ", ¿sí o no?")
  RespuestaDada2= input()
  if RespuestaDada2 == Sí:
    print("Con que ", NombreRe, ", ¿eh? ...")
  if not RespuestaDada2 == Sí:
    print("Jódete, te quedas con", NombreRe)



print("Elija una contraseña. De lo contrario, los demás usuarios pueden ver sus conversaciones con Daila, y usted no quiere eso, ¿verdad?")
Contraseña= input()
print("De acuerdo, muchas gracias por rellenar tus datos. En unos segundos será atentido.")
time.sleep(5)
system("clear")
time.sleep(2)
print("Introduzca su nombre y contraseña:")
time.sleep(1)
NombreLog= input("Nombre: ")
ContraLog= input("Contraseña: ")

if NombreLog == Nombre and ContraLog == Contraseña:
  print("Correcto, ingresando a su cuenta...")

else:
  print("No es correcto.")
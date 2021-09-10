# Definicion de las variables o listas

Arquero = ""
Defensa = []
MedioCampo = []
Delantera = []


print ("A continuacion designará los 11 jugadores de un equipo de futbol separados por su posicion.")

# Agregar al Arquero
Arquero = (input("Introduzca el nombre del arquero, recuerde que solo puede poner uno: "))

print ("El arquero titular es " + Arquero)

# Agregar a los 4 defensores

print ("A continuación introducirá el nombre de cada defensor, recuerde que solo puede poner cuatro.")

contador = 0    
while contador != 4: 
    D=input("Ingrese el nombre del defensor:")
    Defensa.append (D)
    contador = contador+1

print ("La defensa esta conformada por: ") 
print (Defensa)

# Definicion de las variables o listas

Arquero = ""
Defensa = []
MedioCampo = []
Delantera = []
Suplentes = []

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

# Agregar a los Medio Campistas

print ("A continuación introducirá el nombre de cada mediocampista, recuerde que solo puede poner cuatro.")

contador = 0    
while contador != 4: 
    M=input("Ingrese el nombre del mediocampista: ")
    MedioCampo.append (M)
    contador = contador+1

print ("El mediocampo esta conformado por: ") 
print (MedioCampo)

# Agregar a los Delanteros

print ("A continuación introducirá el nombre de cada Delantero, recuerde que solo puede poner dos.")

contador = 0    
while contador != 2: 
    G=input("Ingrese el nombre del delantero: ")
    Delantera.append (G)
    contador = contador+1

print ("La delantera esta conformada por: ") 
print (Delantera)

# Agregar a los Suplentes

print ("A continuación introducirá el nombre de cada jugador suplente, recuerde que solo puede poner 5.")

contador = 0    
while contador != 5: 
    sup=input("Ingrese el nombre del jugador suplente: ")
    Suplentes.append (G)
    contador = contador+1

print ("El banco de suplentes esta conformado por: ") 
print (Suplentes)

#Equipo Completo

print("Los once titulares para este partido son: ")
print(Arquero)
print(Defensa)
print(MedioCampo)
print(Delantera)
print(Suplentes)

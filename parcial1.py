#PROGRAMADORES:HARVEY RIASCOS, LUIS DIAZ,SEBASTIAN DELGADO
import random
import os
posicion=0
juego=[]
nivel=[]
personajes=[]
fin=True
par=0
defs=0
def niveles(nivel):
    if nivel==1:
        return 20
    if nivel==2:
        return 30
    if nivel==3:
        return 50
    
def dados():
    N=[]
    global par
    global defs
    if par==3:
        sum=0
        defs=sum
        return sum
    for i in range(0,2):
        random_num = random.randrange(1,6)
        N.append(random_num)
    print("Dados: ", N)
    suma=N[0]+N[1]
    if N[0]==N[1]:
        print ("es par repite")
        par+=1
        return suma+dados()
    par=0
    defs=suma
    return suma


def Tablero_jugador(jugadores,nivel):
    for i in range (1,jugadores+1):
        personajes.append(i)
    for d in range (0,len(personajes)):
        juego.append([personajes[d],niveles(nivel)])

print(".: CARRERA NUMÉRICA :.")
while 1==1:
    x=int(input("Digite cantidad de jugadores: "))
    if x>1 and x<5:
        break
    else:
        print("la cantidad de jugadores debe estar en 2 y 4 jugadores")


print("")
print ("Elegir un nivel...")
print ("[1]Nivel Básico (Tablero de20 posiciones)")
print ("[2]Nivel Intermedio (Tablero de 30 posiciones)")
print ("[3]Nivel Avanzado (Tablero de 50 posiciones)")
print ("[5]Salir")
print("")


while 1==1:
    y=int(input("Selección Nivel: "))
    if y>=1 and y<=3:
        break
    else:
        print("los niveles deben estar entre 1 y 3")

Tablero_jugador(x,y)
while fin==True:
    for j in range (0,len(juego)):
        os.system("cls")
        print("Juego actual",juego)
        print("")
        print("TURNO JUGADOR: ",j+1)
        avanza=dados()
        print (" el numero total es :",avanza)
        juego[j][1]=juego[j][1]-avanza
        
        if juego[j][1]<=0:
            print ("GANA JUGADOR: ",j+1)
            print("")
            fin=False
            break
        if juego[j][1]>=0:
            print("Juego ahora: ",juego)
            mins=defs
            print("esto",mins)
        print ("")
        lef=input("Presione enter para continuar: ")



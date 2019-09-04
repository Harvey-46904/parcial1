import random
posicion=0
juego=[]
nivel=[]
personajes=[]
fin=True
def niveles(nivel):
    if nivel==1:
        return 20
    if nivel==2:
        return 30
    if nivel==3:
        return 50
    
def dados():
    N=[]
    for i in range(0,2):
        random_num = random.randrange(1,6)
        N.append(random_num)
    print("Dados: ", N)
    suma=N[0]+N[1]
    print("Avanza: ",suma)
    return suma

def Tablero_jugador(jugadores,nivel):
    for i in range (1,jugadores+1):
        personajes.append(i)
    for d in range (0,len(personajes)):
        juego.append([personajes[d],niveles(nivel)])
    
    


print(".: CARRERA NUMERICA :.")
print("")
print ("Elegir un nivel...")
print ("[1]Nivel Básico (Tablero de20 posiciones)")
print ("[2]Nivel Intermedio (Tablero de 30 posiciones)")
print ("[3]Nivel Avanzado (Tablero de 50 posiciones)")
print ("[5]Salir")
print("")
x=int(input("Digite cantidad de jugadores: "))

y=int(input("Selección Nivel: "))
Tablero_jugador(x,y)
while fin==True:
    for j in range (0,len(juego)):
        print("")
        print("TURNO JUGADOR: ",j+1)
        avanza=dados()
        juego[j][1]=juego[j][1]-avanza
        
        if juego[j][1]<=0:
            print ("GANA JUGADOR: ",j+1)
            fin=False
        if juego[j][1]>=0:
            print("posicion actual: ",juego)
        print ("")
        lef=input("Presione enter para continuar: ")
        
    

print(juego)





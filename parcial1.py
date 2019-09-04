import random
posicion=0
jugador=[]
j1=[]
def dados():
    N=[]
    for i in range(0,2):
        random_num = random.randrange(1,6)
        N.append(random_num)
    print("Dados: ", N)
    return N

def tablerobasico():
    posicion=20
    return posicion
def tablerointermedio():
    posicion=30
    return posicion
def tableroavanzado():
    posicion=50
    return posicion

def jugadores(a):
    if a>=2 and a<=4:
        print ("jugadores validos")
        for i in range(1,a+1):
            jugador.append(i)
        print (jugador)
    else:
        print ("minimo 2 jugadores , maximo 4 jugadores")

def menu(a):
    if a==1:
        print("tablero de :",tablerobasico())
        j1.append(1)
        j1.append(tablerobasico())
        print(j1)
    elif a==2:
        print("tablero de :",tablerointermedio())
    elif a==3:
        print("tablero de :",tableroavanzado())





print(".: CARRERA NUMERICA :.")
print ("Elegir un nivel...")
print ("[1]Nivel Básico (Tablero de20 posiciones)")
print ("[2]Nivel Intermedio (Tablero de 30 posiciones)")
print ("[3]Nivel Avanzado (Tablero de 50 posiciones)")
print ("[5]Salir")

x=int(input("Digite cantidad de jugadores: "))
jugadores(x)
y=int(input("seleccion opcion: "))
menu(y)







print(".: CARRERA NUMERICA :.")
print ("Elegir un nivel...")
print ("[1]Nivel Básico (Tablero de20 posiciones)")
print ("[2]Nivel Intermedio (Tablero de 30 posiciones)")
print ("[3]Nivel Avanzado (Tablero de 50 posiciones)")
print ("[5]Salir")

N=[]

for i in range(0,x):
    random_num = random.randrange(0,6)
    N.append(random_num)
print("Los numeros generados son: ", N)
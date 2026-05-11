import random 

#cantidad de jugadores 
  
while True:
    jugadores = (input("Ingrese cantidad de jugadores (2-4): "))

    if 2 <= jugadores <= 4:
        break
    else:
        print("valida: Debe ingresar entre 2 y 4 jugadores.")

#menu de los jugadores 
print("seleccion de nivel ")
print("1. basico(20 posiciones)")
print("2. intermedio (30 posiciones)")
print("3. Avanzado (50 posiciones)")
print("4. Experto (100 posiciones)")

nivel = int(input("Ingrese opción: "))

if nivel == 1:
    meta = 20
elif nivel == 2:
    meta = 30
elif nivel == 3:
    meta = 50
elif nivel == 4:
    meta = 100

else:
    print ("nivel valido se asigna nivel basico. ")
    meta = 20 

posiciones = [0] * jugadores
dobles_consecutivos = [0] * jugadores

ganador = False

print("inicia la carrera")
print(f"la meta es llegar la posicion {meta}\n")

while not (jugadores):

    for i in  range  (jugadores):

    print(f"\nTurno del Jugador {i+1}")

dado1 = random.randint(1,6)
dado2 = random.randint(1,6)

print(f"Dado 1: {dado1}")
print(f"Dado 2: {dado2}")

if dado1 == dado2:
            dobles_consecutivos[i] += 1
            print("Saco dobles")
 else:
            dobles_consecutivos[i] = 0


if dobles_consecutivos[i] == 3:
     print(f"\nJugador {i+1} gana por obtener 3 dobles consecutivos!")
     ganador = True

     
     posiciones = dado1+dado2
     print(f"avanza posiciones.")
     print(f"Posicion actual: {posiciones[i]}")



     if posiciones[i] >= meta:
            print(f"\n Jugador {i+1} llego a la meta y gana!")
            ganador = True


            posiciones=[0,0,0,0]
            dobles=[0,0,0,0,]
            ganador=False


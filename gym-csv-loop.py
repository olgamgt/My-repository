#!/usr/bin/env python

import gym
import gym_csv
import busqueda
import sys

import numpy as np 
import time

# Se comprueba que el numero de parametros es el correcto
if (len(sys.argv) != 7):
    print("Sigue el siguiente formato: ./pygame-loop.py assets/map1.csv 2 2 9 9 estrella")
    quit()

inFileStr = sys.argv[1] #ruta donde se encuentra el mapa
initX = float(sys.argv[2]) #posicion de la X inicial
initY = float(sys.argv[3]) #posicion de la Y inicial
goalX = float(sys.argv[4]) #posicion de la Y final
goalY = float(sys.argv[5]) #posicion de la Y final
metodo = sys.argv[6] #metodo que se quiere utilizar para planificar el camino que debe seguir el robot para llegar a la meta


# X points down (rows)(v), Y points right (columns)(>), Z would point outwards.
LEFT = 0  # < Decrease Y (column)
DOWN = 1  # v Increase X (row)
RIGHT = 2 # > Increase Y (column)
UP = 3    # ^ Decrease X (row)

SIM_PERIOD_MS = 500.0

env = gym.make('csv-pygame-v0')
state = env.reset()
print("state: "+str(state))
env.render()
time.sleep(10)

''' Se crea un objeto de la clase BusquedaMeta y se inicializa con la ruta al mapa 
    y la posicion inicial y final del robot en las coordenadas X Y respectivamente,
    en ambos casos'''
BUSQUEDA = busqueda.BusquedaMeta(inFileStr, initX, initY, goalX, goalY)

# En funcion del metodo que se quiera utilizar se llama al metodo correspondiente
if metodo == 'estrella':
    nodosCamino = BUSQUEDA.metodo_Aestrella()
elif metodo == 'bfs':
    nodosCamino = BUSQUEDA.metodo_bfs()
elif metodo == 'dfs':
    nodosCamino = BUSQUEDA.metodo_dfs()
else:
    print('El metodo ' + metodo + 'no esta disponible, escoja entre: estrella, dfs o bfs')
    quit()

# Se imprime las posiciones X Y del camino hasta la meta 
print (nodosCamino)
# Se utiliza un contador para recorrer nodosCamino de atras a delante ya que se han guardado las posiciones de esa manera
contador = len(nodosCamino) - 1

for i in range(len(nodosCamino)):

	# Si la siguiente posicion aumenta su coordenada X el robot se movera en el eje X un pixel hacia abajo
    if(nodosCamino[contador][0] < nodosCamino[contador - 1][0]):
        new_state, reward, done, _ = env.step(DOWN)
    # Si la siguiente posicion aumenta su coordenada Y el robot se movera en el eje Y un pixel hacia la derecha
    elif(nodosCamino[contador][1] < nodosCamino[contador - 1][1]):
        new_state, reward, done, _ = env.step(RIGHT)
    # Si la siguiente posicion disimuye su coordenada X el robot se movera en el eje X un pixel hacia arriba
    elif(nodosCamino[contador][0] > nodosCamino[contador - 1][0]):
        new_state, reward, done, _ = env.step(UP)
    # Si la siguiente posicion disimuye su coordenada Y el robot se movera en el eje Y un pixel hacia la izquierda
    elif(nodosCamino[contador][1] > nodosCamino[contador - 1][1]):
        new_state, reward, done, _ = env.step(LEFT)
    
    contador -=1 # Se actualiza el contador para coger la siguiente posicion de nodosCamino en la iteracion siguiente

    env.render()
    print("new_state: "+str(new_state)+", reward: "+str(reward)+", done: "+str(done))
    time.sleep(SIM_PERIOD_MS/1000.0)

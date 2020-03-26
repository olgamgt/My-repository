#! /usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import cv2
import PIL.Image
import sys
import os

class BusquedaMeta(object):
    ''' En esta clase se aplicaran los algoritmos de busqueda a los mapas que se le pasen
    por parametro y se devolvera un vector con las posiciones que debe seguir el robot para ir desde el 
    punto inicial hasta el final'''
    def __init__(self, mapa='assets/map1.csv', Xinicial=2, Yinicial=2, Xfinal=9, Yfinal=9 ):

        self.mapa = mapa
        self.Xinicial = int(Xinicial)
        self.Yinicial = int(Yinicial)
        self.Xfinal = int(Xfinal)
        self.Yfinal = int(Yfinal)
    
    '''Este metodo aplica el algoritmo de busqueda en amplitud'''
    def metodo_bfs(self):

        nodes = []
        charMap = []

        init = Node(self.Xinicial, self.Yinicial , 0, -2)
        nodes.append(init)

        # Se lee el mapa que se pasa por parametro y se guarda en una lista charMap
        with open(self.mapa) as f:
            line = f.readline()
            while line:
                charLine = line.strip().split(',')
                charMap.append(charLine)
                line = f.readline()

        # Se identifican el punto inicial y la meta en el mapa con un 3 y un 4, respectivamente
        charMap[self.Xinicial][self.Yinicial] = '3'
        charMap[self.Xfinal][self.Yfinal] = '4'

        done = False
        goalParentId = -1
        nodosExpandidos = 0

        print ("Iniciando busqueda...")

        while not done:
            for node in nodes:
                nodosExpandidos += 1

                # right
                tmpX = node.x
                tmpY = node.y + 1
                if( charMap[tmpX][tmpY] == '4' ):
                    goalParentId = node.myId
                    done = True
                    break
                elif ( charMap[tmpX][tmpY] == '0' ):
                    newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                    charMap[tmpX][tmpY] = '2'
                    nodes.append(newNode)

                # down
                tmpX = node.x + 1
                tmpY = node.y
                if( charMap[tmpX][tmpY] == '4' ):
                    goalParentId = node.myId
                    done = True
                    break
                elif ( charMap[tmpX][tmpY] == '0' ):
                    newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                    charMap[tmpX][tmpY] = '2'
                    nodes.append(newNode)

                # left
                tmpX = node.x
                tmpY = node.y - 1
                if( charMap[tmpX][tmpY] == '4' ):
                    goalParentId = node.myId
                    done = True
                    break
                elif ( charMap[tmpX][tmpY] == '0' ):
                    newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                    charMap[tmpX][tmpY] = '2'
                    nodes.append(newNode)

                # up
                tmpX = node.x - 1
                tmpY = node.y
                if( charMap[tmpX][tmpY] == '4' ):
                    goalParentId = node.myId
                    done = True
                    break
                elif ( charMap[tmpX][tmpY] == '0' ):
                    newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                    charMap[tmpX][tmpY] = '2'
                    nodes.append(newNode)


        print("META ENCONTRADA!!")

        print("%%%%%%%%%%%%%%%%%%")
        ok = False

        # Se crea una lista de posiciones para guardar el camino que debe seguir el robot
        nodosCamino = []
        # En primer lugar se guarda la meta
        nodosCamino.append([self.Xfinal, self.Yfinal])

        # Se busca en la lista de nodos el camino que se ha obtenido en la busqueda y se guardan las coordenas X Y
        while not ok:
            for node in nodes:
                if( node.myId == goalParentId ):
                    node.dump()
                    nodosCamino.append([node.x, node.y])
                    goalParentId = node.parentId
                    if( goalParentId == -2):
                        ok = True

        # Se devuelve la lista con las posiciones finales
        return nodosCamino
        
    '''Este metodo aplica el algoritmo de busqueda en profundidad, el procedimiento que
        se sigue es el mismo que el metodo anterior'''
    def metodo_dfs (self):
        nodes = []
        charMap = []

        init = Node(self.Xinicial, self.Yinicial , 0, -2)
        nodes.append(init)

        with open(self.mapa) as f:
            line = f.readline()
            while line:
                charLine = line.strip().split(',')
                charMap.append(charLine)
                line = f.readline()

        charMap[self.Xinicial][self.Yinicial] = '3'
        charMap[self.Xfinal][self.Yfinal] = '4'


        done = False
        goalParentId = -1
        cont = 0
        numHijos = 0
        nodosExpandidos = 0

        print ("Iniciando busqueda...")

        while not done:
            for node in nodes:
                nodosExpandidos += 1

                # right
                tmpX = node.x
                tmpY = node.y + 1
                if( charMap[tmpX][tmpY] == '4' ):
                    goalParentId = node.myId
                    done = True
                    break
                elif ( charMap[tmpX][tmpY] == '0' ):
                    newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                    charMap[tmpX][tmpY] = '2'
                    nodes.insert(cont+1+numHijos, newNode)
                    numHijos += 1

                # down
                tmpX = node.x + 1
                tmpY = node.y
                if( charMap[tmpX][tmpY] == '4' ):
                    goalParentId = node.myId
                    done = True
                    break
                elif ( charMap[tmpX][tmpY] == '0' ):
                    newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                    charMap[tmpX][tmpY] = '2'
                    nodes.insert(cont+1+numHijos, newNode)
                    numHijos += 1

                        # left
                tmpX = node.x
                tmpY = node.y - 1
                if( charMap[tmpX][tmpY] == '4' ):
                    goalParentId = node.myId
                    done = True
                    break
                elif ( charMap[tmpX][tmpY] == '0' ):
                    newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                    charMap[tmpX][tmpY] = '2'
                    nodes.insert(cont+1+numHijos, newNode)
                    numHijos += 1

                # up
                tmpX = node.x - 1
                tmpY = node.y
                if( charMap[tmpX][tmpY] == '4' ):
                    goalParentId = node.myId
                    done = True
                    break
                elif ( charMap[tmpX][tmpY] == '0' ):
                    newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                    charMap[tmpX][tmpY] = '2'
                    nodes.insert(cont+1+numHijos, newNode)
                    numHijos += 1

                cont += 1
                numHijos = 0

        print("META ENCONTRADA!!")

        print("%%%%%%%%%%%%%%%%%%")
        ok = False

        nodosCamino = []
        nodosCamino.append([self.Xfinal, self.Yfinal])


        while not ok:
            for node in nodes:
                if( node.myId == goalParentId ):
                    node.dump()
                    nodosCamino.append([node.x, node.y])
                    goalParentId = node.parentId
                    if( goalParentId == -2):
                        print("%%%%%%%%%%%%%%%%%%")
                        ok = True
        
        return nodosCamino

    '''Este metodo aplica el algoritmo de busqueda en A*'''
    def metodo_Aestrella(self):
        
        nodes = []
        charMap = []
        done = False
        goalParentId = -1
        nodosExpandidos = []
        idNodo = 0

        # En este caso se calcula la heuristica mediante el calculo de la distancia de Manhattan entre nodo inicial y meta
        heuristica = distanciaManhattan(self.Xinicial, self.Yinicial , self.Xfinal, self.Yfinal)
        init = Node_estrella(self.Xinicial, self.Yinicial , 0, -2, heuristica, 0, heuristica)
        nodes.append(init)

        with open(self.mapa) as f:
            line = f.readline()
            while line:
                charLine = line.strip().split(',')
                charMap.append(charLine)
                line = f.readline()

        charMap[self.Xinicial][self.Yinicial] = '3'
        charMap[self.Xfinal][self.Yfinal] = '4'

        
        print ("Iniciando busqueda...")

        while not done:
            node = nodes[0]
            nodosExpandidos.append(node)

            # right
            tmpX = node.x
            tmpY = node.y + 1
            if( charMap[tmpX][tmpY] == '4' ):
                goalParentId = node.myId
                done = True
                break
            elif ( charMap[tmpX][tmpY] == '0' ):
                heuristica = distanciaManhattan(tmpX, tmpY, self.Xfinal, self.Yfinal)
                idNodo += 1
                coste = node.c + 1
                funcion = heuristica + coste
                newNode = Node_estrella(tmpX, tmpY, idNodo, node.myId, heuristica, coste, funcion)
                charMap[tmpX][tmpY] = '2'
                nodes.append(newNode)

            # down
            tmpX = node.x + 1
            tmpY = node.y
            if( charMap[tmpX][tmpY] == '4' ):
                goalParentId = node.myId
                done = True
                break
            elif ( charMap[tmpX][tmpY] == '0' ):
                heuristica = distanciaManhattan(tmpX, tmpY, self.Xfinal, self.Yfinal)
                idNodo += 1
                coste = node.c + 1
                funcion = heuristica + coste
                newNode = Node_estrella(tmpX, tmpY, idNodo, node.myId, heuristica, coste, funcion)
                charMap[tmpX][tmpY] = '2'
                nodes.append(newNode)


            # left
            tmpX = node.x
            tmpY = node.y - 1
            if( charMap[tmpX][tmpY] == '4' ):
                goalParentId = node.myId
                done = True
                break
            elif ( charMap[tmpX][tmpY] == '0' ):
                heuristica = distanciaManhattan(tmpX, tmpY, self.Xfinal, self.Yfinal)
                idNodo += 1
                coste = node.c + 1
                funcion = heuristica + coste
                newNode = Node_estrella(tmpX, tmpY, idNodo, node.myId, heuristica, coste, funcion)
                charMap[tmpX][tmpY] = '2'
                nodes.append(newNode)

            # up
            tmpX = node.x - 1
            tmpY = node.y
            if( charMap[tmpX][tmpY] == '4' ):
                goalParentId = node.myId
                done = True
                break
            elif ( charMap[tmpX][tmpY] == '0' ):
                heuristica = distanciaManhattan(tmpX, tmpY, self.Xfinal, self.Yfinal)
                idNodo += 1
                coste = node.c + 1
                funcion = heuristica + coste
                newNode = Node_estrella(tmpX, tmpY, idNodo, node.myId, heuristica, coste, funcion)
                charMap[tmpX][tmpY] = '2'
                nodes.append(newNode)

            nodes.pop(0)
            nodes.sort(key = lambda objeto: objeto.f)

        print("META ENCONTRADA!!")

        print("%%%%%%%%%%%%%%%%%%")
        ok = False

        nodosCamino = []
        nodosCamino.append([self.Xfinal, self.Yfinal])


        while not ok:
            for node in nodosExpandidos:
                if( node.myId == goalParentId ):
                    node.dump()
                    nodosCamino.append([node.x, node.y])
                    goalParentId = node.parentId
                    if( goalParentId == -2):
                        ok = True

        return nodosCamino

    

class Node:
    def __init__(self, x, y, myId, parentId):
        self.x = x
        self.y = y
        self.myId = myId
        self.parentId = parentId
    def dump(self):
        print("---------- x "+str(self.x)+\
            " | y "+str(self.y)+\
            " | id "+str(self.myId)+\
            " | parentId "+str(self.parentId))

class Node_estrella:
    def __init__(self, x, y, myId, parentId, h, c, f):
        self.x = x
        self.y = y
        self.myId = myId
        self.parentId = parentId
        self.h = h
        self.c = c
        self.f = f
    def dump(self):
        print("---------- x "+str(self.x)+\
            " | y "+str(self.y)+\
            " | id "+str(self.myId)+\
            " | parentId "+str(self.parentId)+\
            " | heuristica "+str(self.h)+\
            " | coste "+str(self.c)+\
            " | funcion "+str(self.f))

def distanciaManhattan(x1, y1, x2, y2):
  res = (abs(x1-x2) + abs(y1-y2))
  return res

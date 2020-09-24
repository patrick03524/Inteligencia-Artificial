# Practica Del Juego de Damas
Universidad Católica San Pablo
Inteligencia Artificial
Práctica del juego de Damas con IA
Integrantes del grupo:
* Patrick Xavier Márquez Choque
* Jean Carlo Cornejo Cornejo
* Oscar Andree Mendoza

## Tabla de Contenidos
* [Introducción](#introducción)
* [Líbrerías Necesarias](#librerías-necesarias)
* [Resultados](#resultados)

## Introducción
El código se desarolló en Python 3.7.4.
Se implementaron 1 algoritmo de MinMax() para el desarrollo de un juego de Damas.

Este juego básico cuenta con un menu para ingresar la *Dificultad*. La Dificultad es la profundidad máxima que alcanzará nuestro árbol de posibilidades del algoritmo MinMax y generará todas las siguientes posibles jugadas para la IA.

Se utilizó la libreria graphics.py 5.0.1.post1 para dibujar el tablero, las fichas y los movimientos de manera gráfica.

##  Librerías Necesarias
* graphics.py==5.0.1.post1
* numpy 1.19.2  
* random
* copy
* deepcopy
* time
* pickle

##  Resultados
Al compilar el proyecto se mostrará el siguiente menu
![Alt text](https://github.com/patrick03524/Inteligencia-Artificial/blob/master/Laboratorio%20Tema%20de%20B%C3%BAsquedas%201/Imgs/sc1.png)

Cada opción mostrará un item diferente.
La primera opción mostrará un grafo de 10 nodos en un espacio de 100x100; cada nodo es elegido con posiciones aleatorias y con aristas unidas aleatoriamente a cada otro nodo del grafo.
El grafo resultante es el siguiente:
![Alt text](https://github.com/patrick03524/Inteligencia-Artificial/blob/master/Laboratorio%20Tema%20de%20B%C3%BAsquedas%201/Imgs/graph1.png)
La segunda opción mostrará un grafo puntual, un grafo con 100 nodos en un espacio 10x10; cada nodo es vecino dependiendo de su posición en el tablero donde para mostrar el funcionamiento de los algoritmos desde la posición inferior a la izquierda (1,1) hasta la posición superior a la derecha (9,9).
![Alt text](https://github.com/patrick03524/Inteligencia-Artificial/blob/master/Laboratorio%20Tema%20de%20B%C3%BAsquedas%201/Imgs/graph2.png)

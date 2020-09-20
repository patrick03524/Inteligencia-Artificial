# Practica De Búsquedas
Universidad Católica San Pablo
Inteligencia Artificial
Práctica de Búsquedas
Integrantes del grupo:
* Patrick Xavier Márquez Choque
* Jean Carlo Cornejo Cornejo
* Oscar Andree Mendoza
## Introducción
El código se desarolló en Python 3.7.4.
Se implementaron 2 algoritmos de busqueda.
* 1 Algoritmo de Búsqueda Ciega (Búsqueda por Profundidad)

  **Dentro de los ejemplos los caminos de color azul y rojo mostrarán las trayectorias recorridas por la Búsqueda Ciega**
* 1 Algoritmo de Búsqueda Heurística (Algoritmo A* utilizando la Distancia Euclidiana)

  **Dentro de los ejemplos el camino de color verde mostrará las trayectorias recorridas por la Búsqueda Heurística**
  
Se utilizó la libreria matplotlib 3.2.1 para dibujar los grafos y sus seguimiento. El código mostrará el siguiente menu al ser compilado:

##  Librerias Necesarias
* networkx 2.5
* matplotlib 3.2.1
* random
* math
* sys
* time
* PriorityQueue

##  Compilaciones
Al compilar el proyecto se mostrará el siguiente menu
![Alt text](https://github.com/patrick03524/Inteligencia-Artificial/blob/master/Laboratorio%20Tema%20de%20B%C3%BAsquedas%201/Imgs/sc1.png)

Cada opción mostrará un item diferente.
La primera opción mostrará un grafo de 10 nodos en un espacio de 100x100; cada nodo es elegido con posiciones aleatorias y con aristas unidas aleatoriamente a cada otro nodo del grafo.
El grafo resultante es el siguiente:
![Alt text](https://github.com/patrick03524/Inteligencia-Artificial/blob/master/Laboratorio%20Tema%20de%20B%C3%BAsquedas%201/Imgs/graph1.png)
La segunda opción mostrará un grafo puntual, un grafo con 100 nodos en un espacio 10x10; cada nodo es vecino dependiendo de su posición en el tablero donde para mostrar el funcionamiento de los algoritmos desde la posición inferior a la izquierda (1,1) hasta la posición superior a la derecha (9,9).
![Alt text](https://github.com/patrick03524/Inteligencia-Artificial/blob/master/Laboratorio%20Tema%20de%20B%C3%BAsquedas%201/Imgs/graph2.png)

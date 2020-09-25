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

Este juego básico cuenta con un menu para ingresar la *dificultad*. La Dificultad es la profundidad máxima que alcanzará nuestro árbol de posibilidades del algoritmo MinMax y generará todas las siguientes posibles jugadas para la IA.

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
Al compilar el proyecto se mostrará el siguiente menu:

![Alt text](https://github.com/patrick03524/Inteligencia-Artificial/blob/master/Laboratorio%20Juego%20de%20Damas%202/Imgs/dificultad.png)

Esta ventana permite ingresar la *dificultad*. La Dificultad es la profundidad máxima que alcanzará nuestro árbol de posibilidades y es inicializada en 2. Luego al hacer click en la ventana se mostrará la siguiente ventana.

![Alt text](https://github.com/patrick03524/Inteligencia-Artificial/blob/master/Laboratorio%20Juego%20de%20Damas%202/Imgs/tablero.png)

Esta será el tablero del Juego de Damas, ahora puede iniciar el juego:

*Para poder realizar algún movimiento es necesario primero hacer click tanto en alguna ficha que sea capaz de realizar un movimiento y posteriormente ahcer click en alguna casilla vacia donde a la cual se pueda realizar el movimiento, el juego analizará si este es un movimiento válido y posteriormente hará la actualización visual de la ficha moviendose hacia esa casilla.*

Por ejemplo empezaremos el juego de la siguiente manera:

![Alt text](https://github.com/patrick03524/Inteligencia-Artificial/blob/master/Laboratorio%20Juego%20de%20Damas%202/Imgs/primermovimiento.png)

![Alt text](https://github.com/patrick03524/Inteligencia-Artificial/blob/master/Laboratorio%20Juego%20de%20Damas%202/Imgs/segundomovimiento.png)

![Alt text](https://github.com/patrick03524/Inteligencia-Artificial/blob/master/Laboratorio%20Juego%20de%20Damas%202/Imgs/tercermovimiento.png)

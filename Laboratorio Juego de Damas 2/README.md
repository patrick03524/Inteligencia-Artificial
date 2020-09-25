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

El tablero será una matriz de casilla de 8x8 de 500px de tamaño y cada ficha que nosotros controlaremos serán de color azul mientas que las fichas controladas por la IA serán de color rojo.

**Para poder realizar algún movimiento es necesario primero hacer click tanto en alguna ficha que sea capaz de realizar un movimiento y posteriormente ahcer click en alguna casilla vacia donde a la cual se pueda realizar el movimiento, el juego analizará si este es un movimiento válido y posteriormente hará la actualización visual de la ficha moviendose hacia esa casilla.**

Por ejemplo empezaremos el juego de la siguiente manera:

![Alt text](https://github.com/patrick03524/Inteligencia-Artificial/blob/master/Laboratorio%20Juego%20de%20Damas%202/Imgs/primermovimiento.png)

Nosotros realizaremos el primer movimiento, entonces moveremos la 3 ficha azul a la casilla superior derecha.

![Alt text](https://github.com/patrick03524/Inteligencia-Artificial/blob/master/Laboratorio%20Juego%20de%20Damas%202/Imgs/segundomovimiento.png)

Al realizar este movimiento la IA del Juego de damas analizará todas las posibilidades para calcular el mejor movimiento de las fichas que estan disponibles para moverse, en este caso es su primer movimiento asi que las únicas fichas capaces de moverse son las fichas rojas.

![Alt text](https://github.com/patrick03524/Inteligencia-Artificial/blob/master/Laboratorio%20Juego%20de%20Damas%202/Imgs/tercermovimiento.png)

Asi es como la IA del juego va a realizar los movimientos y escocjerá entre ellos la mejor opción. El juego acaba mostrando una pantalla de Game Over cuando algun jugador se queda sin fichas (Con las Mismas Reglas que el juego tradicional).

# Practica Del Algoritmo Genético
Universidad Católica San Pablo
Inteligencia Artificial
Práctica del Algoritmo Genético Maximizando una Función Matemática
Integrantes del grupo:
* Patrick Xavier Márquez Choque
* Jean Carlo Cornejo Cornejo
* Oscar Andree Mendoza

## Tabla de Contenidos
* [Introducción](#introducción)
* [Líbrerías Necesarias](#librerías-necesarias)
* [Resultados](#resultados)

## Introducción
El código se desarolló en C++(GNU C++ 11) en el archivo Algoritmo_Genetico_fun.cpp, los demás archivos corresponden a los archivos necesarios del proyecto que fue desarrollador en Visual Studio 2017.

Se realizo el código para Optimizar una función matemática usando algoritmos genéticos almacenar el valor de aptitud del mejor individuo y el promedio de la población en cada generación.

El proyecto fue realizado en Visual Studio 2017 con el compilador y debbuger del propio Visual Studio.

##  Librerías Necesarias

* Todas las librerías necesarias son nativas del propio lenguaje de C++ así que no es necesario ninguna instalación previa de alguna libreria externa al compilador básico.

##  Resultados
Primero se define variables necesarias para la compilación del algoritmo genético que son:

* [rand_start 1, rand_end 1000] -> Rango de los numeros aleatorios para la creación de los primeros individuos de nuestra población.
* n_pob 4 -> Cantidad de individuos de la población por generación.
* n_iter 100 -> Cantidad de iteraciones o "Generaciones" que se crearán dentro de todo el algoritmo genético.
* len -> Cantidad de bits que tendra cada número("individuo").

Los resultados de una compilación del código mostrarán dentro de cada Generación el valor del Mejor Individuo(Número entero positivo dentro del rango especificado) y el promedio de los valores de todos los individuos.

Luego de esto con todos estos datos se realizó una grafica comparativa de estos dentro de Excel, una previsualización del archivo: grafica.xlsx es el siguiente:





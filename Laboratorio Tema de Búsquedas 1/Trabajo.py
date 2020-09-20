import networkx as nx
import matplotlib.pyplot as plt
import random
import math
import sys
import time
from queue import PriorityQueue 


class Graph(object):
    G = nx.Graph()
    g_nodos = {}
    g_nodos_count = 0
    g_aristas_per_nodo = 0
    g_search_label = 0
    tam_x = 0
    tam_y = 0
    
    Helper = 0
    INICIO = 0
    FIN = 0

    def DefNodos(self, n):
        for i in range(0,n):
            temp_x = random.randint(0,self.tam_x)
            temp_y = random.randint(0,self.tam_y)
            self.g_nodos[i]=(temp_x,temp_y)
        self.G.add_nodes_from(self.g_nodos.keys())
        return

    def DefNodos2(self,n):
        last_n = 0
        h = 0
        for i in range(0, n):
            for j in range(0, n):
                self.g_nodos[j + last_n] = (j, h)  # (height,j) #orientation
            last_n = last_n + n
            h = h + 1
        self.G.add_nodes_from(self.g_nodos.keys())
        return

    def DefAristas(self, a):
        for i in self.G.nodes:
            for j in range(0, 3):
                if self.G.has_node(i + 1) and (i + 1) % a is not 0:
                    self.G.add_edge(i, i + 1, color='silver')  
                if self.G.has_node(i + a):  
                    self.G.add_edge(i, i + a, color='silver')  
                if self.G.has_node(i + a + 1) and (i + a + 1) % a is not 0:
                    self.G.add_edge(i, i + a + 1, color='silver')  
                if self.G.has_node(i - a + 1) and (i - a + 1) % a is not 0:
                    self.G.add_edge(i, i - a + 1, color='silver')  
                
        return

    def DefAristas2(self, a):
        for i in self.G.nodes:
            for j in range(0, 3):
                if self.G.has_node(i + 1) and (i + 1) % a is not 0:
                    self.G.add_edge(i, i + 1, color='silver')  
                if self.G.has_node(i + a):  
                    self.G.add_edge(i, i + a, color='silver')  
                if self.G.has_node(i + a + 1) and (i + a + 1) % a is not 0:
                    self.G.add_edge(i, i + a + 1, color='silver')  
                if self.G.has_node(i - a + 1) and (i - a + 1) % a is not 0:
                    self.G.add_edge(i, i - a + 1, color='silver')  
                
        return

    def CreateRegularGraph(self, n, a, x, y):
        self.g_nodos_count = n
        self.g_aristas_per_nodo = a
        self.tam_x = x
        self.tam_y = y

        self.DefNodos(self.g_nodos_count)
        self.DefAristas(self.g_aristas_per_nodo)
        #self.Helper = self.g_nodos_count
        #self.DefNodos(n)
        #self.DefAristas(n)
        #self.Helper = n
        return
    
    def CreateRegularGraph2(self, n, a, x, y):
        self.g_nodos_count = n
        self.g_aristas_per_nodo = a
        self.tam_x = x
        self.tam_y = y

        self.DefNodos2(self.g_nodos_count)
        self.DefAristas2(self.g_nodos_count)
        self.Helper = self.g_nodos_count        
        return

    def Display(self):
        plt.show(block=False)
        plt.figure(figsize = (self.tam_x,self.tam_y))
        #plt.figure(figsize=(10, 10))

        nx.draw_networkx_nodes(self.G, self.g_nodos, node_size=8, node_color='gray', alpha=0.3)
        nx.draw_networkx_labels(self.G, self.g_nodos, font_size=0)

        edges = self.G.edges()
        colors = [self.G[u][v]['color'] for u, v in edges]

        nx.draw_networkx_edges(self.G, self.g_nodos, width=2, edge_color=colors, alpha=0.75)

        if self.g_search_label is 1:
            plt.title('Result')
        elif self.g_search_label is 2:
            plt.title('Result')
        else:
            plt.title('No Search Performed')
        plt.show()

    def heuristic(self, a, b):
        aX = self.g_nodos.get(a)[0]
        aY = self.g_nodos.get(a)[1]
        bX = self.g_nodos.get(b)[0]
        bY = self.g_nodos.get(b)[1]
        return math.sqrt((bX - aX) ** 2 + (bY - aY) ** 2)  # Euclidean distance
        # return abs(aX - bX) + abs(aY - bY)       #Manhattan distance

    def blindSearch(self, StartX, StartY, EndX, EndY):
        self.INICIO = StartX + (self.Helper * StartY)
        self.FIN = EndX + (self.Helper * EndY)
        if (self.G.has_node(self.INICIO) is False) or (self.G.has_node(self.FIN) is False):
            print("Start or goal doesn't exist")
            return 0
        path = []
        nodossinhijos = []
        path.append(self.INICIO)
        nodossinhijos.append(self.INICIO)

        current = path[0]
        while current != self.FIN:
            vecinos = []
            for i in self.G.neighbors(current):
                if i not in path and i not in nodossinhijos:
                    vecinos.append(i)
            if len(vecinos) > 0:
                current = vecinos[0]
                path.append(current)
            else:
                nodossinhijos.append(current)
                path.pop(-1)

        returnPath = path
        returnPath.reverse()
        returner = returnPath[0]
        i = 0
        while i < len(returnPath) - 1:
            if i == 0 or i == len(returnPath) - 2:
                self.G.add_edge(returner, returnPath[i + 1], color='blue')
            else:
                self.G.add_edge(returner, returnPath[i + 1], color='red')
            returner = returnPath[i + 1]
            i = i + 1
        self.g_search_label = 2
        return len(returnPath)

    def AStar(self, StartX, StartY, EndX, EndY):
        self.INICIO = StartX + (self.Helper * StartY)
        self.FIN = EndX + (self.Helper * EndY)
        pathSize = 0
        if (self.G.has_node(self.INICIO) is False) or (self.G.has_node(self.FIN) is False):
            return 0
        Pawn = PriorityQueue()
        Pawn.put(self.INICIO, 0)
        came_from = {}
        Score = {}
        came_from[self.INICIO] = None
        Score[self.INICIO] = 0
        while not Pawn.empty():
            current = Pawn.get()
            if current == self.FIN:
                break
            for Next in self.G.neighbors(current):
                tentative_score = Score[current] + self.heuristic(current, self.FIN)
                if Next not in Score or tentative_score < Score[Next]:
                    Score[Next] = tentative_score
                    fScore = tentative_score + self.heuristic(self.FIN, Next)
                    Pawn.put(Next, fScore)
                    came_from[Next] = current
        returnPath = {}
        returner = self.FIN
        while returner is not self.INICIO:
            returnPath.update({returner: came_from[returner]})
            self.G.add_edge(returner, came_from[returner], color='green')
            returner = came_from[returner]
            pathSize = pathSize + 1
        self.g_search_label = 1
        return pathSize


def main():
    print("****MENU PRINCIPAL****")
    time.sleep(1)
    choice = input("""
        Bienvenido al Menu de Opciones
        Universidad Católica San Pablo
        Laboratorio de Inteligencia Artificial
        ...
        ...
        Elegir alguna de estas siguientes opciones:
        A: Crear un Grafo Totalmente Aleatorio.
        
        B: Crear un Grafo 10x10 haciendo la
        búsqueda del Nodo(0,0) al Nodo(9,9)
        ...
        Eliga la opcion A o B: """)
    if choice == "A" or choice == "a":
        A = Graph()
        numberNodes = 10
        numberPerEdge = 4
        numberX = 100
        numberY = 100
        A.CreateRegularGraph(numberNodes, numberPerEdge, numberX, numberY)
        Ax, Ay = 1,1
        Bx, By = 7,1
        print("Path: Blind Search was: ", A.blindSearch(Ax, Ay, Bx, By))
        print("Path: A* was: ", A.AStar(Ax, Ay, Bx, By))
        A.Display()
    elif choice == "B" or choice == "b":
        B = Graph()
        numberNodes = 10
        numberPerEdge = 9
        numberX = 10
        numberY = 10
        B.CreateRegularGraph2(numberNodes, numberPerEdge, numberX, numberY)
        Ax, Ay = 1,1
        Bx, By = 9,9
        print("Path: Blind Search: ", B.blindSearch(Ax, Ay, Bx, By))
        print("Path: A*: ", B.AStar(Ax, Ay, Bx, By))
        B.Display()
    

if __name__ == '__main__':
    main()

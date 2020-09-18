from queue import PriorityQueue

import networkx as nx
import matplotlib.pyplot as plt
import random
import math


class Graph(object):
    G = nx.Graph()
    g_nodos = {}
    g_nodos_count = 0
    g_aristas_per_nodo = 0
    g_search_label = 0
    tam_x = 0
    tam_y = 0
    
    Helper = 0
    START = 0
    GOAL = 0

    # Creational methods:
    def DefNodos(self, n):
        for i in range(0,n):
            #temp_x = random.randint(0, 10) 
            #temp_y = random.randint(0, 10)
            temp_x = random.randint(0,self.tam_x)
            temp_y = random.randint(0,self.tam_y)
            self.g_nodos[i]=(temp_x,temp_y)
        self.G.add_nodes_from(self.g_nodos.keys())
        return

    def DefAristas(self, a):
        #for i in self.G.
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
        #self.DefNodos(n)
        #self.DefAristas(n)
        #self.Helper = n
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

    def blindSearch(self, StartX, StartY, GoalX, GoalY):
        self.START = StartX + (self.Helper * StartY)
        self.GOAL = GoalX + (self.Helper * GoalY)
        if (self.G.has_node(self.START) is False) or (self.G.has_node(self.GOAL) is False):
            print("Start or goal doesn't exist")
            return 0
        path = []
        nodossinhijos = []
        path.append(self.START)
        nodossinhijos.append(self.START)

        current = path[0]
        while current != self.GOAL:
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

    def AStar(self, StartX, StartY, GoalX, GoalY):
        self.START = StartX + (self.Helper * StartY)
        self.GOAL = GoalX + (self.Helper * GoalY)
        pathSize = 0
        if (self.G.has_node(self.START) is False) or (self.G.has_node(self.GOAL) is False):
            print("Start or goal doesn't exist")
            return 0
        Pawn = PriorityQueue()
        Pawn.put(self.START, 0)
        came_from = {}
        Score = {}
        came_from[self.START] = None
        Score[self.START] = 0
        while not Pawn.empty():
            current = Pawn.get()
            if current == self.GOAL:
                break
            for Next in self.G.neighbors(current):
                tentative_score = Score[current] + self.heuristic(current, self.GOAL)
                if Next not in Score or tentative_score < Score[Next]:
                    Score[Next] = tentative_score
                    fScore = tentative_score + self.heuristic(self.GOAL, Next)
                    Pawn.put(Next, fScore)
                    came_from[Next] = current
        returnPath = {}
        returner = self.GOAL
        while returner is not self.START:
            returnPath.update({returner: came_from[returner]})
            self.G.add_edge(returner, came_from[returner], color='green')
            returner = came_from[returner]
            pathSize = pathSize + 1
        self.g_search_label = 1
        return pathSize


def main():
    A = Graph()
    numberNodes = 10
    numberPerEdge = 4
    numberX = 100
    numberY = 100
    A.CreateRegularGraph(numberNodes, numberPerEdge, numberX, numberY)
    Sx, Sy = 1,7
    Gx, Gy = 6,1
    print("Path size with Blind Search was: ", A.blindSearch(Sx, Sy, Gx, Gy))
    print("Path size with A* was: ", A.AStar(Sx, Sy, Gx, Gy))
    A.Display()


if __name__ == '__main__':
    main()

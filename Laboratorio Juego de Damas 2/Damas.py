from time import sleep
import time
#import pygame
import graphics
from graphics import Point
import copy
from copy import deepcopy
import pickle
import random
import numpy

#########################################################################################################
#tablero_bien_bonito = pygame.image.load("\Imagenes\Graphics_Damas\tablero2.png")
#ficha_dama_bien_bonito = pygame.image.load("\Imagenes\Graphics_Damas\pieza_dama.png")
#ficha_corona_bien_bontito = pygame.image.load("\Imagenes\Graphics_Damas\pieza_negra.png")

class Pieza():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.center = [x + 25, y + 25]
        self.ficha = None

def copytablero(origin):
    new_tablero = copy.deepcopy(origin)
    for pieza in tablero.flat:
        new_tablero[int(pieza.x / 62.5), int(pieza.y / 62.5)] = copy.deepcopy(pieza)
        new_tablero[int(pieza.x / 62.5), int(pieza.y / 62.5)].ficha = copy.deepcopy(pieza.ficha)
    return new_tablero


class Ficha():
    def __init__(self):
        self.corona = False
        self.x = None
        self.y = None
        self.coronado = False
        self.circle = None
        self.id = None
        self.index = None


def moveFicha(ficha, pieza):
    pieza.ficha = ficha
    ficha.circle.move(pieza.center[0], pieza.center[1])

#########################################################################################################
tablero = numpy.empty((8, 8), dtype=Pieza)
fichas = []

def addFicha(x, y):
    if y == 3 or y == 4:
        return
    ficha = Ficha()
    ficha.id = (x, y)
    ficha.index = x*8 + (y+1)
    if y < 4:
        ficha.coronado = True
    ficha.x = x
    ficha.y = y
    tablero[x, y].ficha = ficha
    fichas.append(ficha)

for x in range(0, 8):
    if x % 2 == 1:
        pieza_offset = True
    else:
        pieza_offset = False
    for y in range(0, 8):
        pieza = Pieza(x * 62.5, y * 62.5)
        tablero[x, y] = pieza
        if (x % 2 == 0 or y % 2 == 0) and (pieza_offset == True):
            addFicha(x, y)
        elif (x % 2 == 1 or y % 2 == 1) and (pieza_offset == False):
            addFicha(x, y)

def King(tablero):
    for pieza in tablero.flat:
        if pieza.ficha is None or pieza.ficha.corona:
            continue
        if (pieza.y / 62.5 == 7 and pieza.ficha.coronado) or (pieza.y / 62.5 == 0 and not pieza.ficha.coronado):
            pieza.ficha.corona = True

def getFullMove(partial_move):
    moves = findJumps(tablero, False) + findMoves(tablero, False)
    for move in moves:
        if move.ficha.id == partial_move.ficha.id and move.pieza.x == partial_move.pieza.x \
                and move.pieza.y == partial_move.pieza.y:
            return move
    return None

def hasWon(tablero):
    no_coronado_actions = findJumps(tablero, False) + findMoves(tablero, False)
    coronado_actions = findJumps(tablero, True) + findMoves(tablero, True)
    if len(no_coronado_actions) == 0:
        return -1
    elif len(coronado_actions) == 0:
        return 1
    else:
        return 0

meaningless_table = numpy.zeros((8, 8, 64))

for i in range(0,8):
    for j in range(0,8):
        for k in range(0,64):
            meaningless_table[i,j,k] = random.randint(0, 1000000)

def moveToHash(move, tablero, depth):
    hsh = 0
    for pieza in tablero.flat:
        if pieza.ficha is None:
            continue
        ficha = pieza.ficha
        hsh = hsh ^ int(meaningless_table[int(pieza.x/62.5), int(pieza.y/62.5), pieza.ficha.index])
    hsh += hash(str(move.ficha.id) + str(move.ficha.x) + str(move.ficha.y))
    return hsh



class Tablero_TablaHash():
    def __init__(self):
        self.tabla_hash = {}
            
    def insert(self, move, ntablero, depth):
        index = moveToHash(move, ntablero, depth)
        self.tabla_hash[index] = move.weight
    
    def search(self, move, ntablero, depth):
        index = moveToHash(move, ntablero, depth)
        return self.tabla_hash[index]

matrix = Tablero_TablaHash()

def takeFicha(x, y, tablero):
    tablero[x, y].ficha = None

DIFFICULTY = 2

def setDifficulty(val):
    DIFFICULTY = val

class Move():
    def __init__(self, ficha, pieza, variant):
        self.ficha = ficha
        self.pieza = pieza
        self.type = variant
        self.distance = 1
        self.weight = None
        self.jumped = []
        self.otherpiezas = []

    def apply(self, tablero):
        ficha_x = self.ficha.x
        ficha_y = self.ficha.y
        new_x = self.pieza.x / 62.5
        new_y = self.pieza.y / 62.5
        tablero[int(ficha_x), int(ficha_y)].ficha = None
        tablero[int(new_x), int(new_y)].ficha = deepcopy(self.ficha)
        tablero[int(new_x), int(new_y)].ficha.x = tablero[int(
            new_x), int(new_y)].x / 62.5
        tablero[int(new_x), int(new_y)].ficha.y = tablero[int(
            new_x), int(new_y)].y / 62.5
        for pieza in self.jumped:
            tablero[int(pieza.x / 62.5), int(pieza.y / 62.5)].ficha = None
        return tablero
    
def findNeighbor(tablero, x, y, up=False, down=False):
    neighbors = []
    if not up:
        if x != 7 and y != 7:
            neighbors.append(tablero[int(x + 1), int(y + 1)])
        if x != 0 and y != 7:
            neighbors.append(tablero[int(x - 1), int(y + 1)])
    if not down:
        if x != 7 and y != 0:
            neighbors.append(tablero[int(x + 1), int(y - 1)])
        if x != 0 and y != 0:
            neighbors.append(tablero[int(x - 1), int(y - 1)])
    return neighbors

def checkNeighbor(x, y, px, py, up=False, down=False, dir=-1):
    results = []
    if not up:
        if (x == px + 1 and y == py + 1):
            # South_West
            results.append(0)
            if dir == 0:
                results = [0]
                return results
        if (x == px - 1 and y == py + 1):
            # South_East
            results.append(1)
            if dir == 1:
                results = [1]
                return results
    if down:
        if results == []:
            results.append(-1)
        return results
    if (x == px + 1 and y == py - 1):
        # North_West
        results.append(2)
        if dir == 2:
            results = [2]
            return results
    if (x == px - 1 and y == py - 1):
        # North_East
        results.append(3)
        if dir == 3:
            results = [3]
            return results
    if results == []:
        results.append(-1)
    return results

def findMoves(tablero, color):
    moves = []
    for pieza in tablero.flat:
        if pieza.ficha is None or pieza.ficha.coronado != color:
            continue
        options = []
        if pieza.ficha.corona:
            piezas = findNeighbor(tablero, pieza.x / 62.5, pieza.y / 62.5)
        elif color:
            piezas = findNeighbor(tablero, pieza.x / 62.5, pieza.y / 62.5, down=True)
        elif not color:
            piezas = findNeighbor(tablero, pieza.x / 62.5, pieza.y / 62.5, up=True)
        for new_pieza in piezas:
            dirs = []
            if color is True or pieza.ficha.corona:
                dirs.append(checkNeighbor(new_pieza.x / 62.5, new_pieza.y / 62.5, pieza.x / 62.5, pieza.y / 62.5, down=True))
            if color is False or pieza.ficha.corona:
                dirs.append(checkNeighbor(new_pieza.x / 62.5, new_pieza.y / 62.5, pieza.x / 62.5, pieza.y / 62.5, up=True))
            for direction in dirs:
                if direction[0] != -1:
                    options.append(new_pieza)

        for option in options:
            if option.ficha == None:
                moves.append(Move(pieza.ficha, option, "Move"))
    return moves

def findJumps(tablero, color, old=None, depth=0):
    jumps = []
    for pieza in tablero.flat:
        if pieza.ficha is None or pieza.ficha.coronado != color:
            continue
        options = []
        dirs = []
        if pieza.ficha.corona:
            piezas = findNeighbor(tablero, pieza.x / 62.5, pieza.y / 62.5)
        elif color:
            piezas = findNeighbor(tablero, pieza.x / 62.5, pieza.y / 62.5, down=True)
        elif not color:
            piezas = findNeighbor(tablero, pieza.x / 62.5, pieza.y / 62.5, up=True)
        for new_pieza in piezas:
            dir = []
            if new_pieza.ficha is None or new_pieza.ficha.coronado == color:
                continue
            if color is True or pieza.ficha.corona:
                dir.append(checkNeighbor(new_pieza.x / 62.5, new_pieza.y /
                                         62.5, pieza.x / 62.5, pieza.y / 62.5, down=True))
            if color is False or pieza.ficha.corona:
                dir.append(checkNeighbor(new_pieza.x / 62.5, new_pieza.y /
                                         62.5, pieza.x / 62.5, pieza.y / 62.5, up=True))
            for direction in dir:
                if direction[0] != -1:
                    options.append(new_pieza)
                    dirs.append(direction[0])
        x = 0
        for option in options:
            new_pieza = None
            if option.x / 62.5 == 0 or option.x / 62.5 == 7 or option.y / 62.5 == 0 or option.y / 62.5 == 7:
                x += 1
                continue
            if dirs[x] == 0:
                new_pieza = tablero[int(option.x / 62.5) + 1,
                                  int(option.y / 62.5) + 1]
                x += 1
            elif dirs[x] == 1:
                new_pieza = tablero[int(option.x / 62.5 - 1),
                                  int(option.y / 62.5 + 1)]
                x += 1
            elif dirs[x] == 2:
                new_pieza = tablero[int(option.x / 62.5 + 1),
                                  int(option.y / 62.5 - 1)]
                x += 1
            elif dirs[x] == 3:
                new_pieza = tablero[int(option.x / 62.5 - 1),
                                  int(option.y / 62.5 - 1)]
                x += 1
            if new_pieza.ficha is None:
                move = Move(pieza.ficha, new_pieza, "Jump")
                move.jumped.append(option)
                new_tablero = copytablero(tablero)
                move.apply(new_tablero)

                if depth < 2:
                    new_jumps = findJumps(new_tablero, color, option, depth + 1)
                    extra_jump = False
                    for jump in new_jumps:
                        if jump.ficha.id == pieza.ficha.id:
                            extra_jump = True
                            jump.jumped.append(option)
                            jump.otherpiezas.append(new_pieza)
                            if old is not None:
                                jump.jumped.append(old)
                            jump.ficha = pieza.ficha
                            jumps.append(jump)
                    if not extra_jump:
                        jumps.append(move)
    return jumps

def weightablero(tablero, depth):
    no_coronado_moves = findMoves(tablero, False) + findJumps(tablero, False)
    coronado_moves = findMoves(tablero, True) + findJumps(tablero, True)
    for move in no_coronado_moves:
        needhash = True
        if moveToHash(move, tablero, depth) in matrix.tabla_hash:
            move.weight = matrix.search(move, tablero, depth)
            needhash = False
        else:
            move.weight = 0
            if Mejora_Move1(tablero, move, False):
                move.weight += 3
            if enemyJump(tablero, move, False):
                move.weight += -3
            if Mejora_Move4(tablero, move, False):
                move.weight += -5
            if Mejora_Move3(tablero, move, False):
                move.weight += 4
            if Mejora_Move2(tablero, move, False):
                move.weight += 6
            if len(coronado_moves) == 3 and Mejora_Ganar(tablero, move, False):
                move.weight += 200
            if move.type == "Jump":
                move.weight += 99 + len(move.jumped)
            if move.type != "Jump":
                matrix.insert(move, tablero, depth)
    for move in coronado_moves:
        needhash = True
        if moveToHash(move, tablero, depth) in matrix.tabla_hash:
            move.weight = matrix.search(move, tablero, depth)
            needhash = False
        else:
            move.weight = 0
            if Mejora_Move1(tablero, move, True):
                move.weight += -3
            if enemyJump(tablero, move, True):
                move.weight += 3
            if Mejora_Move4(tablero, move, True):
                move.weight += 5
            if Mejora_Move3(tablero, move, True):
                move.weight += -4
            if Mejora_Move2(tablero, move, True):
                move.weight += -6
            if len(no_coronado_moves) == 3 and Mejora_Ganar(tablero, move, True):
                move.weight += -200
            if move.type == "Jump":
                move.weight += -99 - len(move.jumped)
            if move.type != "Jump":
                matrix.insert(move, tablero, depth)
    
    return (sorted(no_coronado_moves, key=lambda move: move.weight), sorted(coronado_moves, key=lambda move: move.weight))

def enemyJump(tablero, move, color):
    enemy_jumps = findJumps(move.apply(copytablero(tablero)), not color)
    for jump in enemy_jumps:
        for victim in jump.jumped:
            if victim.ficha.id == move.ficha.id:
                return True
    return False

def Mejora_Move1(tablero, move, color):
    enemy_jumps = findJumps(tablero, not color)
    for jump in enemy_jumps:
        for otherpieza in jump.otherpiezas:
            if otherpieza.x == move.pieza.x and otherpieza.y == move.pieza.y:
                return True
        if move.pieza.x == jump.pieza.x and move.pieza.y == jump.pieza.y:
            return True
    return False

def Mejora_Move2(tablero, move, color):
    if color:
        if move.pieza.x / 62.5 == 7:
            return True
    elif not color:
        if move.pieza.x / 62.5 == 0:
            return True

def Mejora_Move3(tablero, move, color):
    enemy_jumps = findJumps(tablero, not color)
    for jump in enemy_jumps:
        for victim in jump.jumped:
            if victim.x / 62.5 == move.ficha.x and victim.y / 62.5 == move.ficha.y:
                return True
    return False

def Mejora_Ganar(tablero, move, color):
    new_tablero = move.apply(tablero)
    win_val = 0
    if color:
        win_val = -1
    else: 
        win_val = 1
    if hasWon(tablero) == win_val:
        return True
    else:
        return False

def Mejora_Move4(tablero, move, color):
    jumps = findJumps(move.apply(copytablero(tablero)), not color)
    for jump in jumps:
        for otherpieza in jump.otherpiezas:
            if otherpieza.x/62.5 == move.ficha.x and otherpieza.y/62.5 == move.ficha.y:
                return True
        if jump.pieza.x/62.5 == move.ficha.x and jump.pieza.y/62.5 == move.ficha.y:
            return True

    return False

def minimax(depth, color, tablero, a, b):
    if depth == DIFFICULTY:
        moves = weightablero(tablero, depth)
        if color:
            #Mejor movimiento para la IA
            coronado_moves = moves[1]
            mini = None
            for move in coronado_moves:
                if mini is None:
                    mini = move
                elif mini.weight > move.weight:
                    mini = move
                b = min(b, mini.weight)
                if b <= a:
                    break
            return mini
        else:
            #Mejor movimiento para la Ti xd
            no_coronado_moves = moves[0]
            maxi = None
            for move in no_coronado_moves:
                if maxi is None:
                    maxi = move
                elif maxi.weight < move.weight:
                    maxi = move
                a = max(a, maxi.weight)
                if b <= a:
                    break
            return maxi

    best_move = None
    if color:
        coronado_moves = findMoves(tablero, True) + findJumps(tablero, True)
        if best_move is not None:
            return best_move
        for move in coronado_moves:
            copy = copytablero(tablero)
            val = minimax(depth + 1, False, move.apply(copy), a, b)
            if best_move is None or val.weight < best_move.weight or move.type == "Jump":
                best_move = val
            b = min(b, best_move.weight)
            if b <= a:
                break
    else:
        no_coronado_moves = findMoves(tablero, False) + findJumps(tablero, False)
        for move in no_coronado_moves:
            val = minimax(depth + 1, True, move.apply(copytablero(tablero)), a, b)
            if best_move is None or val.weight > best_move.weight:
                best_move = val
            a = max(a, best_move.weight)
            if b <= a:
                break
    return best_move

width = 500
height = 500
offset_x = width / 8
offset_y = height / 8
win = graphics.GraphWin("fichas", width, height)

def drawtablero():
    color_offset = False
    for x in range(0, 8):
        if x % 2 == 1:
            color_offset = True
        else:
            color_offset = False
        for y in range(0, 8):
            point = Point(x * offset_x, y * offset_y)
            box = graphics.Rectangle(point, Point(point.x + offset_x, point.y + offset_y))
            box.setFill("Black")
            if color_offset:
                if x % 2 == 0 or y % 2 == 0:
                    #box.setFill("#c2ab56")
                    box.setFill("#e3e4e5")
            elif x % 2 == 1 or y % 2 == 1:
                #box.setFill("#c2ab56")
                box.setFill("#e3e4e5")
            box.draw(win)

def drawfichas():
    for pieza in tablero.flat:
        if pieza.ficha is not None:
            circle = graphics.Circle(Point(pieza.center[0], pieza.center[1]), 15)
            if pieza.ficha.coronado:
                #circle.setFill("Black")
                circle.setFill("#e60000")
            else:
                circle.setFill("#4d4dff")
            circle.draw(win)

def findPieza(click):
    click_x = click.x/62.5
    click_y = click.y/62.5
    for x in range(0, 8):
        for y in range(0, 8):
            if (click_x > x and click_y > y) and (click_x < x+1 and click_y < y+1):
                return (x, y)
    return None

def redraw():
    for child in win.children:
        child.undraw()
    drawtablero()
    drawfichas()


def runAI(color):
    t1 = time.time()
    ai_move = minimax(0, color, tablero, float("-inf"), float("inf"))
    print(ai_move.weight)
    t2 = time.time()
    print(t2-t1)
    matrix.tabla_hash = {}
    ai_move.apply(tablero)
    redraw()
    return ai_move


def chooseDif():
    difwin = graphics.GraphWin("Choose Difficulty")
    difwin.focus()
    entry = graphics.Entry(Point(100, 100), 20)
    entry.setText("2")
    entry.draw(difwin)
    difwin.getMouse()
    DIFFICULTY = int(entry.getText())
    difwin.close()

def playerTurn(color):
    while True:
        click1 = win.getMouse()
        ficha = findPieza(click1)
        if ficha is None or tablero[int(ficha[0]), int(ficha[1])].ficha is None or tablero[int(ficha[0]), int(ficha[1])].ficha.coronado is not color:
            continue
        click2 = win.getMouse()
        pieza = findPieza(click2)
        if pieza is None or (pieza[0] == ficha[0] and pieza[1] == ficha[1]):
            continue
        partial_move = Move(tablero[int(ficha[0]), int(ficha[1])].ficha, tablero[int(pieza[0]), int(pieza[1])],"?")
        partial_move.ficha.x = ficha[0]
        partial_move.ficha.y = ficha[1]
        move = getFullMove(partial_move)
        if move is None:
            continue
        else:
            move.apply(tablero)
            redraw()
            return

def draw():
    chooseDif()
    drawtablero()
    drawfichas()
    while hasWon(tablero) == 0:
        sleep(0.01)
        King(tablero)
        playerTurn(False)
        King(tablero)
        win.update()
        runAI(True)
    winWindow = graphics.GraphWin("Game over")
    if hasWon(tablero) == 1:
        text = graphics.Text(Point(winWindow.width/2, winWindow.height/2), "You Won!!")
        text.draw(winWindow)
        sleep(3)
    elif hasWon(tablero) == -1:
        text = graphics.Text(Point(winWindow.width / 2, winWindow.height / 2), "You Lost :(")
        text.draw(winWindow)
        sleep(3)
    return

draw()

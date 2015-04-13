# Conway's Game of Life
"""
I chose red for all cells with less than 2 or more than 3 neighbours because they're going to die :(

I chose yellow for all cells with 2 neighbours because the cell is still alive but it's at risk of dying by losing a neighbour

I chose green for cells with 3 neighbours because while the cell is alive with 3 neighbours, it also has the opportunity to
    spawn a new cell from a previously dead one
"""

import turtle
import random

CELL_SIZE = 8

class LifeBoard:
    "Game of Life board, a rectangular board with live and dead cells"

    def __init__(self, width, height):
        "Create a new Game of Life board of specified size."
        self.live = set()
        self.width, self.height = width, height

    def makeRandom(self):
        "Fill the board with a random pattern"
        self.erase()
        for x in range(self.width):
            for y in range(self.height):
                if random.random() > 0.5:
                    self.live.add((x, y))

    def toggle(self, x, y):
        """Toggle a cell's state between live and dead; do nothing
        if (x, y) are outside the board."""
        if (0 <= x < self.width) and (0 <= y < self.height):
            if (x, y) in self.live:
                self.live.remove((x, y))
            else:
                self.live.add((x, y))

    def erase(self):
        "Clear the entire board."
        self.live.clear()    

    def step(self):
        "Compute the next generation according to Conway's rule."
        n = set()
        for x in range(self.width):
            for y in range(self.height):
                c = 0
                for xp in range(x - 1, x + 2):
                    for yp in range(y - 1, y + 2):
                        c = c + ((x, y) != (xp, yp) in self.live)
                if (x, y) in self.live:
                    if c in (2, 3): n.add((x, y)) # survival
                else:
                    if c == 3: n.add((x, y)) # birth                    
        self.live = n
            
    def display(self):
        "Draw the whole board"
        turtle.clear()
        turtle.color('black')
        turtle.setheading(0)
        for (x, y) in self.live:
            turtle.penup()
            turtle.setpos(x * CELL_SIZE, y * CELL_SIZE)
            c = 0
            for xp in range(x - 1, x + 2):
                for yp in range(y - 1, y + 2):
                    c = c + ((x, y) != (xp, yp) in self.live)
            if c < 2:
                turtle.color('red')
            if c == 2:
                turtle.color('yellow')
            if c == 3:
                turtle.color('green')
            if c >3:
                turtle.color('red')
            turtle.pendown()
            turtle.begin_fill()
            for i in range(4):
                turtle.forward(CELL_SIZE - 1)
                turtle.left(90)
            turtle.end_fill()
        turtle.update()


def main():
    # set up window
    width, height = turtle.screensize()
    turtle.setworldcoordinates(0, - 20, width, height - 20)
    turtle.title('Game of Life')

    # write instructions
    writer = turtle.Turtle()
    writer.hideturtle()
    writer.penup()
    writer.setposition(5, -15)
    writer.write("E)rase the board    R)andom fill    S)tep once\
        C)ontinuously step until 'S'    Q)uit    click to toggle", font=('sans-serif', 14, 'normal'))    

    # set up board
    turtle.hideturtle()
    turtle.speed('fastest')
    turtle.tracer(0, 0) # turn off animation; update() needs to be called
    board = LifeBoard(width // CELL_SIZE, (height - 20) // CELL_SIZE)
    board.makeRandom()
    board.display()

    # set up mouse bindings
    def toggle(x, y):
        board.toggle(int(x) // CELL_SIZE, int(y) // CELL_SIZE)
        board.display()
    turtle.onscreenclick(toggle)

    # set up key bindings
    def erase():
        board.erase()
        board.display()
    turtle.onkey(erase, 'e')

    def makeRandom():
        board.makeRandom()
        board.display()
    turtle.onkey(makeRandom, 'r')

    turtle.onkey(turtle.bye, 'q')
    
    def step_once():
        global continuous
        continuous = False
        perform_step()
    turtle.onkey(step_once, 's')

    def step_continuous():
        global continuous
        continuous = True
        perform_step()
    turtle.onkey(step_continuous, 'c')

    def perform_step():
        global continuous
        board.step()
        board.display()
        if continuous: # in continuous mode,
            turtle.ontimer(perform_step, 25) # do again after 25 ms

    # set focus on screen and enter the main loop
    turtle.listen()
    turtle.mainloop()

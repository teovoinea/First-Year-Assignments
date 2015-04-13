import math
from turtle import *

# Physical constants
G = 6.67428e-11     # gravitational constant
AU = 149.6e6 * 1000 # 149.6 million km, in meters.

# Simulation parameters
SCALE = 250 / AU
TIMESTEP = 24*3600  # One day

play = 2

class Body(Turtle):
    """Subclass of Turtle representing a gravitationally-acting body.

    Extra attributes:
    mass : mass in kg
    vx, vy: x, y velocities in m/s
    px, py: x, y positions in m
    """

    def __init__(self, mass, px, py, vx, vy, color):
        Turtle.__init__(self)
        self.mass, self.px, self.py, self.vx, self.vy = mass, px, py, vx, vy
        self.pencolor(color)
        self.penup()
        self.hideturtle()

    
    def attraction(self, other):
        """Returns a pair with the graviational force between self and
        other in horizontal and vertical direction; self must be distinct
        from other.
        """
        if self is other:
            raise NameError('Cannot attract self')
        dx = (other.px - self.px)
        dy = (other.py - self.py)
        d = math.sqrt(dx**2 + dy**2)

        f = G * self.mass * other.mass / (d**2)
        theta = math.atan2(dy, dx)
        fx = math.cos(theta) * f
        fy = math.sin(theta) * f
        return fx, fy

def step(bodies):
    """Updates the attributes vx, vy, px, py of all bodies with
    the new velocity and position after TIMESTEP"""
    force = {}
    for b in bodies:
        totalFx = totalFy = 0.0
        for other in bodies:
            if b is other:
                continue
            fx, fy = b.attraction(other)
            totalFx += fx
            totalFy += fy
        force[b] = (totalFx, totalFy)
    for b in bodies:
        fx, fy = force[b]
        b.vx += fx / b.mass * TIMESTEP
        b.vy += fy / b.mass * TIMESTEP

        b.px += b.vx * TIMESTEP
        b.py += b.vy * TIMESTEP



def display(bodies):
    for body in bodies:
        body.goto(body.px * SCALE, body.py * SCALE)
        body.dot(3)

def stop():
    global play
    play += 1
    if play % 2 == 0:
        return True
    else: return False
def main():
    sun = Body(1.98892 * 10**30, 0, 0, 0, 0, 'yellow')
    earth = Body(5.9742 * 10**24, - AU, 0, 0, 29783, 'blue') # 29.783 km/sec
    venus = Body(4.8685 * 10**24, 0.723 * AU, 0, 0, -35020, 'red')
    bodies = [sun, earth, venus]
    listen()
    while True:#stop():
        step(bodies)
        display(bodies)
        onkey(stop, 'space')
        onkey(bye, 'q')


# Example 4.1: A single particle

from PVector import *

class Particle:
    def __init__(self, l):
        self.location = l.get()
        self.velocity = PVector(random(-1.,1.), random(-2.,0))
        self.acceleration = PVector(0, 0.05)
        self.lifespan = 1.0
    
    def run(self):
        self.update()
        self.display()
    
    def update(self):
        self.velocity.add(self.acceleration)
        self.location.add(self.velocity)
        self.lifespan -= 0.0075
    
    def display(self):
        stroke(0, self.lifespan)
        fill(0.6, self.lifespan)
        oval(self.location.x, self.location.y, 8, 8)
    
    def isDead(self):
        if(self.lifespan < 0.0):
            return True
        else:
            return False


size(640, 360)
speed(60)
background(1)

def setup():
    global p
    p = Particle(PVector((WIDTH/2), 10))
    
def draw():
    global p
    p.run()
    if(p.isDead()):
        print('Particle dead!')



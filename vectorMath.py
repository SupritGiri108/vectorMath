import math
import numpy as np
from multipledispatch import dispatch

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Graph:
    def __init__(self, c=None):
        if c is None:
            c = []
        self.c = c

    @dispatch(float, float)
    def appendVect(self, x, y):
        vect = Vector(x, y)
        self.c.append(vect)

    @dispatch(Vector)
    def appendVect(self, vect: Vector):
        self.c.append(vect)

    @dispatch(float, float)
    def removeVect(self, x, y):
        vect = Vector(x, y)
        self.c.remove(vect)

    @dispatch(Vector)
    def removeVect(self, vect: Vector):
        self.c.remove(vect)

    @dispatch(float, float, float, float)
    def addVect(self, x1: float, y1: float, x2: float, y2: float):
        new_x = x1 + x2
        new_y = y1 + y2
        newVect = Vector(new_x, new_y)
        self.appendVect(newVect)
        return newVect

    @dispatch(Vector, Vector)
    def addVect(self, v1: Vector, v2: Vector):
        new_x = v1.x + v2.x
        new_y = v1.y + v2.y
        newVect = Vector(new_x, new_y)
        self.appendVect(newVect)
        return newVect

    @dispatch(float, float, float, float)
    def subVect(self, x1: float, y1: float, x2: float, y2: float):
        new_x = x1 - x2
        new_y = y1 - y2
        newVect = Vector(new_x, new_y)
        self.appendVect(newVect)
        return newVect

    @dispatch(Vector, Vector)
    def subVect(self, v1: Vector, v2: Vector):
        new_x = v1.x - v2.x
        new_y = v1.y - v2.y
        newVect = Vector(new_x, new_y)
        self.appendVect(newVect)
        return newVect

    @dispatch(Vector)
    def showVect(self, vect: Vector):
        return (vect.x, vect.y)

    def showGraph(self):
        d = []
        for vect in self.c:
            d.append(self.showVect(vect))
        print(d)

    def findMagnitude(self, vect: Vector):
        xSq = vect.x ** 2
        ySq = vect.y ** 2
        return math.sqrt(xSq + ySq)


    def findDirection(self, vect: Vector, angle: str = "radians"):
        if angle == 'radians':
            direction = np.arctan(vect.y / vect.x)
        elif angle == 'degrees':
            direction = np.arctan(vect.y / vect.x) * (180 / np.pi)

        if vect.x < 0 and vect.y >= 0:  # quadrant 2
            direction += np.pi if angle == 'radians' else 180
        elif vect.x < 0 and vect.y < 0:  # quadrant 3
            direction += np.pi if angle == 'radians' else 180
        elif vect.x >= 0 and vect.y < 0:  # quadrant 4
            direction += 2 * np.pi if angle == 'radians' else 360

        return direction

    def scalarMultiplication(self, scalar, vect: Vector):
        scVectX = scalar * vect.x
        scVectY = scalar * vect.y
        new_vect = Vector(scVectX, scVectY)
        return self.showVect(new_vect)

    def findComponents(self, magnitude: float, direction: float, angle: str = "radians"):
      if angle == "radians":
        x_comp = magnitude * np.cos(direction)
        y_comp = magnitude * np.sin(direction)
        vect = Vector(x_comp, y_comp)
        self.appendVect(vect)
        return self.showVect(vect)
      elif angle == "degrees":
        direction = direction * (np.pi/180)
        x_comp = magnitude * (np.cos(direction))
        y_comp = magnitude * (np.sin(direction))
        vect = Vector(x_comp, y_comp)
        self.appendVect(vect)
        return self.showVect(vect)



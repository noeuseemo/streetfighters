from tkinter import Tk, Canvas
from random import randrange

class Weapon(): 
    def __init__(self, c, n, d):
        self._canvas = c
        self._baseDamage = d
        self._name = n

    def display(self, x, y):
        pass

    def hit(self):
        damage = randrange(self._baseDamage-5, self._baseDamage+5)
        return damage
        

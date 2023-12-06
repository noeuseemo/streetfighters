from tkinter import Tk, Canvas
from weapon import Weapon

class Sword(Weapon):
    def __init__(self, c, n, d):
        self._canvas = c
        self._baseDamage = d
        self._name = n

    def display(self, x, y):
        pass

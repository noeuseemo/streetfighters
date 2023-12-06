from tkinter import Tk, Canvas, ARC, W
from human import Human


class Hero(Human):
    def __init__(self, canvas, name, x, y, gender, state):
        super().__init__(canvas, name, x, y, gender)
        self.health = 100
        self._wp = None
        self.isShield = False
        self.shieldBlock = 5
        self.state = state

    def setWeapon(self, weapon):
        self._wp = weapon

    def setShield(self):
        self.isShield = True

    def attack(self, enemy):
        damage = self._wp.hit()

        if enemy.health >= 1:
            if self.gender == 'М':
                if self.isShield:
                    enemy.health = (enemy.health - damage) + self.shieldBlock
                    return f'{self.name} нанес {damage} урона {enemy.name}, но щит заблокировал {self.shieldBlock}\n', enemy.health, enemy.name
                else:
                    enemy.health -= damage
                    return f'{self.name} нанес {damage} урона {enemy.name}\n', enemy.health, enemy.name
            else:
                if self.isShield:
                    enemy.health = (enemy.health - damage) + self.shieldBlock
                    return f'{self.name} нанесла {damage} урона {enemy.name}, но щит заблокировал {self.shieldBlock}\n', enemy.health, enemy.name
                else:
                    enemy.health -= damage
                    return f'{self.name} нанесла {damage} урона {enemy.name}\n', enemy.health, enemy.name

    def _DrawName(self):
        super()._DrawName()
        self.canvas.create_rectangle(self.x+1.5,
                                     self.y-230,
                                     self.x+1.5+100,
                                     self.y-300+80,
                                     outline="#FFF", fill="#FFF", width=2)
        
        self.canvas.create_rectangle(self.x+1.5,
                                     self.y-230,
                                     self.x+1.5+self.health,
                                     self.y-300+80,
                                     outline="#FFF", fill="#1f1", width=2)

    def _DrawWeapon(self):
        self.canvas.create_line(self.x+80,
                                self.y-50,
                                self.x+100,
                                self.y-150,
                                fill='#F00', width=2)

    def _DrawShield(self):
       self.canvas.create_arc(self.x + 50, self.y - 150, self.x + 150, self.y - 20, width=2, fill='grey', start=180, extent=180) #координаты чудун турун
       
       


    def display(self):
        super().display()
        if self.state == 1:
            self._DrawWeapon()
        else:
            self._DrawShield()

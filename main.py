from tkinter import Tk, Canvas
from grid import Grid
from human import Human
from hero import Hero
from sword import Sword
import random
import time

root = Tk()
canvas = Canvas (root, width = 800, height=600)
canvas.pack()
grid = Grid (canvas)
grid.display(root)

f = open("students.txt", 'r', encoding='utf-8')
random_people = []

for i in f:
    g = i.split(";")
    id = int(g[0])
    name = g[1]
    gender = g[4]
    random_people.append({"id":id, 'full_name':name, 'gender':gender})

sword1 = Sword(canvas, 'dragonLore', 10)
human1 = random.choice(random_people)
random_people.remove(human1)
name = f"{human1['full_name'].split()[0]} {human1['full_name'].split()[1][0]}.{human1['full_name'].split()[2][0]}."
p1 = Hero(canvas, name ,100,500, human1['gender'], 0)
p1.setWeapon(sword1)

sword2 = Sword(canvas, 'apex', 12)
human2 = random.choice(random_people)
name = f"{human2['full_name'].split()[0]} {human2['full_name'].split()[1][0]}.{human2['full_name'].split()[2][0]}."
p2 = Hero(canvas, name, 300, 500, human2['gender'], 1)
p2.setShield()
p2.setWeapon(sword2)

p1.display()
p2.display()

while True:
    p2Health = p1.attack(p2)
    grid.updateText(p2Health[0])
    grid.updateText(f'{p2Health[2]} - {p2Health[1]} \n')
    p1Health = p2.attack(p1)
    grid.updateText(p1Health[0])
    grid.updateText(f'{p1Health[2]} - {p1Health[1]} \n')
    if p1Health[1] <= 0:
        grid.updateText(f'Победил игрок {p2.name}')
        break
    if p2Health[1] <= 0:
        grid.updateText(f'Победил игрок {p1.name}')
        break

p1.display()
p2.display()

root.mainloop()

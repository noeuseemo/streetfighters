from tkinter import Tk, Canvas, Frame, BOTH, W


class Human:
    def __init__(self, canvas, name, x, y, gender):
        self.canvas = canvas
        self.name = name
        self.x = x
        self.y = y
        self.gender = gender

    def display(self):
        self._DrawName()
        self._DrawHead()
        self._DrawBody()
        self._DrawLeggs()
        self._DrawHands()
        self._DrawFace()
        self._DrawFace1()
        self._DrawSmailFace()
        if self.gender == "Ж":
            self._DrawPigtails()
        if self.gender == "М":
            self._DrawHair()

    def _DrawName(self):
        self.canvas.create_text(self.x + 24.5, self.y - 200, text=self.name, font="Times 18", anchor=W, fill="green")

    def _DrawHead(self):
        self.canvas.create_oval(self.x + 20, self.y - 180, self.x + 80, self.y - 120, width=2)

    def _DrawBody(self):
        self.canvas.create_line(self.x + 50, self.y - 120, self.x + 50, self.y - 50, width=2)

    def _DrawLeggs(self):
        self.canvas.create_line(self.x, self.y, self.x + 50, self.y - 50, self.x + 100, self.y, width=2)

    def _DrawLeggs(self):
        self.canvas.create_line(self.x, self.y, self.x + 50, self.y - 50, self.x + 100, self.y, width=2)

    def _DrawHands(self):
        self.canvas.create_line(self.x + 10, self.y - 70, self.x + 50, self.y - 110, self.x + 90, self.y - 70, width=2)

    def _DrawFace(self):
        self.canvas.create_oval(self.x + 35, self.y - 165, self.x + 45, self.y - 155, width=2)

    def _DrawFace1(self):
        self.canvas.create_oval(self.x + 55, self.y - 165, self.x + 65, self.y - 155, width=2)

    def _DrawSmailFace(self):

        self.canvas.create_arc(self.x + 40, self.y - 150, self.x + 60, self.y - 135, width=2, start=0, extent=-180)

    def _DrawHair(self):
        self.canvas.create_line(self.x + 35, self.y - 185, self.x + 35, self.y - 175, width=2)
        self.canvas.create_line(self.x + 50, self.y - 190, self.x + 50, self.y - 180, width=2)
        self.canvas.create_line(self.x + 65, self.y - 185, self.x + 65, self.y - 175, width=2)

    def _DrawPigtails(self):
        self.canvas.create_line(self.x + 25, self.y - 100, self.x + 35, self.y - 175, width=2)
        self.canvas.create_line(self.x + 85, self.y - 100, self.x + 65, self.y - 175, width=2)

from tkinter import Canvas, Tk
from random import randint

class PadKruh():
    def __init__(self, x, y, can):
        self.r = randint(10,30)
        self.can=can
        self.id=self.can.create_oval(x-self.r,y-self.r, x+self.r, y+self.r)
        self.pohnisa()

    def pohnisa(self):
        self.v = self.r/10
        self.can.move(self.id, 0, self.v)
        self.can.after(10, self.pohnisa)

        
def klik(event):
    PadKruh(event.x, event.y, can)


root = Tk()
can=Canvas(root, height = 1000, width = 1000)
can.pack()
can.bind('<Button-1>', klik)

pk=PadKruh(50, 50, can)
pk.pohnisa()

root.mainloop()




from tkinter import Canvas as Can
from tkinter import Tk
class Prvok():
    def __init__(self, a):
        self.info = a
        self.next = None

class SpajanyZ():
    def __init__(self,can):
        self.first = Prvok(None)
        self.pointer = self.first
        self.can= can
        self.y = -1

    def append(self,newInfo):
        self.pointer.next = Prvok(newInfo)
        self.pointer = self.pointer.next
        if self.y !=-1:
            can.delete(self.id1)
            can.delete(self.id2)
            can.delete(self.id3)
            self.vlak(self.can,self.y)

    def read(self):
        pointer = self.first
        while pointer != None:
            print(pointer.info,end = ' ')
            pointer = pointer.next

    def sucet(self):
        pocet=0
        pointer=self.first.next
        while pointer !=None:
            pocet+=pointer.info
            pointer = pointer.next
        return pocet

    def leng(self):
        pocet=0
        pointer=self.first.next
        while pointer !=None:
            pocet+=1
            pointer = pointer.next
        return pocet

    def vlak(self,can, y):
        self.y = y
        x=10
        pointer = self.first.next
        while pointer !=None:
                self.id1 = can.create_rectangle(x,y-20, x + 50,y+20)
                self.id2 = can.create_line(x+50,y, x+70,y)
                self.id3 = can.create_text(x+25,y, text = pointer.info)
                x+=70
                pointer = pointer.next

            

        


can = Can(Tk(),width=600,height = 600)
can.pack()

Z1 = SpajanyZ(can)
Z1.read()
Z1.append(2)
Z1.append(4)
Z1.read
Z1.append(7)
Z1.append(8)
Z1.read()
print(Z1.sucet())
print(Z1.leng())
Z1.vlak(can,100)

Z1.append(10)
Z1.append(20)
Z1.append(60)

  


Tk().mainloop()
print('xd')
from tkinter import Canvas as Can
from tkinter import Tk


class Node():
    def __init__(self, info):
        self.left = None
        self.right = None
        self.info = info

class BinTree():
    def __init__(self):
        self.koren = Node(None)    


    def read(self):
        def funk(node):
            if node ==None:
                return 

            print(node.info)
            read(node.left)
            read(node.right)
        return funk(self.koren)

    def sum(self):
        def funk(node):
            suma = 0
            if node ==None:
                return 0

            suma += node.info
            suma+=funk(node.left)
            suma+=funk(node.right)
            # print(node.info)
            # read(node.left)
            # read(node.right)
            return suma
        return funk(self.koren)
    
    def readDraw(self,  y):
        def funk(node, y, minOfCan, widthOfCan):
            c = 40
            if node ==None:
                return
            print(node.info, minOfCan, widthOfCan) 
            can.create_text((minOfCan+widthOfCan)/2,y, text = node.info)
            # print(node.info)
            if node.left!=None:
                print(node.info, minOfCan, widthOfCan)
                x = (minOfCan+widthOfCan)//2
                print(x, x/2)
                can.create_line(x,y+10, x - abs(widthOfCan-minOfCan)/4, y+c)

            funk(node.left, y+c+10, minOfCan, (minOfCan+ widthOfCan)//2)

            if node.right!=None:
                x = (minOfCan+widthOfCan)//2
                can.create_line(x, y+10, (widthOfCan-minOfCan)/4+x, y+c)
            funk(node.right, y+c+10, (minOfCan+widthOfCan)//2, widthOfCan)
        return funk(self.koren, y,0, int(can['width']))
    

    def listy():
        def funk(node):
            if node == None:
                return
            if node.left==None and node.right==None:
                print(node.info)

            listy(node.left)
            listy(node.right)
        return funk(self.koren)
    def sumlisty(self):
        def funk(node):
            suma = 0
            if node == None:
                return 0
            if node.left==None and node.right==None:
                suma += node.info

            suma+=funk(node.left)
            suma+=funk(node.right)
            return suma
        return funk(self.koren)












# def animation(y, x):
#     z = 0

#     d= 5
#     can.delete('all')
#     id = can.create_line(300-z, y, 300+z,y)
    
#     z+=d
#     if z > x:
#         d*=-1
#     elif z<0:d*=-1
#     can.after(animation(y,x),5)
    
        
        
        


# koren = Node(2)
# koren.left  = Node(2)
# koren.left.left = Node(1)
# koren.left.left.left = Node(-3)
# koren.left.left.right = Node(2)
# koren.left.left.right.left = Node(1)
# koren.right = Node(1)
# koren.right.left = Node(7)
# koren.right.right = Node(1)
# koren.right.right.right = Node(7)


# read(koren)

# listy(koren)
# print(sum(koren),'cely')
# print(sumlisty(koren), 'listy')

BS = BinTree()
BS.koren = Node(15)
BS.koren.left = Node(-2)
BS.koren.right = Node(-3)
BS.koren.right.right = Node(1)
BS.koren.right.right = Node(2)
BS.koren.left.left = Node(3)
BS.koren.left.right = Node(4)
BS.koren.left.right.left = Node(6)
BS.koren.left.right.right = Node(8)



print(BS.sum())
print(BS.sumlisty())


tk = Tk()
can = Can(tk,width=600,height = 600)
can.pack()

BS.readDraw(10)

# readDraw(koren,300,10)

# animation(300,150)

# can.bind('<Button-1>',klik)

tk.mainloop()
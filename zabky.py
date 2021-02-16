from tkinter import Canvas as Can
from tkinter import Tk
from random import randint,shuffle
import tkinter as tkin
tk = Tk()
can = Can(tk,width=600,height = 200)
can.pack()



# n = int(input())
n=8
arr= [""]
for i in range(1,n+1):
    arr.append(i)

shuffle(arr)
def klik(event):
    
    index2 = arr.index('')
   
    
    x= event.x
        
    if x//40<=n:
        index = x//40
        if abs(index-index2)<3:
            arr[index2]=arr[index]
            arr[index]=""
            pole = arr.copy()
            pole.pop(index)
            if all(pole[i] <= pole[i+1] for i in range(len(pole)-1)):
                print('usortoval si ')
            
        vykresli()

def vykresli():
    can.delete('all')
    for i in range(n+1):
        can.create_rectangle(40*i+2,2,40*i+40,40)
        can.create_text(40*i+20,20, text=arr[i])
vykresli()
can.bind('<Button-1>',klik)














# can.bind('<Button-1>',klik)

tk.mainloop()

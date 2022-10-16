import random
import time
random.seed(time.process_time())
#k1, k2, k3, k4
k1 = random.randint(60, 100)
k2 = random.randint(60, 100)
k3 = random.randint(60, 100)
k4 = random.randint(60, 100)
Plist = [k1, k2, k3, k4]
Nlist = ["PT", "PC", "PA", "PU"]

Maxi = 0
Maxper = 0
for x in range(1, 4):
    Pe = Plist[x]
    if x == 1 or Pe > Maxper:
        Maxper = Pe
        Maxi = x

name = Nlist[Maxi]

print(name)

import tkinter
from tkinter import *

window = Tk()
window.title("UltrasonidoALi")
window.geometry("500x500")

canvas = Canvas(window, width= 400, height= 500, bg="SpringGreen2")
#canvas.place(x=100, y=0)

#Add a text in Canvas
textcanvas = Frame(window, width= 100, height= 10, bg="White")
region_text = tkinter.Label(textcanvas, width=20, height=1, text="TICK TESTING...", bg="white", font=('Helvetica 15 bold'))
region_text.pack()
textcanvas.pack()

size = 400
px = 0
py = 150-size/2
usrange = 70
fixedstart = 180+usrange/2
fixedextent = usrange+usrange/2
coord = px, py, px+size, py+size
arc = canvas.create_arc(coord, start=fixedstart, extent=fixedextent, fill="white")

canvas.pack(side="right")

credit = 0
def add(amount, name):
    global credit
    credit += amount
    region_text.configure(text=name)



menucanvas = Canvas(window, width= 100, height= 500, bg="SpringGreen2")
for x in range(0,4):
    name = Nlist[x]
    #Button(window, text=name, command=lambda: add(.1)).grid(row=2+x, column=1)

    def customfunction():
        add(.1, name)
        region_text.pack()

    button = tkinter.Button(menucanvas, text=name, command=customfunction,height=1, width=20)
    button.pack()




menucanvas.pack(side="left")
tkinter.Misc.lift(canvas)



"""
print("*******STARTING********")
m = 100
for x in range(1, m):
    print("tick")

print("*******ENDING********")
"""

window.mainloop()
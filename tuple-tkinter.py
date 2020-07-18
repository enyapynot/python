from tkinter import *
from time import *

class myframe(Frame):
  def __init__(self):
    Frame.__init__(self)
    
    self.myCanvas = Canvas(width=1000, height=700, bg="white")
    self.myCanvas.grid()
    self.myCanvas.create_rectangle(10, 10, 20, 20, fill="red")
    self.myCanvas.create_rectangle(10, 30, 20, 40, fill="green")
    self.myCanvas.create_rectangle(10, 50, 20, 60, fill="blue")
    print("find Everything")
    print(self.myCanvas.find_enclosed(0,0,30,70))
    print("find middle")
    print(self.myCanvas.find_enclosed(0,25,30,45))
    print("find nothing")
    print(self.myCanvas.find_enclosed(0,0,1,1))
    
frame01=myframe()
frame01.mainloop()

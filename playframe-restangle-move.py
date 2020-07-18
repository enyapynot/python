from tkinter import *
from time import *

class myframe(Frame):
  def __init__(self):
    Frame.__init__(self)
    
    self.myCanvas = Canvas(width=800, height=600, bg="white")
    self.myCanvas.grid()
    for count in range(10):
      increment = 10*count
      self.myCanvas.create_rectangle(10 + increment,
      10 + increment, 50 + increment, 50 + increment)
      self.myCanvas.update()
      sleep(1)
      self.myCanvas.create_rectangle(10 + increment,
      10 + increment, 50 + increment, 50 + increment,
      outline="white")
      self.myCanvas.update()


frame01=myframe()
frame01.mainloop()



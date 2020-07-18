from tkinter import *
from time import *

class myframe(Frame):
  def __init__(self):
    Frame.__init__(self)
    
    self.myCanvas = Canvas(width=800, height=600, bg="white")
    self.myCanvas.grid()
    myshape_id=self.myCanvas.create_rectangle(10, 10, 50, 50)
    self.myCanvas.update()
    for count in range(10):
      print (count)
      sleep(1)
      increment = 10*count
      self.myCanvas.coords(myshape_id,10 + increment,
      10 + increment, 50 + increment, 50 + increment)
      self.myCanvas.update()
frame01=myframe()
frame01.mainloop()



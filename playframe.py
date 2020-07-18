from tkinter import *

class myframe(Frame):
  def __init__(self):
    Frame.__init__(self)
    self.mycanvas = Canvas(width=450, height=400, bg="green")
    self.mycanvas.grid()
  

frame01=myframe()
frame01.mainloop()

from tkinter import *

class myframe(Frame):
  def __init__(self):
    Frame.__init__(self)
    self.mycanvas = Canvas(width=450, height=400, bg="white")
    self.mycanvas.grid()
    self.mycanvas.create_line(10,10,100,100, arrow="last")


frame01=myframe()
frame01.mainloop()

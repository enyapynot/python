from tkinter import *

class myframe(Frame):
  def __init__(self):
    Frame.__init__(self)
    self.mycanvas = Canvas(width=450, height=400, bg="blue")
    self.mycanvas.grid()
    self.mycanvas.create_rectangle(10,10,100,200, fill="red")
    self.mycanvas.create_oval(10,10,100,200, width=0, fill="pink")


frame01=myframe()
frame01.mainloop()

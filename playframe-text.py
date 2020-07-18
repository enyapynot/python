from tkinter import *

class myframe(Frame):
  def __init__(self):
    Frame.__init__(self)
    self.myCanvas = Canvas(width=450, height=400, bg="white")
    self.myCanvas.grid()
    self.myCanvas.create_text(150, 150, text="Hello World",
        width=250, fill="blue", anchor="sw",
        justify="center", font=("Times", 32))

frame01=myframe()
frame01.mainloop()

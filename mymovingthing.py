from tkinter import *
from time import *

class myframe(Frame):
  def __init__(self):
    Frame.__init__(self)
    
    self.myCanvas = Canvas(width=1000, height=700, bg="cyan")
    self.myCanvas.grid()
    self.myCanvas.create_polygon(0,0,0,100,100,0, fill="dark green")
    self.myCanvas.create_polygon(0,600,0,700,100,700, fill="dark green")
    self.myCanvas.create_polygon(1000,700,1000,600,900,700, fill="dark green")
    self.myCanvas.create_polygon(1000,0,900,0,1000,100, fill="dark green")
    MyShape=self.myCanvas.create_oval(333,267,667,542, fill="indigo")
    
    while True:
      for i in 10,20,30,40,50,60,70,80,90,100,110,120,130,140,130,120,110,100,90,80,70,60,50,40,30,20,10,0:
        self.myCanvas.coords(MyShape, 50+i,267-i,(1.5*667-i),450+i)
        sleep(0.03)
        self.myCanvas.update()

frame01=myframe()
frame01.mainloop()



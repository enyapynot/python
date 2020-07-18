from tkinter import *
from time import *

class MyFrame(Frame):
  def __init__(self):
     Frame.__init__(self)

     self.myCanvas = Canvas(width=500, height=300, bg="light sky blue")
     self.myCanvas.grid()
     
     '''draw hills and house'''
     self.myCanvas.create_oval(200, 100, 700, 600, outline="black", fill="spring green", width=2)
     self.myCanvas.create_oval(-100, 200, 400, 600, outline="black", fill="forest green", width=3)
     self.myCanvas.create_rectangle(100, 160, 150, 210, outline="black", fill="red", width=1)

     for count in range(45):
         '''draw roof'''
         increment = count
         self.myCanvas.create_line(80 + increment, 160 - increment, 170 - increment, 160 - increment,
                                  width=1, fill = "brown")

     my_sun_id = self.myCanvas.create_oval(10, 10, 50, 50, outline="black",width=1, fill="yellow")
     self.myCanvas.update()

     for count in range(20):
         '''sun set'''
         increment = 10*count
         self.myCanvas.coords(my_sun_id,
                              10 + increment, 10 + increment,
                              50 + increment, 50 + increment)
         self.myCanvas.update()
         sleep(.1)

     my_supernova_yellow = self.myCanvas.create_oval(200, 200, 240, 240, outline="black",width=1, fill="yellow")
     my_supernova_red = self.myCanvas.create_oval(200, 200, 240, 240, outline="black",width=1, fill="red")
     self.myCanvas.update()

     for count1 in range(30):
         '''sun explodes'''
         increment = count1*15
         self.myCanvas.coords(my_supernova_yellow,
                             200 - increment, 200 - increment,
                             240 + increment, 240 + increment)
         self.myCanvas.update()
         sleep(.05)

         self.myCanvas.coords(my_supernova_red,
                             200 - increment, 200 - increment,
                             240 + increment, 240 + increment)
         self.myCanvas.update()
         sleep(.05)
        

     for count in range(10):
         '''game over'''
         increment = count
         self.myCanvas.update()
         self.myCanvas.create_text(250, 120, text="GAME OVER",
                               width=350, fill="black", anchor="center",
                               justify="center", font=("Game Over", 100))
         self.myCanvas.create_text(250, 180, text="HIGH SCORE: 2020",
                               width=350, fill="black", anchor="center",
                               justify="center", font=("Game Over", 80))
         sleep(.5)

         self.myCanvas.update()
         self.myCanvas.create_text(250, 120, text="GAME OVER",
                               width=350, fill="yellow", anchor="center",
                               justify="center", font=("Game Over", 100))
         self.myCanvas.create_text(250, 180, text="HIGH SCORE: 2020",
                               width=350, fill="yellow", anchor="center",
                               justify="center", font=("Game Over", 80))
         sleep(.5)     

frame02 = MyFrame()
frame02.mainloop()

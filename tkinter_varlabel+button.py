from tkinter import *

class MyFrame(Frame):
  def __init__(self):
    Frame.__init__(self)
    self.master.geometry("400x400")
    self.master.title("My GUI")
    self.grid()
    
    self.button_click_here = Button(self, text = "Click Here",
      command = self.click_here_click )
    self.button_click_here.grid()

    self.my_text = StringVar()
    self.message = Label(self, textvariable = self.my_text)
    self.message.grid()

  def click_here_click(self):
   self.my_text.set("Fishy fishy floozey fish")
   
#     print("Fishy fishy fisy fish")
   
#       self.message = Label(self, text = "Hello World!")
#       self.message.grid()

frame01 = MyFrame()
frame01.mainloop()

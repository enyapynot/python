from tkinter import *

class MyFrame(Frame):
  """  CookMe """
  def __init__(self):
    Frame.__init__(self)
    self.master.geometry("400x400")
    self.master.title("My GUI")
    self.grid()
    self.button_click_here = Button(self, text = "Click Here",
      command = self.click_here_click )

#       self.button_click_here = Button(self, text = "click on dis ere ting",
#         command = self.click_here_click)

    self.button_click_here.grid()



  def click_here_click(self):
    """Fishes"""
    print("Fishy fishy fisy fish")
    

   
#       self.message = Label(self, text = "Hello World!")
#       self.message.grid()
print(MyFrame.__doc__)
print(MyFrame.click_here_click.__doc__)

frame01 = MyFrame()
frame01.mainloop()

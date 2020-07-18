from tkinter import *

class MyFrame(Frame):
  def __init__(self):
    Frame.__init__(self)
    
    self.master.geometry("400x400")
    self.master.title("My GUI")
    self.grid()

    self.prompt = Label(self, text = "Who dat den?")
    self.prompt.grid(column = 0, row = 0)

    self.input = Entry(self)
    self.input.grid(column = 1, row = 0)
    
    self.button_submit=Button(self,text="Hit Me!",
      command = self.zz)
#    self.button_submit.grid(columnspan = 2)
    self.button_submit.grid(columnspan = 2, pady = 10)

    self.my_text = StringVar()
    self.message = Label(self, textvariable = self.my_text)
    self.message.grid(columnspan = 2)

  def zz(self):
    output_message = "Hurrow " + self.input.get()
    self.my_text.set(output_message)


frame01 = MyFrame()
frame01.mainloop()

#  def submit_click(self):
#   self.my_text.set("Fishy fishy floozey fish")
#     print("Fishy fishy fisy fish")
#       self.message = Label(self, text = "Hello World!")
#       self.message.grid()

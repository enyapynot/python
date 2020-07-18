from tkinter import *

class MyFrame(Frame):
  def __init__(self):
    Frame.__init__(self)
    
    self.master.geometry("400x400")
    self.master.title("My GUI")
    self.grid()

    self.prompt = Label(self, text = "Who dat den?")
    self.prompt.grid()

    self.input = Entry(self)
    self.input.grid()
    
    self.button_submit=Button(self,text="Resistance be futile. You be assimilated",
      command = self.zz)
    self.button_submit.grid()
  
    self.my_text = StringVar()
    self.message = Label(self, textvariable = self.my_text)
    self.message.grid()

  def zz(self):
    output_message = "Hi " + self.input.get()
    self.my_text.set(output_message)


frame01 = MyFrame()
frame01.mainloop()

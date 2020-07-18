from tkinter import *

class MyFrame(Frame):
  def __init__(self):
    Frame.__init__(self)
    
    self.master.geometry("400x400")
    self.master.title("My GUI")
    self.grid()

    self.sample_label = Label(self, text = "Here's a bunch of text", font = "Courier 18")
    self.sample_label.grid(column = 0, row = 0)

    self.bold_on = IntVar()
    self.check_bold = Checkbutton(self, text = "Bold",
       variable = self.bold_on, command = self.set_font)
    self.check_bold.grid(row = 1, column = 0)

    self.underline_on = IntVar()
    self.check_underline = Checkbutton(self, text = "Underline",
      variable = self.underline_on, command = self.set_font)
    self.check_underline.grid(row = 1, column = 1)
        
    self.point_size = StringVar()
    self.point_size.set("10")
        
    self.eighteen_point = Radiobutton(self, text = "16 point",
      variable = self.point_size, value = "10",
      command = self.set_font)
    self.eighteen_point.grid(row = 2, column = 0)

        
    self.twenty_point = Radiobutton(self, text = "20 point",
      variable = self.point_size, value = "12",
      command = self.set_font)
    self.twenty_point.grid(row = 2, column = 1)


  def set_font(self):
    new_font = "Courier"

    if self.point_size.get() == "10":
      new_font = new_font + " 10"
    else:
      self.point_size.get() == "12"
      new_font = new_font + " 12"

    if self.bold_on.get() == 1:
      new_font = new_font + " bold"
    if self.underline_on.get() == 1:
      new_font = new_font + " underline"

    self.sample_label.config( font = new_font)
      
frame01 = MyFrame()
frame01.mainloop()

#     self.prompt.config(font = new_font)


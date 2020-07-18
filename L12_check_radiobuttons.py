from tkinter import *

class MyFrame(Frame):
  def __init__(self):
    Frame.__init__(self)
    
    self.master.geometry("600x200")
    self.master.title("My GUI")
    self.grid()

    self.top_label = Label(self, text = "Feed me", font = "Courier 12")
    self.top_label.grid(column = 0, row = 0)

    self.input = Entry(self)
    self.input.grid(column = 1, row = 0)
    
    self.button_submit=Button(self,text="*click*",command = self.submit_click)
    self.button_submit.grid(column = 2, row = 0)
    
    self.low_label = StringVar()
    self.low_label.set("Enter something above")
    self.new_output = Label(self, textvariable = self.low_label, font = "Courier 12 underline bold")
    self.new_output.grid(padx=20, column = 0, row = 3)
    
    
    self.bold_on = IntVar()
    self.check_bold = Checkbutton(self, text = "Bold",
      variable = self.bold_on,
      command = self.go_forit)
    self.check_bold.grid(row = 1, column = 0)

    self.underline_on = IntVar()
    
    self.check_underline = Checkbutton(self, text = "Underline",
      variable = self.underline_on,
      command = self.go_forit)
    self.check_underline.grid(row = 1, column = 1)
        
    self.point_size = StringVar()
    self.point_size.set("8")

    self.ten_point = Radiobutton(self, text = "10 point",
      variable = self.point_size, value = "10",
      command = self.go_forit)
    self.ten_point.grid(row = 2, column = 0)
    
    self.eighteen_point = Radiobutton(self, text = "12 point",
      variable = self.point_size, value = "12",
      command = self.go_forit)
    self.eighteen_point.grid(row = 2, column = 1)

    self.twenty_point = Radiobutton(self, text = "14 point",
      variable = self.point_size, value = "14",
      command = self.go_forit)
    self.twenty_point.grid(row = 2, column = 2)


  def go_forit(self):
    new_font = "Courier"

    if self.point_size.get() == "10":
      new_font = new_font + " 10"
    elif self.point_size.get() == "12":
      new_font = new_font + " 12"
    elif self.point_size.get() == "14":
      new_font = new_font + " 14"
      
    if self.bold_on.get() == 1:
      new_font = new_font + " bold"
    if self.underline_on.get() == 1:
      new_font = new_font + " underline"

    self.new_output.config( font = new_font)
    
  def submit_click(self):
    self.low_label.set(self.input.get())  #this sonofabitvh. 


      
frame01 = MyFrame()
frame01.mainloop()
#######################################################################

# Assignment
# Use your knowledge of the GUI widgets you learned about
# in this lesson to create a program that allows users to enter any text they want.
# When finished, users will click a Button to display the text in a Label. Then they'll
# be able to control the font style and size. Be sure to give your users the options to
# make their text bold and underlined and provide at least three different font sizes.

#Although your program isn't required to look this way, you might consider
#creating it to look like the following:


# Text Input field button

# Centred output text

# bold underline clickbuttons

# fontsize radiobuttons

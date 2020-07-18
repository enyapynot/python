class The_Time:
  """Create a class blueprint beginning with the all important constructor"""
  def __init__(self):
    self.secs=0
    self.mins=0
    self.hours=0
  def settime(self,hours,mins,secs):
    self.secs=secs
    self.mins=mins
    self.hours=hours
  def printtime(self):
    print("The time is")
    print("Hour: ", self.hours)
    print("Minute: ", self.mins)
    print("Second: ", self.secs)

Time1=The_Time()
Time1.settime(13,13,13)
Time1.printtime()



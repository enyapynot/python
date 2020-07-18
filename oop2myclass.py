class The_Time:
  """Create a class blueprint beginning with the all important constructor"""
  def __init__(self):
    """Constructor"""
    self.__secs=0
    self.__mins=0
    self.__hours=0
  def settime(self,hours,mins,secs):
    """ Set passwd variables, making up the time"""
    self.__secs=secs
    self.__mins=mins
    self.__hours=hours
  def printtime(self):
    """print the calculated time"""
    print("The time is ", self.__hours,":", self.__mins, ":", self.__secs )
# print("Hour: ", self.__hours)
# print("Minute: ", self.__mins)
# print("Second: ", self.__secs)

  def tick(self):
    """increment the time by 1"""
    self.__secs = self.__secs + 1
    if self.__secs > 59:
      self.__secs = 0
      self.__mins = self.__mins + 1
      if self.__mins > 59:
        self.__mins = 0
        self.__hours = self.__hours + 1
        if self.__hours > 23:
          self.__hours = 0

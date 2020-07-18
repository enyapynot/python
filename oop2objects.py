from oop2myclass import The_Time
import time
Time1=The_Time()
Hour=eval(input("Hour: "))
Minute=eval(input("Minute: "))
Second=eval(input("Seconds: "))
Reps=eval(input("Repetitions: "))

Time1.settime(Hour,Minute,Second)


for i in range(Reps):
  Time1.printtime()
  Time1.tick()
  time.sleep(1)

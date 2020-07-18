average=0
count=0
number=0
another="a"

while True:
  number=eval(input("May I have " + another+ " number: "))
  another="another"
  if number == -1:
    break
  count=count+1
  average=average+number
average = average/count
print("Your average is: ", average)

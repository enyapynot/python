average=0
count=0
number=0
go_away=0
the_answers=[]

for i in range(1, 99999):
    
    number=eval(input("May I have number (-999 to quit: "))
    if number == -999:
      break
    the_answers.append(number)
    average=average+number
    
average = average/i
print("You entered ", the_answers, ": ")
print("average is: ", average)

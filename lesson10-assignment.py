import shelve
studentname=""
grade=0
showgrade=""
Lineval="abc"
grade_file = shelve.open('/Users/enyap_ynot/python-course/letters.txt', 'c')

studentname = input("Please enter a student's name (or = to quit): ")


while studentname != '=' :

  grade = eval(input("Please enter score: "))
  studentname = input("Please enter a student's name (or = to quit): ")
  
  grade_file [ studentname ] = grade

print()
print("=========================")
print()

showgrade=input("Whose results would you like to view?: ")
while showgrade != "=":
  
  if (showgrade in grade_file):
    print(grade_file[showgrade])
  else:
    print("Nobody here by that name")
  showgrade=input("Whose results would you like to view?: ")
print()
print()

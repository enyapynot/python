results = {}
studentname=""
grade=""
showgrade=""
studentname = input("Please enter a student's name (or -999 to quit): ")
if studentname == "-999":
  exit()
gradename = ("Please enter " + studentname +"\'s score: ")
grade = input(gradename)

while (studentname != '-999' ):
  results [studentname] = grade
  studentname = input("Please enter a student's name (or -999 to quit): ")
  if studentname == "-999":
    break
  gradename = ("Please enter " + studentname +"\'s score: ")
  grade = input(gradename)

showgrade=input("Whose results would you like to view?")
print(results.get(showgrade, "Nobody here by that name"))
      

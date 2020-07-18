try:
  age = eval( input('Please enter your age: ') )
  ten_years = age + 10
  print ("In 10 years, you'll be", ten_years)
except NameError:
  print ("You must enter a number for your age")
except SyntaxError:
  print ("Now youu are just being silly")
print ("Have a nice day. Goodbye.")

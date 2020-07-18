words = {}
value = input("Please enter a word (or -999 to quit): ")
while (value != '-999'):
   if value in words:
      words [value] = words [value] + 1
   else:
       words [value] = 1

   value = input("Please enter a word (or -999 to quit): ")

for current_key in words.keys():
   print (current_key, '\t', words [current_key] )

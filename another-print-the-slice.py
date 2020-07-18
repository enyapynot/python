# Introduction to Python Programming
# Lesson 02 Assignment
# Sample Solution

# Get phrase from user
phrase = input("Please enter a phrase: ")

# Now get starting and ending positions
startNum = eval(input("Please enter the starting position: "))
endNum = eval(input("Please enter the ending position: "))

# Finally print out the slice
print (phrase[startNum:endNum+1])

# NOTE: Some may want to show the character at the last position
#   to the user.  In that case, the above print statement would be:
# print (phrase[len(phrase)-1:len(phrase)])

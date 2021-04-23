# Function to determine the inputted strng as either Uppercase or LowerCase , isUpper = true if all char in the string are uppercase, false if neither of one re 

def check(input):
  if(input.isUpper):
   print("String has all char cases in UpperCase")
  else:
    print("String lowercase")
    
string = input("Input string: ")
check(string)

#What if it is an number? That is an error in a production setting.

def double(input):
  '''double input'''
  print(input * 2)
  print("")
  return input*2
  
  
#call the functio
double

#type of the call
type(double)

def triple(input):
  '''triple input'''
  print(input * 3)
  print("")
  return input * 3

#Set the function to double and triple for later iteration
functions = [double, triple]

#Call double and triple in a for loop
for function in functions:
  print(function(6))

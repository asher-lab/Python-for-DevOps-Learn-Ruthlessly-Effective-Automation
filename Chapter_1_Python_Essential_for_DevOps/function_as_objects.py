def double(input):
  '''double input'''
  input * 2
  
#call the functio
double

#type of the call
type(double)

def triple(input):
  '''triple input'''
  input * 3
  
#Set the function to double and triple for later iteration
function = [double, triple]

#Call double and triple in a for loop
for function in function:
  print(function(6))

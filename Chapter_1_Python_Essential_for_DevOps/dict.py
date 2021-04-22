my_dict = {'Name':'Equinox'} # Create a dictionary 
type (my_dict) # Print the type of the variable
my_dict # Display the contents of the dict
my_dict['Name'] # Display the value of the Keys

# list out keys and values separately
key_list = list(my_dict.keys())
val_list = list(my_dict.values())

# print key with val 'Equinox'
position = val_list.index('Equinox')
print(key_list[position])

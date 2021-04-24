import os

# using split, basename, dirname

# printing the current working directory
cur_dir = os.getcwd()
print(cur_dir)

#os.path.split splits the leaf level of the path from the parent path.
#split function
print(os.path.split(cur_dir))

#returns the parent path
#dirname function
print(os.path.dirname(cur_dir))

#returns the leaf path      
#basename function
print(os.path.basename(cur_dir))

print()
#walking on directory tree
while os.path.basename(cur_dir):
    cur_dir = os.path.dirname(cur_dir)
    print(cur_dir)


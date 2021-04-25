import os

#Note:
#If the var_name does not exist create by: export var_name="my value"

def find_rc(rc_name=".examplerc"):
  # Check for Env variable
  var_name = "EXAMPLERC_DIR"
  print("Calling the function")
  #Check whether the environment variable exists in the current environment
  if var_name in os.environ:
    print("Pass if-condition of os.environ checking")
    #Use join to construct a path with the environment variable name.
    #This will look something like $EXAMPLERC_DIR/.examplerc.
    var_path = os.path.join(f"${var_name}", rc_name)
    #Expand the environment variable to insert its value into the path.
    config_path = os.path.expandvars(var_path)
    print(f"Checking {config_path}")
    #Check to see if the file exists.
    if os.path.exists(config_path):
        return config_path
        
    
    print("\nSearching on CWD")
    # Check the current working directory
    #Construct a path using the current working directory.
    config_path = os.path.join(os.getcwd(), rc_name)
    print(f"Checking {config_path}")
    if os.path.exists(config_path):
        return config_path
        
    print("\nSearching on Home DIR")    
    # Check user home directory
    #Use the expanduser function to get the path to the user’s home directory.
    home_dir = os.path.expanduser("~/")
    config_path = os.path.join(home_dir, rc_name)
    print(f"Checking {config_path}")
    if os.path.exists(config_path):
        return config_path
    
    print("\nSearching for the directory")    
    ## Check Directory of This File
    #Expand the relative path stored in file to an absolute path
    file_path = os.path.abspath(__file__)
    #Use dirname to get the path to the directory holding the current file
    parent_path = os.path.dirname(file_path)
    config_path = os.path.join(parent_path, rc_name)
    print(f"Checking {config_path}")
    if os.path.exists(config_path):
        return config_path
    print(f"File {rc_name} has not been found")


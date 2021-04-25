# do not run, this will not be interpreted. f format error, use manual method, or better use ipython

import os

print(f"Current Working Dir: {os.getcwd()}")

#changing cwd
os.chdir('/tmp')

print(f"Current Working Dir: {os.getcwd{}}")

print(f"Contents of the environ before changing: {os.environ.get('LOGLEVEL')}")

#changing the value of environ
os.environ['LOGLEVEL']='DEBUG'

print(f"Content of environ after changing: {os.environ.get('LOGLEVEL')}")
      
# get data of current user
os.getlogin()

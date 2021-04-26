# argparse sub flags

#!/usr/bin/env python

"""
Command line tool using argparse
"""

import argparse
def sail():
    ship_name="Titanic"
    print(f"{ship_name} is setting sail")

def list_ships():
    ships = ['John K', 'Yankee Clippers', 'Pequod']
    print(f"Ships: {','.join(ships)}")
    
def greet(greeting, name):
    message = f'{greeting} {name}'
    print(message)


#arguments - main body
if __name__ == '__main__':

    #define description
    parser = argparse.ArgumentParser(description='Maritime control')
    
    #define twice flag
    parser.add_argument('--twice', '-t', help='Do it twice', action='store_true')
    
    #create a subparse object to hold the subparsers.
    #The dest is the name of the attribute used to choose a subparser.
    subparsers = parser.add_subparsers(dest='func')
   
    #add subparser for ships
    ship_parser = subparsers.add_parser('ships', help='Ship related commands')
    
    #add command to ships subparser. The choices paramters
    #gives a list of possible choice for the command
    ship_parser.add_argument('command', choices=['list', 'sail'])
    
    #add subparser for sailors
    sailor_parser = subparsers.add_parser('sailors', help='Talk to a sailor')
    
    #add a required positional argument to the sailors subparse
    sailor_parser.add_argument('name', help='Sailors name')
    sailor_parser.add_argument('--greeting', '-g', help='Greeting', default='Ahoy there')
    
args = parser.parse_args()

#check with subparse is used by checking the func value.
if args.func == 'sailors':
    greet(args.greeting, args.name)
elif args.command == 'list':
    list_ships()
else:
    sail()
    

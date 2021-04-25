#!/usr/bin/env python3
"""
Command-line tool using argparse
"""
import argparse

if __name__ == '__main__':
    #Create the parser object, with its documentation message.
    parser = argparse.ArgumentParser(description='Echo your input')
    #Add a position-based command with its help message.
    parser.add_argument('message', help='Message to echo')
    
    parser.add_argument('--twice', '-t', ##Add an optional argument.
                        help='Do it twice', 
                        action='store_true') #Store the optional argument as a boolean value
  
    #Use the parser to parse the arguments.
    args = parser.parse_args()
    #Access the argument values by name. The optional argument’s name has the -- removed.
    print(args.message)
    if args.twice:
        print(args.message)
        
# ./argparse-echo.py  hello --twice
#./argparse-echo.py -h or --help

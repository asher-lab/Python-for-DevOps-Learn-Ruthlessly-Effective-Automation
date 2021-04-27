#/usr/bin/env python3

"""
Simple fire example
"""

import fire
def greet(greetings='Hiya!', name = 'Tammy'):
    print(f"{greetings} {name}")
    
if __name__ == '__main__':
    fire.Fire(greet)

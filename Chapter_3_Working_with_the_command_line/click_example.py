#!/usr/bin/env python3

"""
Command line tool
Argparse
"""

import click

@click.group()

def cli():
    pass
    
@click.group(help='Ship related commands')
def ships():
    pass

cli.add_command(ships)

@ships.command(help='Your Ship')
def sail():
    ship_name='Your Ship'
    print(f"{ship_name} is setting sail")
    
@ships.command(help='List all of the ships')
def list_ships():
    ships=['John B', 'Yankee Clipper', 'Pequod']
    print(f"Ships: {','.join(ships)}")
    
@cli.command(help='Talk to a sailor')
@click.option('--greeting', default='Ahoy there', help='Greeting for sailor')
@click.argument('name')

def sailors(greeting, name):
    message=f'{greeting}{name}'
    print(message)
    
if __name__=='__main__':
    cli()

import click

@click.command()
@click.option('--greeting', default='Hiya',help='How do you want to greet?')
@click.option('--name', default='Tammy',help='Who do you wan to greet?')

#define the greet function
def greet (greeting,name):
    print(f"{greeting} {name}")
    
if __name__=='__main__':
    greet()
  
  
#usage
#./click.py --greeting Hola --name Erik!

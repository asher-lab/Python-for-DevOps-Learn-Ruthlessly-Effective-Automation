def f1(func):
	def wrapper():
		print("Started")
		func()
		print("Ended")
		
	return wrapper
	
	
"""
Instead of using this 
f(f1)
"""

@f1
def f():
	print("Hello")

f()

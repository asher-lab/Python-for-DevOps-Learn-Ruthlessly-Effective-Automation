def count():
  n = 0
  while True:
    n += 1
    yield n

    
counter = count()
next(counter)
#1
#2
.
.
.
# until counter is called

def fibgen():
  first = 0
  last = 1
  while True:
    first, last = last, first + last
    yield first
    
f = fibgen()
next(f)

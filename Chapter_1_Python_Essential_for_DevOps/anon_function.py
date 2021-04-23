items = [[0, 'a', 2], [5, 'b', 0], [2, 'c', 1]]
print(sorted(items))

def second(item):
  ''' return second entry'''
  return item[1]

print(sorted(items, key=second))

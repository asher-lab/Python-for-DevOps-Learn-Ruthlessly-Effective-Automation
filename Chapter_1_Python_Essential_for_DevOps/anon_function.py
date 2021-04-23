items = [[0, 'a', 2], [5, 'b', 0], [2, 'c', 1]]
print(sorted(items))

def second(item):
  ''' return second entry'''
  return item[1]

print(sorted(items, key=second))


# Display contens of items
print("Contents of Items")
print(items)
#Using lambda keyword
print(sorted(items, key=lambda item: item[1]))
print(sorted(items, key=lambda item: item[2]))
print(sorted(items, key=lambda item: item[0]))

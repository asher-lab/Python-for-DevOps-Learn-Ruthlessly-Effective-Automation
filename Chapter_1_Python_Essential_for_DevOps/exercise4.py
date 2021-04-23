#Write a generator that alternates between returning Even and Odd
#Using for loops to iterate through the lists

even_num = []
for i in range(0, 100):
	even_num.append(i+i)
    
odd_num = []


for i in range(0,100, 2):
	x = odd_num.append(i-1)
    
print(even_num)
print(odd_num)

#Using list comprehension
print()
even_numbers = [i for i in range (0,100,2)]
odd_numbers = [i for i in range (1,100,2)]
print(even_numbers)
print(odd_numbers)

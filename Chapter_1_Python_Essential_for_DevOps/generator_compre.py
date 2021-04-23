list_o_nums = [x for x in range(100)]
gen_o_nums = (x for x in range (100))

print(list_o_nums)
print(gen_o_nums)

#import sys module
import sys

#get the size of the variab;es
print(sys.getsizeof(list_o_nums))
print(sys.getsizeof(gen_o_nums))

#Iterating the value of the generator
print()
for i in range(100):
  print(next(gen_o_nums))

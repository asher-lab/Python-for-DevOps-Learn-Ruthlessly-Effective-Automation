cc_list = '''Ezra Koenig <ekoenig@vpwk.com>,Rostam Batmanglij <rostam@vpwk.com>,Chris Tomson <ctomson@vpwk.com>,Bobbi Baio <bbaio@vpwk.com>'''
 
# Check if Rostam is in cc_list
print('Rostam' in cc_list)



#import re module
import re
print(re.search(r'Rostam', cc_list))

#if condition
if (re.search(r'Rostam', cc_list)):
  print("Found Rostam in cc_list") 
  
# Find
print(re.search(r'[R,B]obb[i,y]', cc_list))
print(re.search(r'Chr[a-z][a-z]', cc_list))
print(re.search(r'[A-Za-z]+', cc_list))
print(re.search(r'[A-Za-z]{6}', cc_list))
print(re.search(r'[A-Za-z]+@[a-z]+\.[a-z]+', cc_list))

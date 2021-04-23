cc_list = '''Ezra Koenig <ekoenig@vpwk.com>,Rostam Batmanglij <rostam@vpwk.com>,Chris Tomson <ctomson@vpwk.com>,Bobbi Baio <bbaio@vpwk.com>'''
 
# Check if Rostam is in cc_list
print('Rostam' in cc_list)



#import re module
print(re.search(r'Rostam', cc_list))

#if condition
if (re.search(r'Rostam', cc_list)):
  print("Found Rostam in cc_list) 

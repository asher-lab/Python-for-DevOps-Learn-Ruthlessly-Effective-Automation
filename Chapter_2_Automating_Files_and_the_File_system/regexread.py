#import re module
import re
line = '127.0.0.1 - rj [13/Nov/2019:14:43:30] "GET HTTP/1.0" 200'
print(re.search(r'(?P<IP>\d+\.\d+\.\d+\.\d+)', line))
m = re.search(r'(?P<IP>\d+\.\d+\.\d+\.\d+)', line)
print(m.group('IP'))

#to make things easier
r = r'\[(?P<Time>\d\d/\w{3}/\d{4}:\d{2}:\d{2}:\d{2})\]'
m = re.search(r, line)
print(m.group('Time'))

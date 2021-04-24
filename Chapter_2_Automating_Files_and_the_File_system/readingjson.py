import pathlib
path = pathlib.Path("service-policy.json")
print(path.read_text())


#with open readlines
with open('service-policy.json', 'r') as opened_file:
	policy = opened_file.readlines()
print(policy)

print()
#importing json module
import json
with open('service-policy.json', 'r') as opened_file:
	policy = json.load(opened_file)	
print(policy)

print()
#using pprint
from pprint import pprint
pprint(policy)

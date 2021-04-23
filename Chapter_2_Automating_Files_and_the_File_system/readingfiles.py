file_path = "text.txt"
open_file = open(file_path, 'r')
text = open_file.read()
print(len(text))

print(text[2])
print(open_file)
open_file.close()

#Using readlines
open_file = open(file_path, 'r')
text = open_file.readlines()
print(len(text))
print(text[2])
open_file.close()

print()
#using 'with' to open and close the file
with open(file_path, 'r') as open_file:
    text = open_file.readlines()
print (text[2])
#file will close automatically
#to validate type
if(open_file.closed):
    print("The file is closed")

#reading file in binary format
file_path = 'example.pdf'
with open(file_path, 'rb') as open_file:
    btext=open_file.read()
print(f"Index number 3 of list: {btext[3]}")
print(f"Contens of btext: {btext}")
print(f"Length of btext: {len(btext)}")
print(f"{btext[:25]}")


print()
#writing Files using w mode
text = '''export STAGE= PROD
export TABLE_ID=token-storage-1234'''

with open(".envrc", 'w') as opened_file:
    opened_file.write(text)
with open(".envrc", 'r') as opened_file:
    env = opened_file.readlines()
    
print(env)

print()
#Reading textfiles using pathlib
#importing the pathlib module
import pathlib
path = pathlib.Path("text.txt")
path.read_text()
#Reading binary files
path.read_bytes()
#overwriting a file
path.write_text("OverRIde")

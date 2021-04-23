file_path = "text.txt"
open_file = open(file_path, 'r')
text = open_file.read()
print(len(text))

print(text[56])
print(open_file)
open_file.close()

#Using readlines
open_file = open(file_path, 'r')
text = open_file.readlines()
print(len(text))
print(text[56])
open_file.close()

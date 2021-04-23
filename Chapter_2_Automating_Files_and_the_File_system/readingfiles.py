file_path = "text.txt"
open_file = open(filepath, 'r')
text = open_file.read()
print(len(text))

print(text[56])
print(open_file)
open_file.close

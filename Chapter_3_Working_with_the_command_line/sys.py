import sys

# print byteorder of current working architecture
print(f"Byte order: {sys.byteorder}")

print(f"Size of Python objects: {sys.getsizeof(1)}")

print(f"Platform: {sys.platform}")

# Limiting code to run on specific version

# If less than 3 
if sys.version_info.major < 3:
    print("You need to update Python")
elif sys.version_info.minor <= 7:
    print("You are not running the latest version of Python")
else:
    print("Your Python version is compatible")

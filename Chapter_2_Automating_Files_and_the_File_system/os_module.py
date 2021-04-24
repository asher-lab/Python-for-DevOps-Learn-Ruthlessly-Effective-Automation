import os

#List directory
os.listdir('.')

# renaming a file or a directory
os.rename('_crud_handler', 'crud_handler')

# change the permission of a directory
os.chmod('my_script.py', 0o777)

#create a dir
os.mkdir('/tmp/holding')

#Recursively create a directory path.
os.makedirs('/Users/kbehrman/tmp/scripts/devops')

#Delete a file.
os.remove('my_script.py')

#Delete a single diretory
os.rmdir('/tmp/holding')

#Delete a tree of directories, starting with the leaf directory up to the tree.
# This operation stops with the first nonempty directory.
os.removedirs('/Users/kbehrman/tmp/scripts/devops')

#Get stats about the file or directory/ These stats include <st_mode, the file type
# and permissions, and st_atime, the time and item was last accessed.
os.stat('crud_handler')

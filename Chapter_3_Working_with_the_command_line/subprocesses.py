# subprocess
# spawning a process of an application
import subprocess
import sys

# hello world command
helloWorld = subprocess.run([sys.executable, "-c", "print('Hello World')"])

# this code translates to > /usr/local/bin/python -c "print('Hello World')"
# ls command
ls = subprocess.check_output(["ls", "-l", "/"])

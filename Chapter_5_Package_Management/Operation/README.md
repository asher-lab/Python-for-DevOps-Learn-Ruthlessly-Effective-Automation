# Usage: main

```
Importing modules can be done:
import sum
sum.sum()

- 
Importing module can also be done: 
from sum import sum 
sum() 
```

# main_1

```
mkdir func
mv subt.py func/subt.py
mv sum.py func/sum.py
mv div.py func/div.py
mv mult.py func/mult.py
cd func
touch __init__.py
cd ..
python3 main_1.py

```
## Adding imports to __init__.py
```
from .sum import sum
from .div import div
from .mult import mult
from .subt import subt
```


## Create main_2 with these contents (same directory as main and main_1):

from .sum import sum
from .div import div
from .mult import mult
from .subt import subt

# setuptools setup.py

```create setup.py

then add following code:


from setuptools import setup, find_packages
setup(
name="hello-world",
version="0.0.1",
author="Example Author",
author_email="author@example.com",
url="example.com",
description="A hello-world example package",
packages=find_packages(),
classifiers=[
"Programming Language :: Python :: 3",
"License :: OSI Approved :: MIT License",
"Operating System :: OS Independent",
],
)
```

```
python3 setup.py sdist
cd dist
pip3 install hello-world-0.0.1.tar.gz
```
reference: https://pythonhosted.org/an_example_pypi_project/setuptools.html<br>
https://docs.python.org/3/distutils/sourcedist.html

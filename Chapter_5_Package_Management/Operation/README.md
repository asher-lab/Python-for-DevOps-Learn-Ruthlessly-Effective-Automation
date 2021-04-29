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
## Adding imports to init.py
```
from .sum import sum
from .div import div
from .mult import mult
from .subt import subt
```

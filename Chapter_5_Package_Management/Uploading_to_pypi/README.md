# Uploading to PyPi (test)

## install twine = tool for registering and uploading packages
## install twine = ```pip3 install setuptools twine```
## https://twine.readthedocs.io/en/latest/
## install keyrings = ```pip3 install --upgrade keyrings.alt ```

### Change email and repository url also author and name
```
setup(
name="pineng",
version="0.0.1",
author="AsherAuthor",
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

### Run:
```
# rm all dist and egg info folders
python3 setup.py sdist
twine upload -r testpypi dist/* --verbose
```

Example output:
```
Uploading pineng-0.0.1.tar.gz
100%|██████████████████████████████████████| 4.13k/4.13k [00:01<00:00, 3.41kB/s]

View at:
https://test.pypi.org/project/pineng/0.0.1/

Install :
python3 -m pip install --index-url
https://test.pypi.org/simple/ hello-world

Here to be exact:
pip install -i https://test.pypi.org/simple/ pineng==0.0.1

```

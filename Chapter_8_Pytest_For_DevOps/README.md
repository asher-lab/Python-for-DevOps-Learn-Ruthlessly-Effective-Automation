## Testing with PyTest
```
python3 -m venv testing
source testing/bin/activate
#create a file 'test_basic.py with the following contents:
def test_simple():
  assert True
def test_fail():
  assert False
```
```
pytest
```
important: pytest is always running in convention which: test_

[https://medium.com/testcult/intro-to-test-framework-pytest-5b1ce4d011ae]

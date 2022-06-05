<h1 align="center"><b>Pytest python testing</b></h1>

The [pytest](https://pytest.org/) framework makes it easy to write small, readable tests, and can scale to support complex functional testing for applications and libraries.

This repo helps document my progress in learning the ins and outs of Pytest

## Why Pytest
### 1. Less Boilerplate
Most functional tests follow the Arrange-Act-Assert model:
1. <b>Arrange</b>, or set up, the conditions for the test
2. <b>Act</b> by calling some function or method
3. <b>Assert</b> that some end condition is true

Pytest simplifies the test workflow by allowing you to use Python’s assert keyword directly:
```python
# test_with_pytest.py

def test_always_passes():
    assert True

def test_always_fails():
    assert False
```
To run the tests:
```bash
$ pytest
============================= test session starts ==============================
platform linux -- Python 3.10.4, pytest-7.1.2, pluggy-1.0.0
rootdir: /home/daniel/Desktop/learn/python_testing
collected 2 items                                                              

test_with_pytest.py .F                                                   [100%]

=================================== FAILURES ===================================
_______________________________ test_always_fail _______________________________

    def test_always_fail():
>       assert(False)
E       assert False

test_with_pytest.py:5: AssertionError
=========================== short test summary info ============================
FAILED test_with_pytest.py::test_always_fail - assert False
========================= 1 failed, 1 passed in 0.04s ==========================
```
The tests result report shows:
1. The system state, including which versions of Python, pytest, and any plugins you have installed
2. The rootdir, or the directory to search under for configuration and tests
3. The number of tests the runner discovered

The output then indicates the status of each test using a syntax similar to unittest:

- A dot (.) means that the test passed.
- An F means that the test has failed.
- An E means that the test raised an unexpected exception.

For tests that fail, the report gives a detailed breakdown of the failure. In the example above, the test failed because assert False always fails. Finally, the report gives an overall status report of the test suite.

## <b>License</b>
[![license](https://img.shields.io/github/license/mashape/apistatus.svg?style=for-the-badge)](LICENSE)
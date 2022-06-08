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

### 2. State and dependency management
Pytest enables explicit dependency declarations by use of <b>fixtures</b>. Fixtures are functions that create data or test doubles or initialize some system state for the test suite. Any test that wants to use a fixture must explicitly accept it as an argument, so dependencies are always stated upfront.Fixtures can also make use of other fixtures, again by declaring them explicitly as dependencies.

### 3. Test filtering
As your test suite grows, you may find that you want to run just a few tests on a feature and save the full suite for later. pytest provides a few ways of doing this:
- <b>Name-based filtering</b> : You can limit pytest to running only those tests whose fully qualified names match a particular expression. You can do this with the -k parameter.
- <b>Directory scoping</b> : By default, pytest will run only those tests that are in or under the current directory.
- <b>Test categorization</b> : pytest can include or exclude tests from particular categories that you define. You can do this with the -m parameter.

Test categorization in particular is a subtly powerful tool. pytest enables you to create marks, or custom labels, for any test you like. A test may have multiple labels, and you can use them for granular control over which tests to run. Later in this tutorial, you’ll see an example of how pytest marks work and learn how to make use of them in a large test suite.

### 4. Test Parameterization
When you’re testing functions that process data or perform generic transformations, you’ll find yourself writing many similar tests. They may differ only in the input or output of the code being tested. This requires duplicating test code, and doing so can sometimes obscure the behavior you’re trying to test. pytest offers a way of collecting several tests into one in which each test can pass or fail independently.

### 5. Plugin-Based Architecture
pytest users have developed a rich ecosystem of helpful plugins due to its openness to customization


#### **Fixtures:Managing State and Dependencies**
pytest fixtures are a way of providing data, test doubles, or state setup to your tests. Fixtures are functions that can return a wide range of values. Each test that depends on a fixture must explicitly accept that fixture as an argument.
##### **When to create fixtures**
If you find yourself writing several tests that all make use of the same underlying test data, then a fixture may be in your future. You can put the repeated data into a single function decorated with @pytest.fixture to indicate that the function is a pytest fixture.You can then use the fixture by adding it as an argument to your tests. Its value will be the return value of the fixture function.
#### **Fixtures at scale**
You can move fixtures from test modules into more general fixture-related modules. That way, you can import them back into any test modules that need them. This is a good approach when you find yourself using a fixture repeatedly throughout your project.
pytest looks for `conftest.py` modules throughout the directory structure. Each conftest.py provides configuration for the file tree pytest finds it in. You can use any fixtures that are defined in a particular `conftest.py` throughout the file’s parent directory and in any subdirectories. This is a great place to put your most widely used fixtures.

#### **Marks:Categorizing Tests**
Pytest enables you to define categories for your tests and provide options for including or excluding categories when you run your suite. One can mark a test with any number of categories
Marking tests is useful for categorizing tests by subsystems or dependencies eg:
`@pytest.mark.database_access` for tests that require database access. To run all tests *except* those that require database access you can use `pytest -m "not database_access"`

pytest provides a few marks out of the box:

- **skip** skips a test unconditionally.
- **skipif** skips a test if the expression passed to it evaluates to True.
- **xfail** indicates that a test is expected to fail, so if the test does fail, the overall suite can still result in a passing status.
- **parametrize** creates multiple variants of a test with different values as arguments.

You can see a list of all the marks pytest knows about by running `pytest --markers`

#### **Parametrization: Combining Tests**
Although fixtures can be used to reduce code dublication by extracting common dependencies they aren't quite useful whenn you have several tests with slightly different inputs and expected outputs. In such cases you can parametrize a single test definition and pytest will create variants of the test for you with the parameters you specify.

#### **Durations Reports: Fighting Slow Tests**
Pytest can automatically record test durations for you and report the top offenders.Use the --durations option to the pytest command to include a duration report in your test results. --durations expects an integer value n and will report the slowest n number of tests. The output will follow your test results:
```bash
$ pytest --durations=5 -vv
============================= test session starts ==============================
platform linux -- Python 3.10.4, pytest-7.1.2, pluggy-1.0.0 -- /home/daniel/.local/share/virtualenvs/python_testing-TXRbz4By/bin/python
cachedir: .pytest_cache
rootdir: /home/daniel/Desktop/learn/python_testing, configfile: pytest.ini
collected 15 items                                                             

test_with_pytest.py::test_always_pass PASSED                             [  6%]
test_with_pytest.py::test_always_fail XFAIL                              [ 13%]
test_with_pytest.py::test_capitalize PASSED                              [ 20%]
test_with_pytest.py::test_reversed PASSED                                [ 26%]
test_with_pytest.py::test_some_primes PASSED                             [ 33%]
test_with_pytest.py::test_format_data_for_display PASSED                 [ 40%]
test_with_pytest.py::test_format_data_for_excel PASSED                   [ 46%]
test_with_pytest.py::test_get_my_ip PASSED                               [ 53%]
test_with_pytest.py::test_is_palindrome[-True] PASSED                    [ 60%]
test_with_pytest.py::test_is_palindrome[a-True] PASSED                   [ 66%]
test_with_pytest.py::test_is_palindrome[Bob-True] PASSED                 [ 73%]
test_with_pytest.py::test_is_palindrome[Never odd or even-True] PASSED   [ 80%]
test_with_pytest.py::test_is_palindrome[Do geese see God?-True] PASSED   [ 86%]
test_with_pytest.py::test_is_palindrome[abc-False] PASSED                [ 93%]
test_with_pytest.py::test_is_palindrome[abab-False] PASSED               [100%]

============================= slowest 5 durations ==============================
0.01s call     test_with_pytest.py::test_get_my_ip
0.00s setup    test_with_pytest.py::test_is_palindrome[Never odd or even-True]
0.00s setup    test_with_pytest.py::test_is_palindrome[-True]
0.00s setup    test_with_pytest.py::test_some_primes
0.00s setup    test_with_pytest.py::test_get_my_ip
======================== 14 passed, 1 xfailed in 0.12s =========================
```

## <b>References</b>
1. https://realpython.com/pytest-python-testing/
2. https://testdriven.io/blog/testing-python/

## <b>License</b>
[![license](https://img.shields.io/github/license/mashape/apistatus.svg?style=for-the-badge)](LICENSE)
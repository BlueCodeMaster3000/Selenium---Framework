# Any pytest file should start with test_ or end with _test
# pytest method names should always start with test
# any code should be wrapped in method only
# you can run all tests that follow those rules via console with py.test and with py.test -v for more info
# you can also add -s to previous command to see program output
# Method name is important!!!
# you can run specific file with py.test <filename>
import pytest


# pytest module for marking(tagging) specific tests that can be later run with -m <mark>
@pytest.mark.smoke
@pytest.mark.skip # marking test with <skip> makes pytest skip this test
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi", "Test failed because strings do not match"


# -k added to py.test command searches for keyword in method name like "-k CreditCard"
def test_secondCreditCard():
    a = 4
    b = 6
    assert a+2 == 6, "Addition does not match"


@pytest.mark.xfail # marking test with <xfail> makes pytest run this test but not report it
def test_thirdProgram():
    msg = "Hi"
    assert msg == "Hello", "Test failed because strings do not match"


def test_fixtureDemo(setup):
    print("I will execute steps in fixtureDemo method")
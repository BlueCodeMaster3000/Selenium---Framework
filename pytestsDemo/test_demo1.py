# Any pytest file should start with test_ or end with _test
# pytest method names should always start with test
# any code should be wrapped in method only
# you can run all tests that follow those rules via console with py.test and with py.test -v for more info
# you can also add -s to previous command to see program output
# Method name is important!!!
# you can run specific file with py.test <filename>
# to run pytest html report you add argument --html=report.html
import pytest


# pytest module for marking specific tests
@pytest.mark.smoke
def test_firstProgram():
    print("Hello")


# -k added to py.test command searches for keyword in method name like "-k CreditCard"
def test_secondGreetCreditCard():
    print("Good morning")


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])
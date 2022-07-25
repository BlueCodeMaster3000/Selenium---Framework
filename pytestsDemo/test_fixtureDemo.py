# pytest.fixture is a prerequisite that can be executed before executing any test
import pytest


# automatically applies fixture present to all methods in this class
@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo(self):
        print("I will execute steps in fixtureDemo method")

    def test_fixtureDemo2(self):
        print("I will execute steps in fixtureDemo method")

    def test_fixtureDemo3(self):
        print("I will execute steps in fixtureDemo method")

    def test_fixtureDemo4(self):
        print("I will execute steps in fixtureDemo method")
# conftest file applies fixture to all tests

import pytest


# pytest.fixture is a prerequisite that can be executed before executing any test
@pytest.fixture(scope="class") # scope = "class makes fixture work on class and not specificly for evey method in class
def setup():
    print("I will be executed first")
    yield # yield keyword makes everything in this function past it to be executed after test
    print("I will be executed last")


@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Kacper", "Biegajlo", 'rahulshettyacademy.com']


# datadrivern and parameterization can be done with return statements in tuple format
@pytest.fixture(params=[("chrome", "Kacper", "Biegajlo"), ("firefox", "Michal"), ("PogSafari", "LMAO")])
def crossBrowser(request):
    return request.param
import os
import pytest


def pytest_addoption(parser):
    parser.addoption("--input1", action="store", default='12',help='hello')
    parser.addoption("--input2", action="store", default='122',help='hello1')


@pytest.fixture
def input1(request):
    return request.config.getoption("--input1")


@pytest.fixture
def input2(request):
    return request.config.getoption("--input2")
# @pytest.fixture(scope='abc')
# def pytest_configure(config):
#     os.environ["input1"]=config.getoption('input1')

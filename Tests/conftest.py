import pytest


def pytest_addoption(parser):
    parser.addoption("--platformname", action="store", default='Android', help='platformname')
    parser.addoption("--udid", action="store", default='122', help='udid')
    parser.addoption("--platformversion", action="store", default='7.0', help='version')
    parser.addoption("--appversion", action="store", default='3.5.6', help='app_version')


@pytest.fixture
def platformname(request):
    return request.config.getoption("--platformname")


@pytest.fixture
def udid(request):
    return request.config.getoption("--udid")


@pytest.fixture
def platformversion(request):
    return request.config.getoption("--platformversion")

@pytest.fixture
def appversion(request):
    return request.config.getoption("--appversion")
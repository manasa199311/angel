import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="run slow tests"
    )


@pytest.fixture(scope="class")
def invokeDriver(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(7)
    yield driver
    driver.quit()

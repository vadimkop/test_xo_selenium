import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or safari")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
#        options.add_argument("--headless")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "safari":
        print("\nstart safari browser for test..")
        browser = webdriver.Safari()
    else:
        raise pytest.UsageError("--browser_name should be chrome or safari")
    yield browser
    print("\nquit browser..")
    browser.quit()
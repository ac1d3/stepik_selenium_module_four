import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en",
                     help="Choose website language")



@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope="function")
def language(request):
    valid_language_codes = ["ar", "ca", "cs", "da", "de", "en-gb", "el", "es", "fi", "fr", "it", "ko", "nl", "pl", "pt",
                            "pt-br", "ro", "ru", "sk", "uk", "zh-cn"]
    language_option = request.config.getoption("language")
    if language_option in valid_language_codes:
        print(f"\nstart test with {language_option} language..")
        language = language_option
    else:
        raise pytest.UsageError("please, enter valid language code for --language option, e.g. 'de' - Deutsch")
    yield language

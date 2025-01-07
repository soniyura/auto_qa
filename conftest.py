import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument("--start-maximized")  # Открыть окно браузера на полный экран
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


"""
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield driver
    driver.quit()
"""
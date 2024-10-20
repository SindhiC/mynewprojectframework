from pydoc import browse

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(params=["chrome"], scope='class')
def setup(request):
    global web_driver
    if request.param == "chrome":
        options = Options()
        options.add_argument("--disable-notifications")
        options.add_argument("--incognito")
        web_driver = webdriver.Chrome(options=options)
    if request.param == "firefox":
        options = Options()
        options.add_argument("--disable-notifications")
        options.add_argument("--incognito")
        web_driver = webdriver.Firefox(options=options)
    request.cls.driver = web_driver
    yield
    web_driver.close()
"""
#It is hook for Adding Env info to the HTML report
def pytest_configure(config):
    config.metadata['Project Name'] = 'nopCommerce'
    config.metadata['Module Name'] = 'Customer'
    config.metadata['Tester Name'] = 'Sindhiya'

#It is a hook for delete/modify the Env info to the HTML report
def pytest_metadata(metadada):
    metadada.pop("JAVA_HOME", None)
    metadada.pop("Plugins", None)
"""
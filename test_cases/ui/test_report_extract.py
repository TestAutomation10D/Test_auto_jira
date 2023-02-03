import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_report_ext(driver):

    driver.get("https://www.google.com/")
    time.sleep(4)
    assert 1 == 1

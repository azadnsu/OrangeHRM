from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest


def test_setup():
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()

def test_login():
    driver.get("https://opensource-demo.orangehrmlive.com/")

    driver.find_element_by_id('txtUsername').clear()
    driver.find_element_by_id('txtUsername').send_keys('admin')

    driver.find_element_by_id('txtPassword').clear()
    driver.find_element_by_id('txtPassword').send_keys('admin123')

    driver.find_element_by_id('btnLogin').click()

    assert driver.title == 'OrangeHRM'

def test_teardown():
    driver.close()
    driver.quit()

    print("Test completed!")
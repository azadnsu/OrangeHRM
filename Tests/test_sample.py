from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest


class TestSample():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print("Test completed!")


    def test_valid_login(self,test_setup):
        driver.get("https://opensource-demo.orangehrmlive.com/")

        driver.find_element_by_id('txtUsername').clear()
        driver.find_element_by_id('txtUsername').send_keys('admin')

        driver.find_element_by_id('txtPassword').clear()
        driver.find_element_by_id('txtPassword').send_keys('admin123')

        driver.find_element_by_id('btnLogin').click()

        assert driver.title == 'OrangeHRM'

    #def test_teardown():
    #    driver.close()
    #    driver.quit()
    #    print("Test completed!")
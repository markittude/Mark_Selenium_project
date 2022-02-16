import unittest
from selenium import webdriver
from locator import *
import page
import configparser
import os

config = configparser.ConfigParser()
current_path = os.path.abspath(__file__)
inifile = os.path.abspath(os.path.dirname(current_path) + "\config.ini")
config.read(inifile)
test_link = str(config.get('Web_driver', 'link'))



class Barco_page(unittest.TestCase):


    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path=os.path.abspath(os.path.dirname(current_path) + "\src\chromedriver.exe"))
        self.driver.get(test_link)

    def test_min_input(self):
        main_page = page.MainPage(self.driver)
        main_page.click(MainPageLocators.close_cookie, True)
        data = main_page.input_text('1234',MainPageLocators.min_char_warning)
        self.assertEqual(str(data),str('Minimum 6 characters required'), "最少字元測試回傳不一致")

    def test_symbol_input(self):
        main_page = page.MainPage(self.driver)
        main_page.click(MainPageLocators.close_cookie, True)
        data = main_page.input_text('!@#$!$@3',MainPageLocators.check_agreement_valid)
        self.assertEqual(str(data),str('Please enter a valid serial number'), "Valid number 測試回傳不一致")

    def test_invalid_input(self):
        main_page = page.MainPage(self.driver)
        main_page.click(MainPageLocators.close_cookie, True)
        data = main_page.input_text('',MainPageLocators.check_specify_valid)
        self.assertEqual(str(data),str('Please specify a serial number'), "回傳不一致")

    def test_check_terms_conditions(self):
        main_page = page.MainPage(self.driver)
        main_page.click(MainPageLocators.close_cookie, True)
        main_page.click(MainPageLocators.terms_agreement, False)
        assert main_page.check_title(1)


    def tearDown(self) -> None:
        self.driver.close()


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Barco_page('test_min_input'))
    suite.addTest(Barco_page('test_symbol_input'))
    suite.addTest(Barco_page('test_invalid_input'))
    suite.addTest(Barco_page('test_check_terms_conditions'))
    results = unittest.TextTestRunner(verbosity=2).run(suite)

    print("results: %s" % results)
    print("results.wasSuccessful: %s" % results.wasSuccessful())
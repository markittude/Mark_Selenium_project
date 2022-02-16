from locator import *


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):

    def click(self, element, allowFail=True):
        """ Click on the requested element \n
            Args: \n
                element： [required] Elememnt name
                allowFail ： [optional] True if the result will not affect the test
        """
        if allowFail:
            try:
                self.driver.find_element(*element).click()
            except Exception:
                pass
        else:
            self.driver.find_element(*element).click()

    def check_title(self, tab):
        """ switch to the designated tab and return result \n
            Args: \n
                tab： [required] index of the tab to switch to
            Return: \n
                Boolean: True if retrieved text matches preset text, False if not
        """
        self.driver.switch_to.window(self.driver.window_handles[tab])
        element = self.driver.find_element(*SeparatePageLocators.check_agreement).text
        return True if str(element) == str('Terms and conditions') else False

    def input_text(self, text, ele):
        """ Input text in the requested element \n
            Args: \n
                element： [required] Elememnt name
                text ： [required] The inputed text
            Return: \n
                String: returned the text presented by the element
        """
        self.driver.find_element(*MainPageLocators.text_box).send_keys(text)
        self.driver.find_element(*MainPageLocators.find_button).click()
        x = self.driver.find_element(*ele).text
        return x







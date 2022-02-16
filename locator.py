from selenium.webdriver.common.by import By

class MainPageLocators(object):

    find_button = By.XPATH, '//button[@class = "btn btn-primary btn-block btn--icon btn--arrow"]',
    text_box = By.XPATH,'//input[@class = "form-control c-warranty__number"] ',
    terms_agreement = By.XPATH,'//a[@class = "cta-discrete cta-sm"]',
    close_cookie = By.XPATH,'//button[@class = "onetrust-close-btn-handler onetrust-close-btn-ui banner-close-button ot-close-icon"]',
    min_char_warning = By.XPATH, '//span[@class = "field-validation-error" and text() = "Minimum 6 characters required"]',
    check_agreement_valid = By.XPATH, '//span[@class = "field-validation-error" and text() = "Please enter a valid serial number"]',
    check_specify_valid = By.XPATH, '//span[@class = "field-validation-error" and text() = "Please specify a serial number"]',


class SeparatePageLocators(object):
    check_agreement = By.XPATH, '//div[@class = "c-bb"]/h1',





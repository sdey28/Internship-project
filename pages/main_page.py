from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import Page

class MainPage(Page):

    USERNAME_FIELD = (By.ID, "email-2")
    PASSWORD_FIELD = (By.ID, "field")
    CONTINUE_BTN = (By.XPATH, "//a[@wized='loginButton']")
    SIDE_NAV_OFF_PLAN = (By.XPATH,"//div[text()='Off-plan']")
    VERIFY_PAGE_OPENS = (By.XPATH, "//div[text()='Total projects']")
    FILTER_BTN = (By.CSS_SELECTOR, "[class='filter-button w-inline-block']")
    PRICE_FROM = (By.CSS_SELECTOR, "[class='input-lield-text w-input']")
    PRICE_TO = (By.CSS_SELECTOR, "[w-el-onchange-0-0='cca7a926-5d95-4018-a514-9633d083ed8c-0-0']")
    APPLY_FILTER_BTN = (By.CSS_SELECTOR, "[class='button-filter w-button']")


    def open_main(self):
        self.open('https://soft.reelly.io')


    def input_username(self):
        self.driver.find_element(*self.USERNAME_FIELD).send_keys("shuchita.dey@gmail.com")
        sleep(7)

    def input_password(self):
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys("Sawgoto357")
        sleep(7)

    def verify_continue_btn(self):
        self.driver.find_element(*self.CONTINUE_BTN).click()
        sleep(5)

    def side_nav(self):
        self.driver.find_element(*self.SIDE_NAV_OFF_PLAN).click()


    def verify_page(self):
        actual_result = self.driver.find_element(*self.VERIFY_PAGE_OPENS).text
        expected_result = 'Total projects'
        assert expected_result in actual_result, f"Expected '{expected_result}', got '{actual_result}'"



    def filter_btn(self):
        self.driver.find_element(*self.FILTER_BTN).click()


    def input_price_from(self):
        self.driver.find_element(*self.PRICE_FROM).send_keys('1200000')

    def input_price_to(self):
        self.driver.find_element(*self.PRICE_TO).send_keys('2000000')

    def click_apply_flr(self):
        self.driver.find_element(*self.APPLY_FILTER_BTN).click()

    def verify_price_in_range(self):
        self.driver.execute_script("window.scrollBy(0, 2000)", "")
        sleep(5)
        self.driver.execute_script("window.scrollBy(0, 2000)", "")

        product_cards = self.driver.find_elements(By.CLASS_NAME, 'number-price-text')

        for price_card in product_cards:
            price_txt = price_card.text


            covert_price = int(price_txt.replace('AED ', '').replace(',', ''))
            assert 1200000 <= covert_price <= 2000000, f"Price {covert_price} is not within the range (1200000 - 2000000)"




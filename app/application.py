from pages.base_page import Page
from pages.main_page import MainPage
from pages.reelly_app_mobile import ReellyPage




class Application:

    def __init__(self,driver):
        self.page = Page(driver)
        self.main_page = MainPage(driver)
        self.reelly_app_mobile =  ReellyPage(driver)

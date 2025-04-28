import time

from selenium.webdriver.common.by import By

from .base_page import BasePage


class WikiTitle(BasePage):
    WIKI_TITLE = (By.XPATH, "/html/body/div[2]/div/div[3]/main/header/h1/span")
    def isElementPresent(self):
        element = self.find_element(self.WIKI_TITLE)
        texto = element.text
        return texto
    def get_title(self):
        # Wait for the title element to be present
        time.sleep(2)
        # Get the title text
        title = self.find_element(self.WIKI_TITLE)
        return title.text

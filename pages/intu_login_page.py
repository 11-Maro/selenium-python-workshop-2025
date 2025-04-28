import time

from selenium.webdriver.common.by import By

from .base_page import BasePage


class intuLogin(BasePage):
    # Define locators for the login page elements
    USERNAME_FIELD = (By.ID, 'username')
    PASSWORD_FIELD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'loginbtn')

ERROR_MESSAGE = (By.XPATH, "/html/body/div[6]/div/div/section/div/div/div/div/div/div/div[2]/div")

def login(self, username, password):
        # Enter the username and password, then click the login button
        self.enter_text(self.USERNAME_FIELD, username)
        self.enter_text(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)

def isElementPresent(self ):
      element = self.find_element(self.ERROR_MESSAGE)
      texto = element.text
      return texto
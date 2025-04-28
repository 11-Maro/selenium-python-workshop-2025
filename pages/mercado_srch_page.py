import time

from selenium.webdriver.common.by import By

from .base_page import BasePage


class MercadoLibrePage(BasePage):
    SEARCH_BOX = (By.NAME, "as_word")
    RESULT_TITLES = (By.XPATH, "/html/body/main/div/div[2]/aside/div[1]/h1")

    def buscar_producto(self, producto):
        search = self.find_element(self.SEARCH_BOX)
        search.clear()
        search.send_keys(producto + "\n")
        time.sleep(3)  # Espera a que carguen los resultados

    def hay_resultados_con_texto(self, texto):
        resultados = self.driver.find_elements(*self.RESULT_TITLES)
        return any(texto.lower() in r.text.lower() for r in resultados)
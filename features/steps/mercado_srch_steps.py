import time

from selenium import webdriver

from pages.mercado_srch_page import MercadoLibrePage


@given('que estoy en la página principal de MercadoLibre')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.mercadolibre.com.co")
    context.page = MercadoLibrePage(context.driver)
    time.sleep(2)

@when('busco "iPhone 13"')
def step_impl(context):
    context.page.buscar_producto("iPhone 13")

@then('veo resultados que contienen el texto "iPhone"')
def step_impl(context):
    assert context.page.hay_resultados_con_texto("iPhone")
    context.driver.quit()
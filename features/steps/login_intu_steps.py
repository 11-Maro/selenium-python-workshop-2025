from behave import given, then, when
from selenium import webdriver

from pages.intu_login_page import intuLogin


@given('el usuario está en la página de inicio de sesión de intu')
@when('el usuario ingresa credenciales incorrectas')
@then('se muestra un mensaje de error indicando que las credenciales son incorrectas')
def step_given_intu_login(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.icesi.edu.co/moodle/login/index.php")
    context.intu_login_page = intuLogin(context.driver)

def step_when_intu_login(context):
    context.intu_login_page.login("wrong", "wrong_")

def step_then_intu_login(context):
    assert "Acceso inválido. Por favor, inténtelo otra vez." == context.intu_login_page.isElementPresent()
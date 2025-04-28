Feature: login de intu

Scenario: credenciales incorrectas
    Given el usuario está en la página de inicio de sesión de intu
    When el usuario ingresa credenciales incorrectas
    Then se muestra un mensaje de error indicando que las credenciales son incorrectas
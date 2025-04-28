Feature: Buscar productos en MercadoLibre

  Scenario: Buscar “iPhone 13” y verificar resultados
    Given que estoy en la página principal de MercadoLibre
    When busco "iPhone 13"
    Then veo resultados que contienen el texto "iPhone 13"
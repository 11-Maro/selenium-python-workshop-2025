Feature: Titulo de la página de Wikipedia


  Scenario: Verificar el título de la página de Wikipedia
    Given I am on the Wikipedia page for python
    When I check the title of the page
    Then the title should be Python
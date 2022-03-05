Feature: auth tests with Keycloak

#  1 Юзер без гражданства пытается попасть на страницу personal

  Scenario: A stateless user is trying to get to the personal page
    When Sleep "2" sec
    When I visited page "https://vk.com/"
    When Sleep "5" sec
    When I visited page "http://217.9.89.223"
    And Sleep "2" sec
    When Button click by element By ID: "login"
    When Check redirect to (enter first url part) Url: "https://esiatest.mai.ru/auth/realms/demo/"
    When Input Text: "r-38@mail.ru" element By ID: "username"
    When Input Text: "eqE-8M4-cx5-ser" element By ID: "password"
    And Button click by element By ID: "kc-login"
    And Sleep "2" sec
    When I visited page "http://217.9.89.223/applicants/"
    And Sleep "5" sec
    When Check redirect to (enter first url part) Url: "http://217.9.89.223/applicants/citizenship"
    And Sleep "2" sec
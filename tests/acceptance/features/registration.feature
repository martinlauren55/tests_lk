#Feature: Registration
#
#  @browser
#  Scenario: Access registration from the login page
#    Given anonymous user
#    When I visit /accounts/login
#    And I click "Войти"
#    Then I should be redirected
#    And I should see "Вход в учетную запись"

#  @browser
#  Scenario: Access registration from the login page
#    Given anonymous user
#    When I visit /accounts/manage
#    And I click "Получить доступ"
#    Then I should be redirected to /accounts/get_access
#    And I should see "Получение доступа"
#
#  @browser
#  Scenario: Access yandex test
#    When I visit https://yandex.ru/
#    Then I should see "Яндекс"


#  @browser
#  Scenario: Access signup page from the registration page
#    Given anonymous user
#    When I visit /accounts/manage
#    And I click "Подать заявление"
#    Then I should be redirected to /accounts/signup

#
#  @browser
#  Scenario: Impossible to signup without email
#    Given anonymous user
#    When I visit /accounts/signup
#    And I fill password with my email
#    And I click "Зарегистрироваться"
#    Then I should not be redirected
#
#  @browser
#  Scenario: Impossible to signup without a password
#    Given anonymous user
#    When I visit /accounts/signup
#    And I fill email with my email
#    And I click "Зарегистрироваться"
#    Then I should not be redirected
#
#  @browser
#  Scenario: Impossible to signup twice
#    Given logged out user
#    When I visit /accounts/signup
#    And I fill email with my email
#    And I fill password with my password
#    And I click "Зарегистрироваться"
#    Then I should see "Пользователь с данным E-mail уже зарегистрирован"
#
#

class Locator():
    ACCOUNT_BUTTON="//a[contains(@href, '/account')]"
    REGISTRATION_BUTTON="//a[contains(@href, '/register')]"
    NAME_INPUT="(.//label[text()='Имя']/following::input)[1]"
    EMAIL_INPUT="(.//label[text()='Email']/following::input)[1]"
    PASS_INPUT="(.//label[text()='Пароль']/following::input)[1]"
    REGISTRATION_COMMIT_BUTTON="//button[contains(text(), 'Зарегистрироваться')]"
    LOGIN_BUTTON="//button[contains(text(), 'Войти')]"
    CREATE_ORDER_BUTTON="//button[contains(text(), 'Оформить заказ')]"
from screens.base_screen import BaseScreen


class AuthWebviewScreen(BaseScreen):
    def __init__(self, context):
        super().__init__(context)
        self.elements.update({
            "Toolbar": "//*[contains(@resource-id, 'faToolbar')]",
            "BackButton": "//android.widget.ImageButton[@content-desc='Назад']",
            "LoginInput": "//android.widget.EditText[@resource-id='login']",
            "PasswordInput": "//android.widget.EditText[@resource-id='password']",
            "LoginButton": "//android.widget.Button[@text='Нажмите, чтобы войти']",
        })
        self.required_elements.append(self.elements.get("Toolbar"))
        self.required_elements.append(self.elements.get("LoginInput"))
        self.required_elements.append(self.elements.get("PasswordInput"))
        self.required_elements.append(self.elements.get("LoginButton"))

    def login(self, login, password):
        self.send_keys_to_element("LoginInput", login)
        self.send_keys_to_element("PasswordInput", password)
        self.click_element("LoginButton")
        self.wait_for_element_disappear("LoginButton")


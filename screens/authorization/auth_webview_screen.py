from framework.base_elements import BaseScreen, ViewGroup, Button, Input


class AuthWebviewScreen(BaseScreen):
    def __init__(self, context):
        super().__init__(context)
        self.elements.update({
            "Toolbar": ViewGroup("Toolbar", "//*[contains(@resource-id, 'faToolbar')]", self),
            "BackButton": Button("BackButton", "//android.widget.ImageButton[@content-desc='Назад']", self),
            "LoginInput": Input("LoginInput", "//android.widget.EditText[@resource-id='login']", self),
            "PasswordInput": Input("PasswordInput", "//android.widget.EditText[@resource-id='password']", self),
            "LoginButton": Button("LoginButton", "//android.widget.Button[@text='Нажмите, чтобы войти']", self),
        })
        self.required_elements.append(self.elements.get("Toolbar"))
        self.required_elements.append(self.elements.get("LoginInput"))
        self.required_elements.append(self.elements.get("PasswordInput"))
        self.required_elements.append(self.elements.get("LoginButton"))

    def login(self, login, password):
        self.elements["LoginInput"].send_keys(login)
        self.elements["PasswordInput"].send_keys(password)
        self.elements["LoginButton"].click()
        self.elements["LoginButton"].wait_for_disappear()

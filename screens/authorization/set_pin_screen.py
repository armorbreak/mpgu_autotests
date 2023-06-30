from screens.base_screen import BaseScreen
from time import sleep


class SetPinScreen(BaseScreen):
    def __init__(self, context):
        super().__init__(context)
        self.elements.update({
            "GreetingsText": "//*[contains(@resource-id, 'fpTvGreetings')]",
            "Avatar": "//*[contains(@resource-id, 'fpIvAvatarLogo')]",
            "SetPinTitle": "//*[contains(@resource-id, 'fpTvPinTitle') and @text='Придумайте код доступа']",
            "RepeatPinTitle": "//*[contains(@resource-id, 'fpTvPinTitle') and @text='Повторите код']",
            "PinInputKeyboard": "//android.view.ViewGroup[contains(@resource-id, 'vpkGlPincodeContainer')]",
            "LogoutButton": "//android.widget.Button[contains(@resource-id, 'vpkBtnLogout')]",
        })
        self.required_elements.append(self.elements.get("GreetingsText"))
        self.required_elements.append(self.elements.get("Avatar"))
        self.required_elements.append(self.elements.get("PinInputKeyboard"))
        self.required_elements.append(self.elements.get("LogoutButton"))

    def set_pin(self, pin):
        for n in range(2):
            for digit in str(pin):
                pin_digit_button = "//android.widget.Button[contains(@resource-id, 'vpkBtn%s')]" % (str(digit))
                self.click_element(pin_digit_button)
                sleep(0.3)
            if n == 0:
                self.wait_for_element_disappear("SetPinTitle")
                self.wait_for_element_is_visible("RepeatPinTitle")
            else:
                self.wait_for_element_disappear("RepeatPinTitle", timeout=60)

from framework.base_elements import BaseScreen, Text, Image, Button, ViewGroup
from time import sleep


class SetPinScreen(BaseScreen):
    def __init__(self, context):
        super().__init__(context)
        self.elements.update({
            "GreetingsText": Text("GreetingsText", "//*[contains(@resource-id, 'fpTvGreetings')]", self),
            "Avatar": Image("Avatar", "//*[contains(@resource-id, 'fpIvAvatarLogo')]", self),
            "SetPinTitle": Text("SetPinTitle",
                                "//*[contains(@resource-id, 'fpTvPinTitle') and @text='Придумайте код доступа']", self),
            "RepeatPinTitle": Text("RepeatPinTitle",
                                   "//*[contains(@resource-id, 'fpTvPinTitle') and @text='Повторите код']", self),
            "PinInputKeyboard": ViewGroup("PinInputKeyboard",
                                          "//android.view.ViewGroup[contains(@resource-id, 'vpkGlPincodeContainer')]", self),
            "LogoutButton": Button("LogoutButton", "//android.widget.Button[contains(@resource-id, 'vpkBtnLogout')]", self),
        })
        self.required_elements.append(self.elements.get("GreetingsText"))
        self.required_elements.append(self.elements.get("Avatar"))
        self.required_elements.append(self.elements.get("PinInputKeyboard"))
        self.required_elements.append(self.elements.get("LogoutButton"))

    def set_pin(self, pin):
        for n in range(2):
            for digit in str(pin):
                pin_digit_button = Button("",
                                          "//android.widget.Button[contains(@resource-id, 'vpkBtn%s')]" % (str(digit)),
                                          self)
                pin_digit_button.click()
                sleep(0.3)
            if n == 0:
                self.elements["SetPinTitle"].wait_for_disappear()
                self.elements["RepeatPinTitle"].wait_for_appear()
            else:
                self.elements["RepeatPinTitle"].wait_for_disappear(timeout=60)

from screens.base_screen import BaseScreen
from time import sleep


class Forced2FaScreen(BaseScreen):
    def __init__(self, context):
        super().__init__(context)
        self.elements.update({
            "ToolbarTitle": "//*[contains(@resource-id, 'ffbToolbar')]/android.widget.TextView[@text='Авторизация']",
            "Title": "//*[contains(@resource-id, 'ffbTvTitle')]",
            "ShieldImage": "//*[contains(@resource-id, 'ffbImage')]",
            "Add2FaButton": "//*[contains(@resource-id, 'ffbBtnAdd2fa')]",
            "Skip2FaButton": "//*[contains(@resource-id, 'ffbBtnSkip')]",
        })
        self.required_elements.append(self.elements.get("ToolbarTitle"))
        self.required_elements.append(self.elements.get("Title"))
        self.required_elements.append(self.elements.get("ShieldImage"))
        self.required_elements.append(self.elements.get("Add2FaButton"))

    def skip(self, timeout=10):
        try:
            self.wait_for_screen_loaded(timeout=timeout)
            self.click_element("Skip2FaButton")
            self.wait_for_element_disappear("Title")
        except Exception:
            pass

from framework.base_elements import BaseScreen, Text, Image, Button


class Forced2FaScreen(BaseScreen):
    def __init__(self, context):
        super().__init__(context)
        self.elements.update({
            "ToolbarTitle": Text("ToolbarTitle",
                                 "//*[contains(@resource-id, 'ffbToolbar')]/android.widget.TextView[@text='Авторизация']",
                                 self),
            "Title": Text("Title", "//*[contains(@resource-id, 'ffbTvTitle')]", self),
            "ShieldImage": Image("ShieldImage", "//*[contains(@resource-id, 'ffbImage')]", self),
            "Add2FaButton": Button("Add2FaButton", "//*[contains(@resource-id, 'ffbBtnAdd2fa')]", self),
            "Skip2FaButton": Button("Skip2FaButton", "//*[contains(@resource-id, 'ffbBtnSkip')]", self),
        })
        self.required_elements.append(self.elements.get("ToolbarTitle"))
        self.required_elements.append(self.elements.get("Title"))
        self.required_elements.append(self.elements.get("ShieldImage"))
        self.required_elements.append(self.elements.get("Add2FaButton"))

    def skip(self, timeout=10):
        try:
            self.wait_for_screen_loaded(timeout=timeout)
            self.elements["Skip2FaButton"].click()
            self.elements["Title"].wait_for_disappear()
        except Exception:
            pass

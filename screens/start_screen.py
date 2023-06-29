from screens.base_screen import BaseScreen
from selenium.webdriver.common.by import By
from creds import contour


class StartScreen(BaseScreen):
    def __init__(self, context):
        super().__init__(context)
        self.elements.update({
            "Logo": "//*[contains(@resource-id, 'flIvAppLogo')]",
            "LoginButton": "//*[contains(@resource-id, 'flBtnLogin')]",
            "ContourText": "//*[contains(@resource-id, 'flTvContourText')]",
            "ChangeContourButton": "//*[contains(@resource-id, 'flIvContourLogo')]",
            "ContourSelectionBottomSheet": "//*[contains(@resource-id, 'design_bottom_sheet')]"
        })
        self.required_elements.append(self.elements.get("Logo"))
        self.required_elements.append(self.elements.get("LoginButton"))

    def get_contour(self):
        current_contour = self.context.driver.find_element(By.XPATH, self.elements.get("ContourText")).text
        return current_contour

    def select_contour(self, target):
        if self.get_contour().lower() != target.lower():
            self.click_element("ChangeContourButton")
            self.wait_for_element_is_visible("ContourSelectionBottomSheet")
            contour_selector = "//android.widget.TextView[contains(@resource-id, 'bottomSheetCheckableDialogItemTvText')" \
                               " and translate(@text, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz') = '%s']" % (target.lower())
            self.click_element(contour_selector)
            self.wait_for_screen_loaded()

    def authorize(self, login, password, contour=contour, pin_code=3366):
        onboarding_screen = self.context.screen_manager.get_screen("Onboarding")
        onboarding_screen.skip_tutorial()
        self.wait_for_screen_loaded()
        self.select_contour(contour)
        self.click_element("LoginButton")
        auth_webview = self.context.screen_manager.get_screen("AuthWebview")
        auth_webview.wait_for_screen_loaded()
        auth_webview.login(login, password)
        set_pin_screen = self.context.screen_manager.get_screen("SetPin")
        set_pin_screen.wait_for_screen_loaded()
        set_pin_screen.set_pin(pin_code)

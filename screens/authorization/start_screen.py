from framework.base_elements import BaseScreen, Image, Text, Button, FrameLayout
from creds import contour


class StartScreen(BaseScreen):
    def __init__(self, context):
        super().__init__(context)
        self.elements.update({
            "Logo": Image("Logo", "//*[contains(@resource-id, 'flIvAppLogo')]", self),
            "LoginButton": Button("LoginButton", "//*[contains(@resource-id, 'flBtnLogin')]", self),
            "ContourText": Text("ContourText", "//*[contains(@resource-id, 'flTvContourText')]", self),
            "ChangeContourButton": Button("ChangeContourButton", "//*[contains(@resource-id, 'flIvContourLogo')]", self),
            "ContourSelectionBottomSheet": FrameLayout("ContourSelectionBottomSheet",
                                                       "//*[contains(@resource-id, 'design_bottom_sheet')]", self),
        })
        self.required_elements.append(self.elements.get("Logo"))
        self.required_elements.append(self.elements.get("LoginButton"))

    def get_contour(self):
        current_contour = self.elements.get("ContourText").get_text()
        return current_contour

    def select_contour(self, target):
        if self.get_contour().lower() != target.lower():
            self.elements["ChangeContourButton"].click()
            self.elements["ContourSelectionBottomSheet"].wait_for_appear()
            contour_selector = Text("",
                                    "//android.widget.TextView[contains(@resource-id, 'bottomSheetCheckableDialogItemTvText')" \
                                    " and translate(@text, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz') = '%s']"
                                    % (target.lower()),
                                    self)
            contour_selector.click()
            self.wait_for_screen_loaded()

    def authorize(self, login, password, contour=contour, pin_code=3366):
        onboarding_screen = self.context.screen_manager.get_screen("Onboarding")
        onboarding_screen.skip_tutorial()
        self.wait_for_screen_loaded()
        self.select_contour(contour)
        self.elements["LoginButton"].click()
        auth_webview = self.context.screen_manager.get_screen("AuthWebview")
        auth_webview.wait_for_screen_loaded()
        auth_webview.login(login, password)
        set_pin_screen = self.context.screen_manager.get_screen("SetPin")
        set_pin_screen.wait_for_screen_loaded()
        set_pin_screen.set_pin(pin_code)
        forced_2fa_screen = self.context.screen_manager.get_screen("Forced2Fa")
        forced_2fa_screen.skip()
        main_screen = self.context.screen_manager.get_screen("MainScreen")
        main_screen.close_supported_links_popup()
        main_screen.wait_for_screen_loaded()

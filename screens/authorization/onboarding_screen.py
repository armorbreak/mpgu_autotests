from framework.base_elements import BaseScreen, Image, Button


class OnboardingScreen(BaseScreen):
    def __init__(self, context):
        super().__init__(context)
        self.elements.update({
            "GooglePlayUpdateDeclineButton": Button("GooglePlayUpdateDeclineButton",
                                                    "//android.widget.Button[contains(@resource-id, 'resource_name_obfuscated') and contains(@text, 'НЕТ')]",
                                                    self),
            "OnboardingStoriesImage": Image("OnboardingStoriesImage", "//*[contains(@resource-id, 'fsspVpStories')]", self),
            "NextButton": Button("NextButton", "//*[contains(@resource-id, 'fsspBtnNext')]", self),
        })
        self.required_elements.append(self.elements.get("OnboardingStoriesImage"))

    def skip_tutorial(self):
        while self.elements["OnboardingStoriesImage"].is_visible(timeout=1):
            self.elements["NextButton"].click()
            
    def close_google_play_update_if_displayed(self):
        if self.context.driver.desired_capabilities['platformName'].lower() == "android":
            if self.elements["GooglePlayUpdateDeclineButton"].is_visible(timeout=2):
                self.elements["GooglePlayUpdateDeclineButton"].click()
                
    def wait_for_screen_loaded(self, timeout=15, check_google_play_popup=False):
        if check_google_play_popup:
            self.close_google_play_update_if_displayed()
        super(OnboardingScreen, self).wait_for_screen_loaded()

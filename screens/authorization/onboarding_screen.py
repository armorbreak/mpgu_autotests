from screens.base_screen import BaseScreen


class OnboardingScreen(BaseScreen):
    def __init__(self, context):
        super().__init__(context)
        self.elements.update({
            "OnboardingStories": "//*[contains(@resource-id, 'fsspVpStories')]",
            "NextButton": "//*[contains(@resource-id, 'fsspBtnNext')]"
        })
        self.required_elements.append(self.elements.get("OnboardingStories"))

    def skip_tutorial(self):
        while self.element_is_displayed(self.elements.get("OnboardingStories"), timeout=1):
            self.click_element(self.elements.get("NextButton"))

from screens.base_screen import BaseScreen
from selenium.webdriver.common.by import By
from creds import contour


class MainScreen(BaseScreen):
    def __init__(self, context):
        super().__init__(context)
        self.elements.update({
            "RobotMaxSearchField": "//*[contains(@resource-id, 'fmTvRobot')]",
            "RobotMaxButton": "//*[contains(@resource-id, 'fmIvRobotIcon')]",
            "GosScan": "//*[contains(@resource-id, 'fmLavGosScan')]",
            "ContentArea": "//*[contains(@resource-id, 'fmClContentRoot')]",
            "NavigationMain": "//*[contains(@resource-id, 'navigationMain')]",
            "NavigationServices": "//*[contains(@resource-id, 'navigationServices')]",
            "NavigationDocs": "//*[contains(@resource-id, 'navigationDocuments')]",
            "NavigationPayments": "//*[contains(@resource-id, 'navigationPayments')]",
            "NavigationProfile": "//*[contains(@resource-id, 'navigationProfile')]",
            "SupportedLinksPopup": "//*[contains(@resource-id, 'parentPanel')]//*[contains(@resource-id, 'alertTitle') "
                                   "and @text='Добавьте поддерживаемые ссылки']",
            "SupportedLinksSkipButton": "//*[contains(@resource-id, 'parentPanel')]//*[contains(@resource-id, 'button2') "
                                   "and @text='ПОЗЖЕ']",
        })
        self.required_elements.append(self.elements.get("RobotMaxSearchField"))
        self.required_elements.append(self.elements.get("RobotMaxButton"))
        self.required_elements.append(self.elements.get("GosScan"))
        self.required_elements.append(self.elements.get("ContentArea"))
        self.required_elements.append(self.elements.get("NavigationMain"))
        self.required_elements.append(self.elements.get("NavigationServices"))
        self.required_elements.append(self.elements.get("NavigationDocs"))
        self.required_elements.append(self.elements.get("NavigationPayments"))
        self.required_elements.append(self.elements.get("NavigationProfile"))

    def close_supported_links_popup(self):
        if self.element_is_displayed("SupportedLinksPopup", timeout=5):
            self.click_element("SupportedLinksSkipButton")
            self.wait_for_element_disappear("SupportedLinksPopup")


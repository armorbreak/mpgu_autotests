from framework.base_elements import BaseScreen, Text, Image, FrameLayout, ViewGroup, Button


class MainScreen(BaseScreen):
    def __init__(self, context):
        super().__init__(context)
        self.elements.update({
            "RobotMaxSearchField": Text("RobotMaxSearchField", "//*[contains(@resource-id, 'fmTvRobot')]", self),
            "RobotMaxImageButton": Image("RobotMaxImageButton", "//*[contains(@resource-id, 'fmIvRobotIcon')]", self),
            "GosScanImageButton": Image("GosScanImageButton", "//*[contains(@resource-id, 'fmLavGosScan')]", self),
            "ContentArea": ViewGroup("ContentArea", "//*[contains(@resource-id, 'fmClContentRoot')]", self),
            "NavigationMain": FrameLayout("NavigationMain", "//*[contains(@resource-id, 'navigationMain')]", self),
            "NavigationServices": FrameLayout("NavigationServices", "//*[contains(@resource-id, 'navigationServices')]",
                                              self),
            "NavigationDocs": FrameLayout("NavigationDocs", "//*[contains(@resource-id, 'navigationDocuments')]", self),
            "NavigationPayments": FrameLayout("NavigationPayments", "//*[contains(@resource-id, 'navigationPayments')]",
                                              self),
            "NavigationProfile": FrameLayout("NavigationProfile", "//*[contains(@resource-id, 'navigationProfile')]",
                                             self),
            "SupportedLinksPopupTitle": Text("SupportedLinksPopupTitle",
                                             "//*[contains(@resource-id, 'parentPanel')]"
                                             "//*[contains(@resource-id, 'alertTitle') "
                                             "and @text='Добавьте поддерживаемые ссылки']",
                                             self),
            "SupportedLinksSkipButton": Button("SupportedLinksSkipButton",
                                               "//*[contains(@resource-id, 'parentPanel')]"
                                               "//*[contains(@resource-id, 'button2') "
                                               "and @text='ПОЗЖЕ']", self),
        })
        self.required_elements.append(self.elements.get("RobotMaxSearchField"))
        self.required_elements.append(self.elements.get("RobotMaxImageButton"))
        self.required_elements.append(self.elements.get("GosScanImageButton"))
        self.required_elements.append(self.elements.get("ContentArea"))
        self.required_elements.append(self.elements.get("NavigationMain"))
        self.required_elements.append(self.elements.get("NavigationServices"))
        self.required_elements.append(self.elements.get("NavigationDocs"))
        self.required_elements.append(self.elements.get("NavigationPayments"))
        self.required_elements.append(self.elements.get("NavigationProfile"))

    def close_supported_links_popup(self):
        if self.elements["SupportedLinksPopupTitle"].is_visible(timeout=5):
            self.elements["SupportedLinksSkipButton"].click()
            self.elements["SupportedLinksPopupTitle"].wait_for_disappear()



class navigationHelper:
    def __init__(self, App):
        self.app = App

    def openLoginPage(self, isLogin=True):
        wd = self.app.wd
        if wd.current_url.endswith("login_page.php"):
            if len(wd.find_elements_by_name("login_form"))>0:
                return
        wd.get(self.app.base_url)

    def openMenu(self, _tab):
        wd = self.app.wd
        wd.find_element_by_link_text(_tab).click()
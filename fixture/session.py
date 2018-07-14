
class sessionHelper:

    def __init__(self, App):
        self.app = App

    # login method
    def login(self, _login, _password):
        wd = self.app.wd
        self.app.navigation.openLoginPage()
        self.app.set_text_field("username", _login)
        self.app.set_text_field("password", _password)
        wd.find_element_by_xpath("//form[@name='login_form']//input[@value='Login']").click()

    # logout
    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()

    def ensure_login(self, login, password):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(login):
                return
            else:
                self.logout()
        self.login(login, password)

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def is_logged_in_as(self, login):
        wd = self.app.wd
        return wd.find_element_by_xpath("//td[@class='login-info-left']/span[@class='italic']").text == login

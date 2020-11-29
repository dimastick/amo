from selene import browser
from selene.support.jquery_style_selectors import s

from src.pages.MainPage import MainPage


class LoginPage:
    def __init__(self):
        self.login_input = s('#session_end_login')
        self.password_input = s('#password')
        self.login_btn = s('#auth_submit')

    def open(self):
        browser.open_url('/')
        return self

    def login(self, user):
        self.login_input.set(user.login)
        self.password_input.set(user.password)
        self.login_btn.click()
        return MainPage()






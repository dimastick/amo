from selene.support.jquery_style_selectors import s, ss
from selene.conditions import *
from selene import browser

from src.pages.ContactDetailSection import ContactDetailSection


class ContactListSection:
    def __init__(self):
        super().__init__()
        self.search_input = s('#search_input')

    def open_contact_detail(self, email):
        # browser.execute_script("location.reload()")
        self.search_input.set(email).press_enter()
        s('*[data-body-fixed="0"]').should_be(visible)
        s('.page-loading').should_not_be(visible)
        ss('div[id^="list_item"] div[data-field-id="name"]').find_by(text(email)).s("a").click()
        return ContactDetailSection()
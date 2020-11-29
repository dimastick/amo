from selene import browser
from selene.support.jquery_style_selectors import s, ss
from selene.conditions import *

from src.pages.ContactListSection import ContactListSection
from src.pages.SettingsSection import SettingsSection


class MainPage:

    def __init__(self):
        self.menu = s('#left_menu')
        self.page_container = s('#page_holder')

    def open_settings_section(self):
        self.menu.s('div[data-entity="settings"]').click()
        self.page_container.s('h2.aside__head').should_have(exact_text('Настройки'.upper()))
        s('body.page-loading').should_not_be(visible)
        return SettingsSection()

    def open_contact_list_section(self):
        self.menu.s('div[data-entity="catalogs"]').hover()
        s('.h-elevated').should_be(visible)
        ss('ul.aside__list li').find_by(text('Контакты')).click()
        s('.page-loading').should_not_be(visible)
        s('.h-text-overflow').should_have(exact_text('КОНТАКТЫ'))
        browser.execute_script(
            'var element = document.getElementById("left-menu-overlay");'
            'element.classList.remove("default-overlay-visible");'
            'element.classList.remove("hover-overlay");'
        )
        return ContactListSection()
from selene import browser
from selene.support.jquery_style_selectors import s, ss
from selene.conditions import *


class WidgetSettings:
    def __init__(self):
        self.privacy_policy_accept = s('div.amo_sendpulse_dp label.widget-settings__checkbox-privacy-policy')
        self.install_widget_btn = s('button[id="amo_sendpulse_dp"]')
        self.sp_id_input = s('input[name="sendpulse_id"]')
        self.sp_secret_input = s('input[name="sendpulse_secret"]')
        self.save_settings_btn = s('#save_amo_sendpulse_dp')

    def install_widget(self, user_id, secret):
        self.privacy_policy_accept.click()
        self.install_widget_btn.click()
        self.sp_id_input.set(user_id)
        self.sp_secret_input.set(secret)
        self.save_settings_btn.click()
        s('.widget-settings').should_not(visible)

        # after widget pop-up is closed two widgets are displayed.
        # Should be only 1. By search it is not filtered
        browser.execute_script("location.reload()")
        return SettingsSection()

    def check_widget_status(self):
        s('.sp-inc-status-bar').should_have(text('Виджет работает'))
        self.save_settings_btn.click()
        s('.widget-settings').should_not(visible)
        s('*[data-body-fixed="1"]').should_not_be(visible)
        return SettingsSection()


class SettingsSection:

    def __init__(self):
        self.search_input = s('#widgets_search')

    def open_widget_settings(self):
        self.search_input.set('SendPulse')
        s('*[data-body-fixed="1"]').should_not_be(visible)

        (
                s('.widget-card__wrapper[title="SendPulse"]')
                .should_be(visible)
                .should_be(clickable)
                .click()
        )

        return WidgetSettings()
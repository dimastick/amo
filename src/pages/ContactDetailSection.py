from selene.support.jquery_style_selectors import s, ss
from selene.conditions import *

from src.components.custom_fields import CustomField
from src.modules.cf_constants import CFType, CFSection, EntityAbbr


class ContactDetailSection:
    def __init__(self):
        self.settings_btn = s('div[data-id="settings"]')

    def open_entity_settings(self):
        self.settings_btn.click()
        s('.card-cf__description').should_have(text('Настройка свойств полей'))
        return self

    def delete_custom_fields(self, cf_section=CFSection.CONTACTS_CF):
        container_with_cfs = s('.cf-section[data-type="{section}"]'.format(**{'section': cf_section.value}))

        custom_fields = container_with_cfs.ss(
            "div.cf-field-wrapper:not(.predefined):not(.cf-field-wrapper-fake)")

        while custom_fields:

            custom_fields.first().click()
            cf = CustomField()
            cf.delete_cf()

            custom_fields = container_with_cfs.ss(
                "div.cf-field-wrapper:not(.predefined):not(.cf-field-wrapper-fake)")

    def add_custom_field(self, cf_section=CFSection.CONTACTS_CF, cf_type=CFType.TEXT, entity_abbr=EntityAbbr.CONTACT):

        container_with_cfs = s('.cf-section[data-type="{section}"]'.format(**{'section': cf_section}))
        add_cf_button = container_with_cfs.s('.cf-field-add.js-card-cf-add-field')
        add_cf_button.click()

        cf = CustomField()
        cf.add_cf(cf_type, entity_abbr)

    # def open_company_list(self):
    #     self.menu.catalogs.click()
    #     ss('ul.aside__list li').find_by(text('Компании')).click()
    #     s('*[data-body-fixed="1"]').should_not_be(visible)
    #     s('.page-loading').should_not_be(visible)
    #     s('.h-text-overflow').should_have(exact_text('Компании'))
    #     return 1





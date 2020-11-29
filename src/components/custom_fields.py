from selene.support.jquery_style_selectors import s, ss
from selene.conditions import *
from selene import by

from src.modules.cf_constants import CFType


class CustomField:

    def __init__(self):
        self.cf_props_container = s('div[id^="cf_field"] div.edit-mode')  # .edit-mode class
        self.name_input = self.cf_props_container.s('input[name="name"]')
        self.cf_type_select = self.cf_props_container.s('.cf-field-edit__type-select')

        self.save_btn = self.cf_props_container.s('button.js-modal-accept')
        self.cancel_btn = self.cf_props_container.s('button.button-cancel')
        self.delete_btn = self.cf_props_container.s('div.js-modal-trash')

    def delete_cf(self):
        self.delete_btn.click()
        s('.modal-body').s('button.js-modal-accept').click()
        s('.modal.modal-list.js-modal-confirm').should_not_be(visible)

    def add_cf(self, cf_type, entity):
        (
            self
            .cf_type_select
            .click()
            .ss('ul.control--select--list-opened li span')
            .filter(text(cf_type.value)).first()
            .scroll_to()
            .click()
        )

        self.name_input.set('_'.join([entity.value, cf_type.name]))

        if cf_type in [CFType.LIST, CFType.MULTI_LIST, CFType.SWITCHER]:
            opt_inputs = ss('input[placeholder="Вариант"]')

            for i, opt_input in zip(range(1, 6), opt_inputs):
                opt_input.set('_'.join([cf_type.value, str(i)]))

        self.save_btn.click()
        self.cf_props_container.should_not_be(visible)


import pytest

from src.pages.LoginPage import LoginPage
from src.modules.user import User

from src.modules.cf_constants import CFType, CFSection, EntityAbbr

CONTACT_EMAIL = 'contact@e.cn.ua'


def test_user_can_login(conf):
    user = User(conf['amo_credentials']['login'], conf['amo_credentials']['password'])

    main_page = LoginPage().open().login(user=user)
    widget_settings = main_page.open_settings_section().open_widget_settings()
    settings_section = widget_settings.install_widget(
        conf['sp_keys']['id'],
        conf['sp_keys']['secret'],

    ).open_widget_settings().check_widget_status()

    cont_list_section = main_page.open_contact_list_section()

    cont_list_section.open_contact_detail(CONTACT_EMAIL).open_entity_settings().delete_custom_fields()

    # cont_settings_tab = cont_list_section.open_contact_detail(CONTACT_EMAIL).open_entity_settings()
    # for cf_type in list(CFType):
    #     cont_settings_tab.add_custom_field(
    #         cf_section=CFSection.CONTACTS_CF.value, cf_type=cf_type, entity_abbr=EntityAbbr.CONTACT
    #     )

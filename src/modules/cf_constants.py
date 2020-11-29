from enum import Enum


class EntityAbbr(Enum):
    CONTACT = 'CONT'
    COMPANY = 'CORP'


class CFSection(Enum):
    CONTACTS_CF = 'contacts'
    COMPANIES_CF = 'companies'


class CFType(Enum):
    TEXT = 'Текст'
    DIGIT = 'Число'
    FLAG = 'Флаг'
    LIST = 'Список'
    MULTI_LIST = 'Мультисписок'
    DATE = 'Дата'
    LINK = 'Ссылка'
    TEXT_AREA = 'Текстовая область'
    SWITCHER = 'Переключатель'
    SHORT_ADDRESS = 'Короткий адрес'
    ADDRESS = 'Адрес'
    DATE_OF_BIRTH = 'День рождения'
    LEGAL_ENTITY = 'Юр. лицо'
    DATETIME = 'Дата и время'
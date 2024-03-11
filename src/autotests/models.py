import pytest
from core.models import Translations
from autotests.logging import passed
from core.setup import transltions_path


async def validation_dict():
    translations = Translations()
    translations.from_dict({
        'en': {'key1': 'value1', 'key2': 'value2'},
        'uk': {'key1': 'значення1', 'key2': 'значення2'},
    })
    passed('translations validation')
    

async def extra_uk_key_dict():
    translations = Translations()
    with pytest.raises(ValueError):
        translations.from_dict({
            'en': {'key1': 'value1'},
            'uk': {'key1': 'значення1', 'key2': 'значення2'},
        })
    passed('extra ukrainian key')


async def extra_en_key_dict():
    translations = Translations()
    translations.from_dict({
        'en': {'key1': 'value1', 'key2': 'value2'},
        'uk': {'key1': 'значення1'},
    })
    passed('extra english key')


async def validation_json():
    translations = Translations()
    translations.from_dir(
        transltions_path
    )


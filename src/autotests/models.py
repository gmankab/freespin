import pytest
from core.models import Translations
from autotests.errors import passed


async def translations_validation():
    Translations(root={
        'en': {'key1': 'value1', 'key2': 'value2'},
        'uk': {'key1': 'значення1', 'key2': 'значення2'},
    })
    passed('translations validation')
    

async def extra_uk_key():
    with pytest.raises(ValueError):
        Translations(root={
            'en': {'key1': 'value1'},
            'uk': {'key1': 'значення', 'key2': 'значення2'},
        })
    passed('extra ukrainian key')


async def extra_en_key():
    Translations(root={
        'en': {'key1': 'value1', 'key2': 'value2'},
        'uk': {'key1': 'значення1'},
    })
    passed('extra english key')


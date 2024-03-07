from pydantic import RootModel, model_validator


class Translations(RootModel[dict[str, dict[str, str]]]):
    root: dict[str, dict[str, str]]

    @model_validator(mode='after')
    def check_english_keys(self, values):
        english_keys = set(self.root['en'].keys())
        for lang_code, translation in self.root.items():
            if lang_code == 'en':
                continue
            if not english_keys.issuperset(
                translation.keys()
            ):
                extra_keys = set(translation.keys()) - english_keys
                raise ValueError(
                    f'{extra_keys} found in {lang_code} but not found in en'
                )
        return values


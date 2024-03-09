from pydantic import BaseModel
from pathlib import Path
import json


class Translations(BaseModel):
    langs: dict[str, dict[str, str]] = {}

    def from_dict(
        self,
        langs: dict[str, dict[str, str]] = {}
    ) -> None:
        self.langs = langs
        self.validation()

    def from_dir(
        self,
        langs_dir_path: Path,
    ) -> None:
        for filename in langs_dir_path.iterdir():
            with filename.open() as file:
                self.langs[filename.stem] = json.load(file)
        self.validation()

    def validation(self) -> None:
        assert 'en' in self.langs
        english_keys = set(self.langs['en'].keys())
        for lang_code, translation in self.langs.items():
            if lang_code == 'en':
                continue
            if not english_keys.issuperset(
                translation.keys()
            ):
                extra_keys = set(translation.keys()) - english_keys
                raise ValueError(
                    f'{extra_keys} found in {lang_code} but not found in en'
                )


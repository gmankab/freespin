from autotests import (
    models,
    errors,
)
import autotests.pyright
import autotests.requirements
import asyncio


async def main():
    background_requirements = asyncio.create_task(
        autotests.requirements.background()
    )
    background_pyright = asyncio.create_task(
        autotests.pyright.background()
    )
    foreground = [
        models.validation_dict,
        models.extra_uk_key_dict,
        models.extra_en_key_dict,
        models.validation_json
    ]
    for func in foreground:
        try:
            await func()
        except:
            errors.write_error()
    await autotests.pyright.get_result(
        await background_pyright
    )
    await autotests.requirements.get_result(
        await background_requirements
    )


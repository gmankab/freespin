from autotests import (
    models,
    logging,
)
from core import (
    common,
    status,
)
import autotests.pyright
import autotests.requirements
import asyncio
import os


async def main():
    exit_code: int = 0
    common.console.log(status.status.get())
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
            logging.write_error()
            exit_code = 1
    success = await autotests.pyright.get_result(
        await background_pyright
    )
    if not success:
        exit_code = 1
    await autotests.requirements.get_result(
        await background_requirements
    )
    os._exit(exit_code)


import autotests.errors
import core.setup
import subprocess
import asyncio
import json


async def get_result(
    output_str: str,
):
    output_dict = json.loads(output_str)
    if output_dict['generalDiagnostics']:
        autotests.errors.write_text(
            name = 'pyright',
            text = output_str,
        )
    else:
        autotests.errors.passed(
            'pyright test',
        )


async def background() -> str:
    venv_python, _ = core.setup.get_venv_python_pip()
    cmd = [
            str(venv_python),
            '-m',
            'pyright',
            str(core.setup.src_path),
            '--outputjson',
            '--project',
            str(core.setup.app_path / 'pyrightconfig.json'),
    ]
    process = await asyncio.create_subprocess_shell(
        cmd=' '.join(cmd),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    stdout, _ = await process.communicate()
    return str(stdout.decode())


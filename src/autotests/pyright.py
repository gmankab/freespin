import autotests.logging
import core.setup
import subprocess
import asyncio
import json


async def get_result(
    output_str: str,
) -> bool:
    '''
    returns true if test passed, false if not passed
    '''
    if not output_str:
        return True
    try:
        output_dict = json.loads(output_str)
    except:
        autotests.logging.write_text(
            name = 'pyright',
            text = f'failed to decode: {output_str}'
        )
        return False
    if output_dict['generalDiagnostics']:
        autotests.logging.write_text(
            name = 'pyright',
            text = output_str,
        )
        return False
    else:
        autotests.logging.passed(
            'pyright test',
        )
        return True


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
    stdout, stderr = await process.communicate()
    result = str(stdout.decode())
    if not result:
        autotests.logging.warn(f'can\'t run pyright test: {stderr.decode()}')
        return ''
    else:
        return result


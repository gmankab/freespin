import autotests.errors
import subprocess
import core.setup
import asyncio
import json


async def background() -> str:
    venv_python, _ = core.setup.get_venv_python_pip()
    cmd = [str(venv_python), '-m', 'pip', 'list', '--outdated', '--format=json']
    process = await asyncio.create_subprocess_shell(
        cmd=' '.join(cmd),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    stdout, _ = await process.communicate()
    unparsed = stdout.decode()
    start = unparsed.find('[')
    end = unparsed.rfind(']')
    return unparsed[start:end + 1]


async def parse_requirements_txt() -> dict:
    requirements: dict = {}
    with core.setup.requirements_txt.open('r') as file:
        for line in file:
            if '==' in line:
                package, version = line.strip().split('==')
                requirements[package] = version
    return requirements


async def get_result(
    outdated_str: str,
):
    requirements_dict = await parse_requirements_txt()
    outdated_list: list[dict] = json.loads(outdated_str)
    count = 0
    for package_dict in outdated_list:
        name = package_dict['name'].lower()
        if name in requirements_dict:
            count += 1
    if count:
        autotests.errors.warn(
            f'{count} packages are outdated, to update requirements.txt use --update_req_txt --install_req'
        )
    else:
        autotests.errors.passed('no oudtdated packages')


from pathlib import Path
import subprocess
import venv


app_name = 'freespin'
app_version = '23.0.0'
app_path = Path(
    __file__
).parent.parent.parent.resolve()
src_path = app_path / 'src'
transltions_path = src_path / 'translations'
venv_path = app_path / '.venv'
app_launcher_path = app_path / f'{app_name}.py'
requirements_txt = app_path / 'requirements.txt'
data_path = app_path / f'{app_name}_data'


def get_venv_python_pip() -> list[Path]:
    venv_bin = venv_path / 'bin'
    venv_scripts = venv_path / 'Scripts'
    if venv_bin.exists():
        venv_python = venv_bin / 'python'
        venv_pip = venv_bin / 'pip'
    elif venv_scripts.exists():
        venv_python = venv_scripts / 'python.exe'
        venv_pip = venv_scripts / 'pip.exe'
    else:
        raise FileNotFoundError()
    return [venv_python, venv_pip]


def install_requirements(
    force: bool = False,
):
    if venv_path.exists() and not force:
        print('dependencies already installed, skipping')
        print('remove .venv dir if you want to reinstall dependencies')
        return
    if not venv_path.exists():
        print('installing dependencies')
        venv.create(
            env_dir=venv_path,
            with_pip=True,
        )
    if venv_path.exists() and force:
        print('reinstralling dependencies')
    _, venv_pip = get_venv_python_pip()
    subprocess.run(
        [venv_pip, 'install', '-U', 'pip']
    )
    subprocess.run(
        [venv_pip, 'install', '-Ur', requirements_txt]
    )


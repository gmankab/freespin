#!/bin/env python

import src.core.setup
import subprocess
import platform
import sys
import os


def main():
    src.core.setup.app_launcher_path.chmod(0o755)
    src.core.setup.install_requirements()
    argv = sys.argv[1:]
    venv_python, _ = src.core.setup.get_venv_python_pip()
    command = [
        venv_python,
        '-u',
        str(src.core.setup.src_path),
        *argv,
    ]
    if platform.system() == 'Windows':
        result = subprocess.run(command)
        os._exit(result.returncode)
    else:
        os.execv(command[0], command)


if __name__ == '__main__':
    main()


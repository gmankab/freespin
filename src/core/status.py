from core import setup
import platform
import subprocess
import datetime
import shutil


class Status:
    def __init__(self) -> None:
        self.start_time = datetime.datetime.now()

    def get(self) -> dict[str, str]:
        return {
            'backend_version': setup.app_version,
            'bot_uptime': self.get_bot_uptime(),
            'system': platform.system(),
            'system_uptime': self.get_system_uptime(),
            'kernel': platform.release(),
            'python_ver:': platform.python_version(),
            'python_implementation': platform.python_implementation(),
            'commit': self.get_commit_hash(),
        }

    def get_bot_uptime(self) -> str:
        backend_uptime = datetime.datetime.now() - self.start_time
        days = backend_uptime.days
        seconds = backend_uptime.seconds
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        return f"{days} days, {hours} hours, {minutes} minutes"

    def get_system_uptime(self) -> str:
        try:
            uptime = subprocess.run(
                ['uptime'],
                text=True,
                capture_output=True,
            )
        except:
            return ''
        else:
            return uptime.stdout.strip()

    def get_commit_hash(self) -> str:
        git = shutil.which('git')
        if not git:
            return ''
        result = subprocess.run(
            [git, 'rev-parse', '--short', 'HEAD'],
            cwd=setup.app_path,
            capture_output=True,
            check=True,
            text=True,
        )
        return result.stdout.strip()

status = Status()

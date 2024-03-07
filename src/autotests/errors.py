from core.common import console
from pathlib import Path
import rich.console
import core.setup
import datetime


errors_path = core.setup.data_path / 'errors_path'


def generate_filename(
    dir_path: Path,
    max_files_in_dir: int = 30,
    extension: str = 'txt',
) -> Path:
    dir_path.mkdir(
        exist_ok = True,
        parents = True,
    )
    all_files = list(
        dir_path.iterdir()
    )
    all_files.sort()
    while len(
        all_files
    ) >= max_files_in_dir:
        all_files[0].unlink()
        all_files.remove(all_files[0])
    file_date = datetime.datetime.now().strftime('%Y.%m.%d_%H.%M')
    test_file_path = dir_path / file_date
    file_path = Path(
        f'{test_file_path}.{extension}'
    )
    index = 2
    while file_path.exists():
        file_path = Path(
            f'{test_file_path}_{index}.{extension}'
        )
        index += 1
    return file_path


def write_text(
    name: str,
    text: str,
) -> None:
    error_path = generate_filename(
        dir_path=errors_path
    )
    with error_path.open(
        'w',
        encoding='utf-8',
    ) as file:
        file.write(text)
    console.log(f'[red]\\[{name} error][/] {error_path}')


def write_error() -> None:
    error_path = generate_filename(
        dir_path=errors_path
    )
    with error_path.open(
        'w',
        encoding='utf-8',
    ) as file:
        file_console = rich.console.Console(
            width = 80,
            file = file,
        )
        for printer in file_console.print_exception, console.print_exception:
            printer(
                show_locals = False,
                suppress = [
                ],
            )
        error(str(error_path))


def error(
    text: str
):
    console.log(f'[red]\\[error][/] {text}')


def warn(
    text: str,
):
    console.log('[yellow]\\[WARN][/]', text)


def passed(
    text: str,
) -> None:
    console.log(
        f'[green]\\[pass][/] {text}',
    )


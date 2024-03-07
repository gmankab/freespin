import rich.console


console = rich.console.Console()


def yes_no(
    text: str,
) -> bool:
    console.print(
        text,
        end = '',
    )
    yes_no = input()
    if yes_no in [
        '',
        'Y',
        'y',
    ]:
        return True
    else:
        return False


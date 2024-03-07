import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'mode',
        choices=['bot', 'autotests'],
        help='run autotests',
    )
    args: argparse.Namespace = parser.parse_args()
    return args


from typing import Callable
from traceback import extract_tb
from sys import exc_info


def _success(err: Exception, lineno: int, line: str):
    print(
        f"{'─' * 64}",
        f"\033[1;46m{'| Success |':^64}\033[0m",
        f"{'─' * 64}",
        '',
        f"\033[36m<\033[31m{type(err).__name__}\033[0m {err}\033[36m>\033[0m",
        f"line {lineno}: \033[4m{line}\033[0m",
        '',
        f"{'─' * 64}",
        end='\n', sep='\n'
    )


def _failed():
    print(
        f"{'─' * 64}",
        f"\033[1;41m{'| Failed |':^64}\033[0m",
        f"{'─' * 64}",
        end='\n', sep='\n'
    )


def check(func: Callable[[], None]):
    """虽然叫check但是还顺带包含了run的功能"""
    try:
        func()
    except Exception as err:
        *_, traceback = exc_info()
        for tb in reversed(extract_tb(traceback)):
            if tb.name == 'raise_me':
                _success(err, tb.lineno, tb.line)
                return
            elif tb.name == 'answer':
                _failed()
                return

    _failed()


if __name__ == '__main__':
    _success(ValueError('This is an example error str.'), 1, 'asset 1 == 2')
    # _failed()
    raise ValueError('This is an example error str.')

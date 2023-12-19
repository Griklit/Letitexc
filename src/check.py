from typing import Callable
from traceback import extract_tb
from sys import exc_info


def check(func: Callable[[], None]):
    """虽然叫check但是还顺带包含了run的功能"""
    try:
        func()
    except Exception as err:
        *_, traceback = exc_info()
        for tb in reversed(extract_tb(traceback)):
            if tb.name == 'raise_me':
                print(f"success! \n"
                      f"Exception:\n"
                      f"  {err}\n"
                      f"  at line {tb.lineno}: {tb.line}")
                return
            elif tb.name == 'answer':
                print(f"failed!")
                return

    print('failed!')

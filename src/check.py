from typing import Callable
from traceback import extract_tb
from sys import exc_info


def check(func: Callable[[], None]):
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
                break
            elif tb.name == 'answer':
                print(f"failed!")
                break
        else:
            print('failed!')

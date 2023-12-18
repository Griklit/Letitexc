from typing import Callable
from traceback import extract_tb
from sys import exc_info


def check(func: Callable[[], None]):
    try:
        func()
    except Exception as err:
        *_, traceback = exc_info()
        # last_tb = extract_tb(traceback)[-1]
        # if last_tb.name == 'raise_me':
        #     print(f"success! \n"
        #           f"Exception:\n"
        #           f"  {err}\n"
        #           f"  at line {last_tb.lineno}: {last_tb.line}")
        #     return
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

"""
难度: 4
"""
from src import check


def raise_me(alpha: dict):
    import time
    if type(alpha) is dict:
        if 'key' in alpha:
            time.sleep(0.1)
            return alpha['key']


@check
def answer():
    # write your answer here.
    raise_me({'key': 'value'})

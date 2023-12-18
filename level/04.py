"""
难度: 2
"""
from src import check


def raise_me(alpha: bytes):
    if type(alpha) is bytes:
        return alpha.decode()


@check
def answer():
    # write your answer here.
    raise_me(b'hello')

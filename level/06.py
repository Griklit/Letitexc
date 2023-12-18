"""
难度: 2
"""
from src import check


def raise_me(alpha):
    print(alpha)


@check
def answer():
    # write your answer here.
    raise_me('hello')

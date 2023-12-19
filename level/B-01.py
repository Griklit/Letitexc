"""
难度: 1 未完成
"""
from src import check


def raise_me():
    x = []
    for _ in range(10):
        y = yield x
        x.append(y)


@check
def answer():
    # write your answer here.
    for _ in raise_me():
        ...

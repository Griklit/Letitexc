from src import check


def raise_me(alpha: int, beta: int):
    if not (type(alpha) is int and type(beta) is int):
        return
    if alpha == beta ** 2:
        assert alpha is beta ** 2


@check
def answer():
    # write your answer here.
    raise_me(16, 4)

from src import check


def raise_me(alpha):
    if alpha == 2:
        assert alpha == 2


@check
def answer():
    # write your answer here.
    raise_me(...)

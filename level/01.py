from src import check


def raise_me(alpha):
    beta = alpha + 1
    return beta


@check
def answer():
    # write your answer here.
    raise_me(1)

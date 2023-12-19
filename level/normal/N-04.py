from src import check


def raise_me(alpha):
    if hasattr(alpha, 'hello'):
        return alpha.hello


@check
def answer():
    # write your answer here.
    raise_me(...)

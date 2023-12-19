from src import check


def raise_me(alpha):
    if hasattr(alpha, 'hello'):
        alpha.hello = 'world'


@check
def answer():
    # write your answer here.
    raise_me(...)

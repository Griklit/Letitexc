from src import check


def raise_me(*args):
    return set(args)


@check
def answer():
    # write your answer here.
    raise_me(...)

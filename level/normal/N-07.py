from src import check


def raise_me(alpha: list):
    if not type(alpha) is list:
        return
    if len(alpha) < 1:
        return
    assert alpha != alpha[0]


@check
def answer():
    # write your answer here.
    raise_me(...)

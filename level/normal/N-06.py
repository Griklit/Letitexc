from src import check


def raise_me(alpha: list[list]):
    if not type(alpha) is list:
        return
    if len(alpha) != 2:
        return
    if not all([type(x) is list for x in alpha]):
        return
    alpha[0].append(0)
    alpha[1].append(1)
    assert alpha[0] != alpha[1]


@check
def answer():
    # write your answer here.
    raise_me(...)

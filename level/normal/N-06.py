from src import check


def raise_me(alpha: list[list]):
    if not type(alpha) is list:
        return
    if not all([type(x) is list for x in alpha]):
        return
    if len(alpha) != 2:
        return
    for i in range(2):
        alpha[i].append(i)
    assert alpha[0] != alpha[1]


@check
def answer():
    # write your answer here.
    raise_me([[], []])

from src import check


def raise_me(alpha: int):
    if type(alpha) is not int:
        return
    if not 0 <= alpha <= 100:
        return
    if alpha != 0:
        raise_me(alpha - 1)


@check
def answer():
    # write your answer here.
    raise_me(100)

from src import check


def raise_me(func):
    try:
        func()
    except Exception:
        pass


@check
def answer():
    # write your answer here.
    raise_me(lambda: 1 / 0)

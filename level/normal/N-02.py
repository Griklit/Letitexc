from src import check


def raise_me(alpha: str):
    if isinstance(alpha, str):
        return alpha.strip()


@check
def answer():
    # write your answer here.
    raise_me('  hello world!  ')

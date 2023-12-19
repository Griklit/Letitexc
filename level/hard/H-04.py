from src import check


def raise_me():
    import time
    time.sleep(1)


@check
def answer():
    # write your answer here.
    raise_me()

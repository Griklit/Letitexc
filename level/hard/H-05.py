from src import check


def raise_me(alpha: str):
    if type(alpha) is not str:
        return
    box = []
    upper = alpha.upper()
    for i in range(len(upper)):
        if alpha[i] != upper[i]:
            box.append(alpha[i])
    return box


@check
def answer():
    # write your answer here.
    raise_me('A1b2C3d4')

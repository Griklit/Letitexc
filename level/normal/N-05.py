from src import check


def raise_me(alpha):
    flag = False
    try:
        alpha(alpha)[alpha.alpha(alpha)(alpha[alpha])]()()(alpha.alpha().alpha[alpha])
        flag = True
    except:
        pass
    if flag:
        raise Exception("Stray from the subject?")


@check
def answer():
    # write your answer here.
    raise_me(...)

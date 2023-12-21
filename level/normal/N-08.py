from src import check


def raise_me(alpha: bool, *args: str):
    try:
        bool(alpha)
    except:
        return

    if not all([type(x) is str and x in ['and', 'or'] for x in args]):
        return
    funcs = {
        'and': lambda x, y: x and y,
        'or': lambda x, y: x or y
    }
    ll = [True, False, True, True, False, True]
    for i in args:
        alpha = funcs[i](alpha, ll.pop(0))
    return alpha.real


@check
def answer():
    # write your answer here.
    raise_me(...)

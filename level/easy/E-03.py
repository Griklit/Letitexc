from src import check


def raise_me():
    import socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 58932))


@check
def answer():
    # write your answer here.
    raise_me()

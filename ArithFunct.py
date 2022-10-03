def ADD(x, y):
    funcs = {0: x if callable(x) else lambda _: x, 1: y if callable(y) else lambda _: y}
    return lambda t: funcs[0](t) + funcs[1](t)


def SUB(x, y):
    funcs = {0: x if callable(x) else lambda _: x, 1: y if callable(y) else lambda _: y}
    return lambda t: funcs[0](t) - funcs[1](t)


def MUL(x, y):
    funcs = {0: x if callable(x) else lambda _: x, 1: y if callable(y) else lambda _: y}
    return lambda t: funcs[0](t) * funcs[1](t)


def DIV(x, y):
    funcs = {0: x if callable(x) else lambda _: x, 1: y if callable(y) else lambda _: y}
    return lambda t: funcs[0](t) / funcs[1](t)

from sys import stdin


def statcounter():
    statcounter.buff = {}
    func = yield statcounter.buff

    while True:
        statcounter.buff[func] = 0

        def wrapped(f):
            def inner(*args, **kwargs):
                statcounter.buff[f] += 1
                return f(*args, **kwargs)

            return inner

        func = yield wrapped(func)


if __name__ == '__main__':
    exec(stdin.read())

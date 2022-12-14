import numbers, sys

class fixed(type):

    def __new__(mcs, name, bases, classdict, **kwargs):
        n = kwargs.get("ndigits", 3)

        def wrapped(func):
            def inner(*args, **kwargs):
                res = func(*args, **kwargs)
                if isinstance(res, numbers.Real):
                    return round(res, n)
                return res

            return inner

        new_cls_dct = {
            attr: wrapped(val) if callable(val) else val for attr, val in classdict.items()
        }

        return super().__new__(mcs, name, bases, new_cls_dct)


if __name__ == '__main__':
    exec(sys.stdin.read())
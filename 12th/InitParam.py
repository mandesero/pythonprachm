import sys
from inspect import get_annotations


class init(type):

    def __new__(mcs, name, bases, classdict, **kwargs):

        def wrapped(func):
            def inner(*args, **kwargs):

                defs = []

                for attr, tpy in get_annotations(func).items():

                    try:
                        defs.append(tpy())
                    except Exception:
                        defs.append(None)

                try:
                    t = len(func.__defaults__)
                    defs = defs[:-t]
                    defs.extend(func.__defaults__)
                except:
                    pass


                # defs.extend(func.__defaults__)

                func.__defaults__ = tuple(defs)

                return func(*args, **kwargs)

            return inner

        new_cls_dct = {
            attr: wrapped(val) if callable(val) else val for attr, val in classdict.items()
        }

        return super().__new__(mcs, name, bases, new_cls_dct)


if __name__ == '__main__':
    exec(sys.stdin.read())

from sys import stdin


def sloter(fields, default):
    class Wrapped:
        __slots__ = fields

        def __init__(self):
            for field in self.__slots__:
                setattr(self, field, default)

        def __iter__(self):
            return (getattr(self, obj_name) for obj_name in self.__slots__)

        def __delattr__(self, item):
            setattr(self, item, default)

    return Wrapped


if __name__ == '__main__':
    exec(stdin.read())

import asyncio
import sys
from collections import defaultdict


class NotifyEvent(asyncio.Event):
    def __init__(self):
        super().__init__()
        self.isFirst = True
        self.name = None

        self.event = asyncio.Event()
        self.event.set()

    def set(self, name=None):
        self.name = name

        self.event.set()

        if self.isFirst:
            self.isFirst = False
        else:
            self.clear()

        super().set()

    async def wait(self):
        await self.event.wait()
        await super().wait()
        self.event.clear()
        return self.name


async def task(name, event, dct=defaultdict(int)):
    while True:
        ev_name = await event.wait()
        if ev_name is None:
            break
        if ev_name == name:
            dct[ev_name] += 1
            print(f"{name}: {dct[ev_name]} / {sum(dct.values()) - dct[ev_name]}")


if __name__ == '__main__':
    exec(sys.stdin.read())

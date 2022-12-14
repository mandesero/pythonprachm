import asyncio
import sys
from collections import deque


class FilterQueue(asyncio.Queue):
    def __init__(self, *args):
        super().__init__(*args)
        self.window = None

    async def put(self, item):
        await super().put(item)
        self.window = self._queue[0] if self.qsize() else None

    def __contains__(self, flt):
        for elem in self._queue:
            if flt(elem):
                return True
        return False

    def later(self):
        if self.qsize():
            self.put_nowait(super().get_nowait())
            self.window = self._queue[0] if self.qsize() else None
            return
        raise asyncio.QueueEmpty

    async def get(self, flt=None):

        if flt is None:
            head = await super().get()
            self.window = self._queue[0] if self.qsize() else None
            return head

        for i, elem in enumerate(self._queue):
            if flt(elem):
                break
        else:
            elem = await super().get()
            self.window = self._queue[0] if self.qsize() else None
            return elem

        self._queue = deque(list(self._queue)[i:] + list(self._queue)[:i])
        elem = await super().get()
        self.window = self._queue[0] if self.qsize() else None
        return elem


exec(sys.stdin.read())

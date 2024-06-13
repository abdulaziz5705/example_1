
import time


class Range:
    def __init__(self, start, stop=None, step=1):
        if stop is None:
            self.stop = start
            self.start = -step
            self.step = step
        else:
            self.start = start - step
            self.stop = stop
            self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        time.sleep(1)
        self.start += self.step
        if self.start >= self.stop:
            raise StopIteration
        return self.start


for i in Range(0, 50, 2.5):
    print(i)

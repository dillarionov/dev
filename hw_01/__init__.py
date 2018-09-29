import time
from functools import wraps


class ObjIterator:
    """Iterates sequence of ints in range (1, 4)
    """

    def __init__(self):
        self.i = 1

    def __str__(self):
        return 'abc'

    def __iter__(self):
        return self

    def __next__(self):
        while self.i < 4:
            i = self.i
            self.i += 1
            return i

        raise StopIteration()


def even_nums(n=100):
    """Generates sequence of evens in range (2, n + 1)
    """
    for i in range(2, n + 1, 2):  # include n
        yield i


def print_exec_duration(f):
    """Decorator prints execution time for provided function `f`
    """

    @wraps(f)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        f(*args, **kwargs)
        delta = time.time() - t1
        print(delta)

    return wrapper

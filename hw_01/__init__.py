import time
from functools import wraps
from collections import namedtuple, deque, Counter


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


class Swapper():
    def swap1(self, x=1):
        """Because False == 0, True == 1 in Python
        """
        return (1, 2)[x == 1]

    def swap2(self, x=1):
        """Element in tuple by decremented index
        """
        return (2, 1)[x - 1]

    def swap3(self, x=1):
        """By dict key
        """
        d = {
            1: 2,
            2: 1,
        }
        return d[x]

    def swap4(self, x=1):
        """While loop may have else
        """
        while x <= 1:
            return 2
        else:
            return 1

    def swap5(self, x=1):
        """String also has indexes
        """
        return int("21"[x - 1])

    def swap6(self, x=1):
        """Sets may include x, or may not
        """
        while x in {1}:
            return 2
        return 1

    def swap7(self, x=1):
        """Like dicts, but with named tuples
        """
        T = namedtuple('Foo', 'v1 v2')
        t = T(v1='2', v2='1')
        return int(getattr(t, 'v%i' % x))

    def swap8(self, x=1):
        """Linked lists like deque can be rotated and popped
        """
        d = deque([0, 1, 2])
        d.rotate(x)
        return d.popleft()

    def swap9(self, x=1):
        """Count occurrences with built-in Counter
        """
        counter = Counter((1, 1, 2))
        return counter[x]

    def swap10(self, x=1):
        """Dicts may have default values if key not found
        """
        d = {1: 2}
        return d.get(x, 1)

    def swap11(self, x=1):
        """The same as prev, but with Exception
        """
        d = {1: 2}
        try:
            return d[x]
        except:  # catch all exceptions
            return 1

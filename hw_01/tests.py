import unittest
import sys
import time

from io import StringIO
from collections import deque

from hw_01 import (
    ObjIterator,
    even_nums,
    print_exec_duration,
    Swapper,
)


class Capturing(list):
    """Context manager to catch stdout into list.

    Usage:
        with Capturing() as output:
            print('foo')
        output  " ['foo']
    """

    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio
        sys.stdout = self._stdout


class TestIterator(unittest.TestCase):

    def setUp(self):
        self.obj_iterator = ObjIterator()

    def test_name(self):
        """Should blueprint self name as 'abc'
        """
        with Capturing() as output:
            print(self.obj_iterator)

        self.assertEqual(output[0], 'abc')

    def test_iter(self):
        """Should generate seq (1,2,3,)
        """
        d = deque()

        for i in self.obj_iterator:
            d.append(i)

        self.assertEqual(d, deque((1, 2, 3)))


class TestEvenNums(unittest.TestCase):

    def test_even_nums(self):
        """Should generate even seq,
            less or equal to N
            """
        for i in even_nums(100):
            self.assertEqual(i % 2, 0)
            self.assertLessEqual(i, 100)


class TestPrintExecDuration(unittest.TestCase):
    @print_exec_duration
    def sleep(self, sec=1):
        """Stops execution flow for `sec` seconds
        """
        time.sleep(sec)

    def test_exec_duratoon_decorator(self):
        """Should print execution time,
        which is greater or equal to function execution time
        """
        for i in (1, 2, 3):  # should pass various execution time
            with Capturing() as output:
                self.sleep(i)
            self.assertEqual(len(output), 1)
            self.assertGreaterEqual(float(output[0]), i)


class TestSwapper(unittest.TestCase):
    def setUp(self):
        self.swapper = Swapper()

    def test_swap(self):
        # gather swappers
        fs = [getattr(self.swapper, 'swap%i' % i) for i in range(1, 12)]
        for f in fs:
            self.assertEqual(f(1), 2)
            self.assertEqual(f(2), 1)


if __name__ == '__main__':
    unittest.main()

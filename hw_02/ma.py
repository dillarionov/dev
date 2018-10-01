from base import First, Second, Parent, MyError


class A(First):
    def __init__(self):
        self.i = 3
        # self.__isSecond = 0

    def fnc(self, x=2):
        if x == 7:
            raise MyError
        return x * 2 * 3

    def isFirst(self):
        return 1

    @property
    def isSecond(self):
        # return self.__isSecond
        return 0

    @isSecond.setter
    def isSecond(self, isSecond):
        raise AttributeError

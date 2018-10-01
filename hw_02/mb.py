from base import First, Second, Parent


class B(Second):
    def __init__(self, n=5):
        self.n = n
        self.isSecond = 1

    def fnc(self, x=10, y=4):
        return x * y * 5

    def isFirst(self):
        return 0

class Parent():
    def __init__(self):
        pass


class First(Parent):
    def __init__(self):
        pass


class Second(Parent):
    def __init__(self):
        pass


class MyError(Exception):
    def __str__(self):
        return 'Error text'

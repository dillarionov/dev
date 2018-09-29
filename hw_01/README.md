

# Тесты

```sh
python -m unittest discover hw_01 "*tests.py"
```

Необходим: `Python 3.6.5`.

## Задание 1

Создать объект с подмененой итерацией:

1. `obj = ObjIterator()` - инициализация объекта.
2. `print(obj)` должен выдавать `abc`.
3. Перебор for i in obj должен выдавать 1, 2, 3.

## Задание 2

1. Создать функцию `even_nums` - генератор четных чисел.
2. `for i in even_nums(100)` должен выдавать 2, 4, 6, и т.д. до 100.

## Задание 3

Создать такой декоратор который делал бы print(exec_func_duration)  - времени выполнения функции которую он оборачивает 

[Литература](https://anandology.com/python-practice-book/iterators.html#generators).

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from threading import Thread
import math

"""
С использованием многопоточности для заданного значения найти сумму ряда с точностью члена ряда по абсолютному
значению 1e-07 и произвести сравнение полученной суммы с контрольным значением функции для двух бесконечных
рядов.
"""


def func_s(n, x=-0.7):
    result = (n + 1) * math.pow(x, n)
    return result


def func_y(x=-0.7):
    result = 1/(math.pow((1 - x), 2))
    return result


def summ(i, thead, flag):
    pre = 0
    s = 0
    n = 0
    e = 1e-07
    curr = func_s(n)
    s += curr
    n += 1
    print(f"Цикл № {i}. Поток {thead}")
    while abs(curr - pre) > e:
        pre = curr
        curr = func_s(n)
        n += 1
        s += curr
        if flag is True:
            print(f"Результат суммы бесконечного ряда {s}")
    return s


def compare(x, y):
    result = x - y
    print(f"Результат сравнения {result}")


def sequential(calc, thead):
    print(f"Запускаем поток № {thead}")
    for i in range(calc):
        summ(i, thead, True)
    print(f"{calc} циклов вычислений закончены. Поток № {thead}")


def threaded(theads, calc):
    threads = []
    for thead in range(theads):
        t = Thread(target=sequential, args=(calc, thead), daemon=True)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()


if __name__ == '__main__':
    threaded(4, 20)
    compare(summ(0, 0, False), func_y())

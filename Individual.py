#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""""
Напишите функцию, принимающую произвольное количество аргументов, и возвращающую
требуемое значение. Если функции передается пустой список аргументов, то она должна
возвращать значение None . Номер варианта определяется по согласованию с преподавателем.
В процессе решения не использовать преобразования конструкции *args в список или иную
структуру данных.

Произведение аргументов, расположенных между первым и вторым нулевыми аргументами.
Произведение вычислить функцией. 
"""""

def proiz(*args):
    p = 1
    for i in args:
        p *= i
    return p


def f(*args):
    if args:
        zero_f = 0
        zero_s = 0
        ok = True
        for index, item in enumerate(args):
            if item == 0 and ok:
                zero_f = index
                ok = False

            elif item == 0 and index > zero_f:
                zero_s = index
        return proiz(*args[zero_f + 1: zero_s])

    else:
        return None


if __name__ == '__main__':
    lst = list(map(int, input().split(' ')))
    print(f(*lst))
"Напишите функцию, принимающую произвольное количество аргументов, и возвращающую"
"требуемое значение. Если функции передается пустой список аргументов, то она должна"
"возвращать значение None . Номер варианта определяется по согласованию с преподавателем."
"В процессе решения не использовать преобразования конструкции *args в список или иную"
"структуру данных."

"Произведение аргументов, расположенных между первым и вторым нулевыми аргументами."

def f(*args):
    p = 1
    if len(args) == 0:
        return None
    var = args[args.index(0) + 1: args.index(0, args.index(0) + 1)]
    for i in var:
        p *= i
    return p

if __name__ == '__main__':
    lst = list(map(int, input().split(' ')))
    print (f(*lst))
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
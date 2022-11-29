def info(**args):
    print("Data type of argument: ",type(args))

    for key, value in args.items():
        print("{} is {}".format(key, value))

if __name__ == '__main__':
    info(Firstname="Nikita", Lastname="Nazarov", Age=19, Phone=9614624711)
    info(Firstname="Bogdan", Lastname="Harchenko", Email="harchenkobo2003@gmail.com", Country="Russian Federation", Age=19, Phone=9628535082)
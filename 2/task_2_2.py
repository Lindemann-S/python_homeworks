

def my_enumerate(xs, start_value=0):
    return zip(range(start_value, len(xs) + start_value), xs)


def which(func, xs):
    result = []
    for i, element in zip(range(len(xs)), xs):
        if func(element):
            result.append(i)
    return result


def my_all(func, xs):
    for element in xs:
        if not func(element):
            return False
    return True


def my_any(func, xs):
    for element in xs:
        if func(element):
            return True
    return False


def main():
    # print(list(my_enumerate("abcd", 1)))
    # print(which(lambda x: x % 2 == 0, [4, 8, 15]))
    # print(my_all(lambda x: x % 2 == 0, [4, 8, 15]))
    print(my_any(lambda x: x % 2 == 0, [4, 8, 15]))


if __name__ == "__main__":
    main()

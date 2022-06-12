
def compose(*funcs):
    def create_res(data):
        for func in funcs[::-1]:
            data = func(data)
        return data
    return create_res


def const(value):
    def const_functions(*_, **_kwargs):
        return value
    return const_functions


def flip(func):
    def create_func(*args, **kwargs):
        return func(*args[::-1], **kwargs)
    return create_func


def curry(function, *args, **kwargs):
    def create_func(*args1, **kwargs1):
        return function(*args, *args1, **(kwargs | kwargs1))
    return create_func


def main():
    # print("Compose function test:")
    # f = compose(lambda x: x**2, lambda x: x + 1)
    # print(f(2))
    # print("Const function test:")
    # val = const(42)
    # print(val())
    # print(val(range(4), range(2), foo="bar"))
    print("Flip function test:")
    f2 = flip(map)
    print(list(f2(range(5), range(0, 10, 2), lambda x, y: x**y)))
    # print("Curry function test:")
    # def my_pow(a, p):
    #     return a**p
    # f3 = curry(my_pow, 10)
    # print(f3(3))
    # square = curry(my_pow, p=2)
    # print(square(42))


if __name__ == "__main__":
    main()

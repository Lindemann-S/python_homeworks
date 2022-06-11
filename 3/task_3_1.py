import functools
import sys

DEBUG = True


# def update_wrapper(wrapped, wrapper):
#     for attr in ["__name__", "__doc__", "__module__"]:
#         setattr(wrapper, attr, getattr(wrapped, attr))
#     return wrapper
#
#
# def wraps(wrapped):
#     def deco(wrapper):
#         update_wrapper(wrapped, wrapper)
#         return wrapper
#
#     return deco


def trace(func=None, *, stream=sys.stdout):
    if func is None:
        return functools.partial(trace, stream=stream)

    if not DEBUG:
        return func

    @functools.wraps(func)
    def inner(*args, **kwargs):
        call = ", ".join([str(x) for x in args] + [f"{k}={w}" for k, w in kwargs.items()])
        print(f"{func.__name__}({call}) = ...", file=stream)
        ret = func(*args, **kwargs)
        print(f"{func.__name__}({call}) = {ret}", file=stream)
        return ret

    return inner


@trace
def union(*args):
    res = set()
    for arg in args:
        res |= arg
    return res


def digits(num):
    if num == 0:
        return [0]
    result = []
    while num != 0:
        number = num % 10
        num //= 10
        result.append(number)
    return result[::-1]


def lcm(x, y, *args):
    def gcd(a, b):
        while b:
            a %= b
            a, b = b, a
        return a
    result = x * y // gcd(x, y)
    return result if not args else lcm(result, *args)


def compose(*funcs):
    def initial(data):
        for func in funcs[::-1]:
            data = func(data)
        return data

    return initial


def main():
    union({1, 2, 3}, {10}, {2, 6})
    # print(digits(0))
    # print(lcm(*range(2, 40, 8)))
    # print(lcm(100500, 42))


if __name__ == "__main__":
    main()

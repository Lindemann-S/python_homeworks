import functools

DEBUG = False


def trace_if(predicate):
    def decorator(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            call = None
            is_valid = predicate(*args, **kwargs)
            if is_valid:
                call = ", ".join([str(x) for x in args] + [f"{k}={w}" for k, w in kwargs.items()])
                print(f"{func.__name__}({call}) = ...")
            ret = func(*args, **kwargs)
            if is_valid:
                print(f"{func.__name__}({call}) = {ret}")
            return ret

        return inner
    return decorator


def n_times(count=1):
    def decorator(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            for _ in range(count):
                func(*args, **kwargs)

        return inner
    return decorator


def n_times1(count=1, func=None):
    if func is None:
        return functools.partial(n_times1, count)

    @functools.wraps(func)
    def inner(*args, **kwargs):
        for _ in range(count):
            func(*args, **kwargs)

    return inner


def once(func):
    called = False
    cache = None

    @functools.wraps(func)
    def inner(*args, **kwargs):
        nonlocal called
        nonlocal cache
        if not called:
            called = True
            cache = func(*args, **kwargs)
        return cache

    return inner


@once
def initialize_settings():
    print("Settings initialized.")
    return {"token": 42}


@n_times1()
def write_code1():
    print("needed every day1!")


@n_times()
def write_code():
    print("needed every day!")


@trace_if(lambda x, y, **kwargs: kwargs.get("integral"))
def div(x, y, integral=False):
    return x // y if integral else x / y


def main():
    # print(initialize_settings())
    # print(initialize_settings())
    # write_code1()
    print(div(4, 2))
    print(div(4, 2, integral=True))


if __name__ == "__main__":
    main()

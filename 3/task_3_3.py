import functools


def remove_mult_calls(calls):
    if len(calls) == 1:
        return calls
    result = []
    already_called = set()
    for call in calls:
        if call not in already_called:
            result.append(call)
            already_called.add(call)
    return result


def project():
    tasks = {}
    full_dep_list = {}

    def register(func=None, *, depends_on=None):
        depends = {}
        dep_list = []

        if func is None:
            return functools.partial(register, depends_on=depends_on)

        nonlocal tasks
        tasks[func.__name__] = func

        @functools.wraps(func)
        def inner():
            for task in full_dep_list[func.__name__]:
                tasks[task]()

        inner.get_dependencies = lambda: list(*depends.values())

        if depends_on:
            depends[func.__name__] = depends_on
            for name in depends_on:
                assert tasks[name], f"function named {name} doesn't exist"
                dep_list += full_dep_list[name]
        else:
            depends[func.__name__] = []
        dep_list.append(func.__name__)
        full_dep_list[func.__name__] = remove_mult_calls(dep_list)

        return inner

    register.get_all = lambda: list(tasks.keys())

    return register


reg = project()


# @reg
# def do_something():
#     print("doing something")
#
#
# @reg(depends_on=["do_something"])
# def do_other_thing():
#     print("doing other thing")


@reg
def task_a():
    print("task_a")


@reg(depends_on=["task_a"])
def task_b():
    print("task_b")


@reg(depends_on=["task_a"])
def task_c():
    print("task_c")


@reg(depends_on=["task_b", "task_c"])
def task_d():
    print("task_d")


def main():
    # print(reg.get_all())
    # do_something()
    # do_other_thing()
    # print(do_something.get_dependencies())
    # print(do_other_thing.get_dependencies())
    task_d()
    print(task_d.get_dependencies())
    # print(reg.get_all())


if __name__ == "__main__":
    main()

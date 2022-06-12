OK, ERROR = "OK", "ERROR"


def char(ch):
    def inner(string):
        if not string:
            return ERROR, "eof", string
        if string[0] != ch:
            return ERROR, f"expected {ch} got `{string[0]}`", string
        return OK, ch, string[1:]
    return inner


def any_of(check_string):
    def parser(string):
        if not string:
            return ERROR, "eof", string
        if string[0] in check_string:
            return OK, string[0], string[1:]
        else:
            return ERROR, f"expected any of {check_string} got {string[0]}", string
    return parser


def chain(*parsers):
    def func(string):
        result = []
        if not string:
            return ERROR, "eof", string
        for parser in parsers:
            tag, res, leftover = parser(string)
            if tag == ERROR:
                return tag, res, leftover
            string = leftover
            result.append(res)
        return OK, result, string
    return func


def choice(*parsers):
    def func(string):
        if not string:
            return ERROR, "eof", string
        for parser in parsers:
            tag, res, leftover = parser(string)
            if tag == OK:
                return tag, res, leftover
        return ERROR, "none matched", string
    return func


def many(parser):
    def func(string):
        result = []
        while string:
            tag, res, leftover = parser(string)
            if tag == ERROR:
                break
            string = leftover
            result.append(res)
        return OK, result, string
    return func


def many1(parser):
    def func(string):
        if not string:
            return ERROR, "eof", string
        tag, res1, leftover = parser(string)
        if tag == ERROR:
            return tag, res1, leftover
        many_parser = many(parser)
        tag, res2, leftover = many_parser(leftover)
        return tag, [res1, *res2], leftover
    return func


def transform(p, f):
    def inner(string):
        tag, res, leftover = p(string)
        return tag, f(res) if tag == OK else res, leftover
    return inner


def sep_by(p, separator):
    def func(string):
        if not string:
            return ERROR, "eof", string
        tag, res1, leftover = p(string)
        if tag == ERROR:
            return tag, res1, leftover
        many_parser = many(chain(separator, p))
        transform_many_parser = transform(many_parser, lambda xs: [x for _, x in xs])
        tag, res2, leftover = transform_many_parser(leftover)
        if tag == ERROR:
            return tag, res2, leftover
        return tag, [res1, *res2], leftover
    return func


def parse(parser, string):
    tag, res, leftover = parser(string)
    assert not leftover, (tag, res, leftover)
    return res


def parsing():
    lparen, rparen = char("("), char(")")
    ws = many1(any_of(" \r\n\t"))
    number = transform(
        many1(any_of("1234567890")),
        lambda digits: int("".join(digits))
    )
    op = any_of("+-*/")

    def sexp(string):
        args = sep_by(choice(number, sexp), ws)

        # Уберём лишние None из результата chain.
        p = chain(lparen, op, ws, args, rparen)
        p = transform(p, lambda res: (res[1], res[3]))
        return p(string)
    result = parse(sexp, "(+ 42 (* 2 4))")
    print(result)
    return result


def calculate(op, val):
    if op == "+":
        return val[0] + val[1]
    elif op == "*":
        return val[0] * val[1]
    elif op == "-":
        return val[0] - val[1]
    elif op == "/":
        return val[0] / val[1]


def eval_exp(expression):
    op, xs = expression
    assert op in ['*', '+', '-', '/'], "non-existent operator"
    operands = []
    for el in xs:
        is_nested_expression = type(el) is tuple
        if is_nested_expression:
            operands.append(eval_exp(el))
        else:
            operands.append(el)
    return calculate(op, operands)


def main():
    # p = any_of("()")
    # print(p("[]"))
    # p = chain(char("("), char(")"))
    # print(p(")"))
    # p = choice(char("."), char("!"))
    # print(p("&"))
    # p = many(char("."))
    # print(p("...?!"))
    # p = many1(char("."))
    # print(p(".!"))
    # p = sep_by1(any_of("1234567890"), char(","))
    # print(p("1,2,3"))
    res = parsing()
    print(eval_exp(res))


if __name__ == "__main__":
    main()

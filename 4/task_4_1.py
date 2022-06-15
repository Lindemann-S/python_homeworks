

def capwords(string, sep=" "):
    if sep == " ":
        split_string = string.split()
    else:
        split_string = string.split(sep)
    capitalize_split_string = [string.capitalize() for string in split_string]
    result = sep.join(capitalize_split_string)
    return result


def cut_suffix(string, suffix):
    if string.endswith(suffix):
        return string[0:len(string) - len(suffix)]
    return string


def boxed(string, fill="", pad=2):
    str_len = len(string)
    box_width = str_len + pad * 2 + 2
    width_side = fill * box_width + "\n"
    center = (string.center(str_len + 2)).center(box_width, fill) + "\n"
    return width_side + center + width_side


def find_all(string, sub_string):
    result = []
    pos = 0
    sub_string_len = len(sub_string)
    while True:
        pos = string.find(sub_string, pos)
        if pos == -1:
            break
        result.append(pos)
        if sub_string_len == 1:
            pos += sub_string_len
        else:
            pos += sub_string_len - 1
    return result


def common_prefix(*args):
    n_strings = len(args)
    min_len = float('inf')
    index_min_len = 0
    for string, index in zip(args, range(n_strings)):
        str_len = len(string)
        if min_len > str_len:
            min_len = str_len
            index_min_len = index
    pref = args[index_min_len]
    while pref:
        for string, index in zip(args, range(n_strings)):
            if not string.startswith(pref):
                break
            if index == n_strings - 1:
                return pref
        pref = pref[0:len(pref) - 1]
    return ""


def main():
    # print(capwords("foo,bar boo,", sep=","))
    # print(capwords(" foo  \nbar\n"))
    # print(capwords("foo,bar boo,",  sep=""))
    # print(cut_suffix("foobar", "bar"))
    # print(cut_suffix("foobar", "boo"))
    # print(boxed("Hello world", fill="*", pad=2))
    # print(boxed("Fishy", fill="#", pad=1))
    # print(find_all("abracadabra", "a"))
    # print(find_all("arara", "ara"))
    print(common_prefix("abra", "abracadabra", "abrasive"))
    print(common_prefix("abra", "foobar"))


if __name__ == "__main__":
    main()

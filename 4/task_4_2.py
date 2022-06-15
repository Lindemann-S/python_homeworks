import gzip
import bz2


def parse_shebang(path):
    with open(path) as file:
        script = file.read()
    if script.startswith("#!"):
        return script.strip("#! '\n'")
    return None


def reader(path, mode="rt", encoding="UTF-8"):
    if path.endswith(".txt"):
        return open(path, mode=mode, encoding=encoding)
    if path.endswith(".gz"):
        return gzip.open(path, mode=mode, encoding=encoding)
    if path.endswith(".bz2"):
        return bz2.open(path)


def main():
    print(reader("sources/example.txt"))
    print(reader("sources/example.txt.gz", mode="rt", encoding="ascii"))
    print(reader("sources/example.txt.bz2", mode="wb"))
    print(parse_shebang("sources/script.py"))
    print(parse_shebang("sources/script.sh"))


if __name__ == "__main__":
    main()

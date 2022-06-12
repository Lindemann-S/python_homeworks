from collections import Counter
from itertools import combinations


def hamming(seq1, seq2):
    return sum([x != y for x, y in zip(seq1, seq2)])


def kmers(seq, k):
    dictionary = Counter()
    for i in range(len(seq) - k + 1):
        sub_str = seq[i:i+k]
        dictionary[sub_str] += 1
    return dictionary


def distance1(seq1, seq2, k=2):
    dict1 = kmers(seq1, k)
    dict2 = kmers(seq2, k)
    result_list = [abs(dict1.get(key, 0) - dict2.get(key, 0)) for key in dict1 | dict2]
    return sum(result_list)
        

def hba1(path, distance):
    file = open(path)
    lines = file.readlines()
    max_index = len(lines)
    dictionary = {}
    indexes = [x for x in range(max_index)]
    pair_indexes = list(combinations(indexes, 2))
    pair_lines = list(combinations(lines, 2))
    assert len(pair_indexes) == len(pair_lines), "Lists have different lengths"
    for line, pair in zip(pair_lines, pair_indexes):
        if distance == hamming:
            dictionary[pair[0], pair[1]] = hamming(line[0], line[1])
        elif distance == distance1:
            dictionary[pair[0], pair[1]] = distance1(line[0], line[1])
    min_key = min(dictionary, key=dictionary.get)
    print(min_key)


def main():
    hba1("./HBA1.txt", hamming)
    hba1("./HBA1.txt", distance1)


if __name__ == '__main__':
    main()

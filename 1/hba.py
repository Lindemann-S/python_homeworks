
def hamming(seq1, seq2):
    result = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            result += 1
    return result


def phash(string):
    p = 53
    result = 0
    p_pow = 1
    for letter in string:
        result += (ord(letter) - ord('a') + 1) * p_pow
        p_pow *= p
    return result


def rabin_karp(sub_str, string):
    result = 0
    str_len = len(string)
    sub_str_len = len(sub_str)
    sub_str_hash = phash(sub_str)
    for i in range(str_len - sub_str_len + 1):
        str_hash = phash(string[i:i+sub_str_len])
        if str_hash == sub_str_hash and string[i:i+sub_str_len] == sub_str:
            result += 1
    return result


def kmers(seq, k):
    dictionary = {}
    for i in range(len(seq) - k + 1):
        sub_str = seq[i:i+k]
        dictionary[sub_str] = rabin_karp(sub_str, seq)
    # print(dict)
    return dictionary


def distance1(seq1, seq2, k=2):
    kmers_seq1 = kmers(seq1, k)
    kmers_seq2 = kmers(seq2, k)
    result = 0
    for item in kmers_seq1:
        if kmers_seq2.get(item, 0) == 0:
            kmers_seq2[item] = kmers_seq1[item]
        else:
            kmers_seq2[item] = abs(kmers_seq2[item] - kmers_seq1[item])
    for item in kmers_seq2:
        result += kmers_seq2[item]
    # print(result)
    return result
        

def hba1(path, distance):
    file = open(path)
    lines = file.readlines()
    max_index = len(lines)
    dictionary = {}
    if distance == hamming:
        for line1, index1 in zip(lines[:max_index - 1], range(max_index - 1)):
            for line2, index2 in zip(lines[index1 + 1:], range(index1 + 1, max_index)):
                dictionary[index1 * 10 + index2] = hamming(line1, line2)

    if distance == distance1:
        for line1, index1 in zip(lines[:max_index - 1], range(max_index - 1)):
            for line2, index2 in zip(lines[index1 + 1:], range(index1 + 1, max_index)):
                dictionary[index1 * 10 + index2] = distance1(line1, line2)

    min_key = min(dictionary, key=dictionary.get)
    print((min_key // 10, min_key % 10))
    

def main():
    hba1("./HBA1.txt", hamming)
    hba1("./HBA1.txt", distance1)
    # kmers("abracadabra", 2)
    # distance1("abracadabra", "abracadabra")


if __name__ == '__main__':
    main()

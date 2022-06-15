import io
from more_itertools import pairwise
import random


def words(file):
    result = []
    for string in file:
        result += string.split(" ")
    return result


def transition_matrix(list_of_words):
    result = {}
    keys = pairwise(list_of_words)
    for key, value in zip(keys, list_of_words[2:]):
        if key in result:
            result[key].append(value)
        else:
            result[key] = [value]
    return result


def markov_chain(list_of_words, dictionary, n_words):
    result = []
    for word in random.choices(list_of_words, k=2):
        result.append(word)
    for i in range(n_words - 2):
        key = (result[i], result[i + 1])
        if key not in dictionary:
            result.append(random.choice(list_of_words))
        else:
            result.append(random.choice(dictionary[key]))
    result_text = ""
    for word in result:
        if word.endswith("\n"):
            last_is_n = True
        else:
            last_is_n = False
        if last_is_n:
            result_text += word
        else:
            result_text += " " + word
    return result_text


def snoop_says(path, length):
    with open(path) as file:
        text = words(file)
    stripped_text = [word.strip(".,") for word in text]
    matrix = transition_matrix(stripped_text)
    print(markov_chain(text, matrix, length))


def main():
    # handle = io.StringIO("""Ignorance is the curse of God;
    # ... knowledge is the wing wherewith we fly to heaven.""")
    # print(words(handle))
    # language = words(handle)
    # m = transition_matrix(language)
    # print(m["is", "the"])
    snoop_says("sources/snoopdogg279.txt", 23)


if __name__ == "__main__":
    main()

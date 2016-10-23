

def letter_frequency(sentence):
    frequencies = {}
    for letter in sentence:
        frequency = frequencies.setdefault(letter, 0)
        frequencies[letter] = frequency + 1
    return frequencies


mapF = letter_frequency('abrakadabrawtf')
print(mapF)

from collections import defaultdict

def letter_frequency(sentence):
    frequencies = defaultdict(int)
    for letter in sentence:
        frequencies[letter] += 1
    return frequencies

frMapper = letter_frequency('andry lindon became more popular than ever')
print(frMapper)


num_items = 0
def tuple_counter():
    global  num_items
    num_items += 1
    return (num_items, [])

d = defaultdict(tuple_counter)
d['a'][1].append("hello")
d['b'][1].append('world')
print(d)


import string
CHARACTERS = list(string.ascii_letters) + [" "]

def letter_frequency(sentence):
    frequencies = [(c, 0) for c in CHARACTERS]
    for letter in sentence:
        index = CHARACTERS.index(letter)
        frequencies[index] = (letter, frequencies[index][1] + 1)
    return frequencies

letters = letter_frequency('the quick brown fox jumps over the lazy dog')
print(letters)

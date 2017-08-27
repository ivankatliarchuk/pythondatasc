#!/usr/bin/env python

import random

numbers = range(0, 50)

even_numbers = [i for i in numbers if i % 2 == 0 and i >= 2]
print even_numbers

random_numbers = [random.randint(1, 100) for x in range(50)]
unique_random_numbers = list(set(random_numbers))
print unique_random_numbers

names = ['adam', 'Justin', 'joe', 'tony', 'zoe']
names_formatted = map(lambda x: x.title(), names)
print names_formatted

names_starting_with_j = [name for name in names_formatted if name[0].lower() == 'j']
print names_starting_with_j

import string
from random import shuffle

raw_text = "Hello and welcome to Linux Academy!!!"
letters = list(string.ascii_letters)
encoded_letters = letters[:]
shuffle(encoded_letters)

encoding_key = {}
decoding_key = {}

for k, v in zip(letters, encoded_letters):
    encoding_key[k] = v
    decoding_key[v] = k

print encoding_key
encoded_text = ''

for letter in raw_text:
    encoded_text += (encoding_key.get(letter, letter))

encoding_key = dict(zip(letters, encoded_letters))
decoding_key = dict(zip(encoding_key.values(), encoding_key.keys()))

encoded_text = ''.join([encoding_key.get(w, w) for w in raw_text])
print encoded_text
decoded_text = ''.join([decoding_key.get(w, w) for w in encoded_text])
print decoded_text




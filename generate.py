import numpy as np
import pickle
import argparse


def get_next_word(prev_words):
    slovarik = machine[tuple(prev_words)]
    summa = 0
    p = []
    for key in slovarik:
        summa += slovarik[key]
    for key in slovarik:
        p.append(slovarik[key] / summa)
    nats = list(range(1, int(len(machine[tuple(prev_words)])) + 1))
    out_word = np.random.choice(nats, p=p)
    counter = 0
    for key in slovarik:
        counter += 1
        if counter == out_word:
            return key


parser = argparse.ArgumentParser(description='Short sample app')
parser.add_argument("--model", action="store", dest="model_dir")
parser.add_argument("--prefix", action="store", dest="prefix")
parser.add_argument("--length", action="store", dest="leng", type=int)
parse = parser.parse_args()

if parse.prefix:
    prefix_words = parse.prefix.split(" ")
    word_buffer = prefix_words
else:
    word_buffer = ['я', 'хочу']

m = len(word_buffer)
n = 2

with open(parse.model_dir, 'rb') as file:
    machine = pickle.load(file)


print(word_buffer[0], end='')
for i in range(1, len(word_buffer)):
    print('', word_buffer[i], end='')
pointer = m - n
for i in range(parse.leng - m):
    _next = get_next_word(word_buffer[pointer:pointer + n])
    while word_buffer[pointer + n - 1] == '.' and _next == '.':
        _next = get_next_word(word_buffer[pointer:pointer + n])
    pointer += 1
    word_buffer.append(_next)
    if _next == '.':
        print(_next, end='')
    else :
        print('', _next, end='')

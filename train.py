import pickle
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description='Short sample app')
parser.add_argument("--input-dir", action="store", dest="input_dir")
parser.add_argument("--model", action="store", dest="model_dir")
parse = parser.parse_args()
print(parse.input_dir)


machine = {}


def do_train():
    word_data_base = []
    sentences = []

    for sent in f.split('.'):
        sent = sent.strip()
        add = ""
        for ch in sent:
            if ch.isalpha() or ch == " ":
                add = add + ch
        if add != "":
            sentences.append(add.lower())
            # if len(sentences) > 0 and sentences[len(sentences) - 1] != ".":
            #     sentences.append('.')

    # Я бы хотел, чтобы машина могла и точки расставлять, но, увы, из условия я понял, что это не требуется

    for sent in sentences:
        for word in sent.split(' '):
            if word != ' ' and word != '':
                word_data_base.append(word.strip())

    n = 2
    size = len(word_data_base)

    for i in range(size - n - 1):
        new_list = word_data_base[i:i + n]
        if tuple(new_list) not in machine:
            machine[tuple(new_list)] = {}
        ne = word_data_base[i + n]
        if ne not in machine[tuple(new_list)]:
            machine[tuple(new_list)][ne] = 1
        else:
            machine[tuple(new_list)][ne] = machine[tuple(new_list)][ne] + 1


if parse.input_dir:
    p = Path(parse.input_dir + "\\data\\")
    for x in p.rglob("*"):
        filename = x
        # filename = parse.input_dir + "\\data\\220454.txt"
        file = open(filename, 'r', encoding='utf-8')
        f = file.read()
        file.close()
        do_train()
else:
    f = input()
    do_train()


with open(parse.model_dir, "wb") as file:
    pickle.dump(machine, file)



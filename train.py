import pickle
import argparse

parser = argparse.ArgumentParser(description='Short sample app')
parser.add_argument("--input-dir", action="store", dest="input_dir")
parser.add_argument("--model", action="store", dest="model_dir")
parse = parser.parse_args()
print(parse.input_dir)

if parse.input_dir:
    filename = parse.input_dir + "\\220454.txt"
    file = open(filename, 'r', encoding='utf-8')
    f = file.read()
    file.close()
else:
    f = input()

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

wordDataBase = []

for sent in sentences:
    for word in sent.split(' '):
        if word != ' ' and word != '':
            wordDataBase.append(word.strip())

machine = {}

n = 2
size = len(wordDataBase)

for i in range(size - n - 1):
    newList = wordDataBase[i:i + n]
    if tuple(newList) not in machine:
        machine[tuple(newList)] = {}
    ne = wordDataBase[i + n]
    if ne not in machine[tuple(newList)]:
        machine[tuple(newList)][ne] = 1
    else:
        machine[tuple(newList)][ne] = machine[tuple(newList)][ne] + 1

with open(parse.model_dir, "wb") as file:
    pickle.dump(machine, file)

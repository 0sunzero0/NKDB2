#-*- coding: utf-8 -*-

import pickle
with open('/home/hyeyoung/dataset/data/doc_list.txt', 'rb') as f:
    data = pickle.load(f)

import kss
sentence_list = []
index = 1
for one_data in data:
    sentence_oneDoc_list = kss.split_sentences(one_data)
    for one_sentence in sentence_oneDoc_list:
        sentence_list.append(one_sentence)
    index += 1
    print(index)

with open('/home/hyeyoung/dataset/data/sentence_list.txt', 'wb') as f:
    pickle.dump(sentence_list, f)

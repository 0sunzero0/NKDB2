#-*- coding: utf-8 -*-

import pickle
with open('/home/hyeyoung/dataset/data/sentence_list.txt', 'rb') as f:
    sentence_list = pickle.load(f) # 단 한줄씩 읽어옴

new_sentence_list = []
for one_sentence in sentence_list:
    one_sentence = one_sentence.split(" ")
    new_sentence_list.append(one_sentence)

with open('/home/hyeyoung/dataset/data/sentence_split_list.txt', 'wb') as f:
    pickle.dump(new_sentence_list, f)
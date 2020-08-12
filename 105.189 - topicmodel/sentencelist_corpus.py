#-*- coding: utf-8 -*-

import pickle
with open('/home/hyeyoung/dataset/data/new_sentence_list.txt', 'rb') as f:
    new_sentence_list = pickle.load(f) # 단 한줄씩 읽어옴

from gensim.corpora.dictionary import Dictionary

dictionary = Dictionary(new_sentence_list)
corpus = [dictionary.doc2bow(dic) for dic in new_sentence_list]
print(corpus)

from gensim import models

# 4. 만들어진 사전 정보를 가지고 벡터화 하기
tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]

print(tfidf)
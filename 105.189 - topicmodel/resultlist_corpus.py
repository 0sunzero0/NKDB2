#-*- coding: utf-8 -*-

import pickle
with open('/home/hyeyoung/dataset/data/total_result_list.txt', 'rb') as f:
    result_list = pickle.load(f) # 단 한줄씩 읽어옴

from gensim.corpora.dictionary import Dictionary

dictionary = Dictionary(result_list)
corpus = [dictionary.doc2bow(dic) for dic in result_list]
print(corpus)

with open('/home/hyeyoung/dataset/data/corpus_result_list.txt', 'wb') as f:
    pickle.dump(corpus, f)

from gensim import models

# 4. 만들어진 사전 정보를 가지고 벡터화 하기
tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]

print(tfidf)
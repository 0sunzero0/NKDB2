#-*- coding: utf-8 -*-

import pickle
with open('/home/hyeyoung/dataset/data/total_morphs_list.txt', 'rb') as f:
    total_morphs_list = pickle.load(f) # 단 한줄씩 읽어옴

from gensim.corpora.dictionary import Dictionary

dictionary = Dictionary(total_morphs_list)
dictionary.save('nkdb.dict')
corpus = [dictionary.doc2bow(dic) for dic in total_morphs_list]
print(corpus)

with open('/home/hyeyoung/dataset/data/corpus_sentence_list.txt', 'rb') as f:
    total_morphs_list = pickle.load(f) # 단 한줄씩 읽어옴

from gensim import models

with open('/home/hyeyoung/dataset/data/corpus_sentence_list.txt', 'wb') as f:
    pickle.dump(corpus, f)

# 4. 만들어진 사전 정보를 가지고 벡터화 하기
tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]

print(tfidf)
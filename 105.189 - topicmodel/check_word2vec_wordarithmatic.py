#-*- coding: utf-8 -*-

from gensim.models import word2vec

model_path = "/home/hyeyoung/dataset/model/Skipgram_model_dimension150.model"
model = word2vec.Word2Vec.load(model_path)

#1
print(model.wv.most_similar(positive=['서울', '일본'], negative=['한국']))
print()

#2
print(model.wv.most_similar(positive=['왕', '남자'], negative=['여자']))
print()

#3
print(model.wv.most_similar(positive=["김대중", "북한"], negative=["남한"]))
print()

#4
print(model.wv.most_similar(positive=["대통령", "북한"], negative=["남한"]))
print()

#5
print(model.wv.most_similar(positive=["국가원수", "남한"], negative=["북한"]))
print()

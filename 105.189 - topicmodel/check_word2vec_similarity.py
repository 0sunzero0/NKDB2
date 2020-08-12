#-*- coding: utf-8 -*-

from gensim.models import word2vec

model_path = "/home/hyeyoung/dataset/model/Skipgram_model_dimension200.model"
model = word2vec.Word2Vec.load(model_path)

print(model.wv.similarity('의료', '진료'))
print()

print(model.wv.similarity('남북정상회담', '한미정상회담'))
print()

print(model.wv.similarity())
print()

print(model.wv.similarity())
print()

print(model.wv.similarity())
print()

print(model.wv.similarity())
print()

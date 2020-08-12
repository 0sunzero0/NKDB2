#-*- coding: utf-8 -*-

from gensim.models import word2vec
model_path = "/home/hyeyoung/dataset/model/Skipgram_model_dimension200.model"
model = word2vec.Word2Vec.load(model_path)

#1
input_query = "대통령"
associate_word = model.wv.most_similar(positive=[input_query])
print(associate_word)
print()

#2
input_query = "통일"
associate_word = model.wv.most_similar(positive=[input_query])
print(associate_word)
print()

#3
input_query = "주민"
associate_word = model.wv.most_similar(positive=[input_query])
print(associate_word)
print()

#4
input_query = "식량"
associate_word = model.wv.most_similar(positive=[input_query])
print(associate_word)
print()

#5
input_query = "의료"
associate_word = model.wv.most_similar(positive=[input_query])
print(associate_word)
print()

#6
input_query = "농업"
associate_word = model.wv.most_similar(positive=[input_query])
print(associate_word)
print()

#7
input_query = "정상회담"
associate_word = model.wv.most_similar(positive=[input_query])
print(associate_word)
print()

#8
input_query = "북핵"
associate_word = model.wv.most_similar(positive=[input_query])
print(associate_word)
print()

#9
input_query = "인권"
associate_word = model.wv.most_similar(positive=[input_query])
print(associate_word)
print()

#10
input_query = "지원"
associate_word = model.wv.most_similar(positive=[input_query])
print(associate_word)
print()
#-*- coding: utf-8 -*-

from gensim.models import word2vec
model_path = "/home/hyeyoung/dataset/model/Skipgram_model_dimension200.model"
#model_path = "/home/hyeyoung/tmp/NKDB2_project/105.189 - topicmodel/model_path"
model = word2vec.Word2Vec.load(model_path)

#1
print(model.doesnt_match("통일 북한 남한 무역".split()))
#2
print(model.doesnt_match("필요성 교육 재인식 고려사항 조치 식량".split()))
#3
print(model.doesnt_match("북핵 핵 실험 무역".split()))
#4
print(model.doesnt_match("의료 보건 건강 인권".split()))
#5
print(model.doesnt_match("인권 유엔 정책 김정일".split()))




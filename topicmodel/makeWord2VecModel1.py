#-*- coding: utf-8 -*-

import pickle
with open('/home/hyeyoung/dataset/data2/total_morphs_list_2.txt', 'rb') as f:
    corpus = pickle.load(f) # 단 한줄씩 읽어옴

# word2vec 모델 학습
from gensim.models import word2vec

data = corpus
model = word2vec.Word2Vec(data, size = 50, window = 5, min_count=5, workers = -1, sg=1) #Skipgram
# 50차원 벡터,
# 출현 빈도는 5개 미만은 제외
# 분석 방법론은 Skip-gram을 선택

model.save("/home/hyeyoung/dataset/model/Skipgram_model_dimension50.model")


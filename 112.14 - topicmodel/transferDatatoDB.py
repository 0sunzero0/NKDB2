#-*- coding: utf-8 -*-

import pickle
import pymongo

uri = "mongodb://localhost:27017"
connection = pymongo.MongoClient(uri)


db = connection["NKDB"]
nkdb_collection = db["nkdb_test"]

with open('/home/hyeyoung/dataset/data/total_morphs_list_2.txt', 'rb') as f:
    data = pickle.load(f) # 단 한줄씩 읽어옴

for one_data in data:
    one_data
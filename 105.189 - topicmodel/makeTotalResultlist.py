#-*- coding: utf-8 -*-
import pickle

with open('/home/hyeyoung/dataset/data/result_list1.txt', 'rb') as f:
    data1 = pickle.load(f) # 단 한줄씩 읽어옴

with open('/home/hyeyoung/dataset/data/result_list2.txt', 'rb') as f:
    data2 = pickle.load(f) # 단 한줄씩 읽어옴

with open('/home/hyeyoung/dataset/data/result_list3.txt', 'rb') as f:
    data3 = pickle.load(f) # 단 한줄씩 읽어옴

with open('/home/hyeyoung/dataset/data/result_list4.txt', 'rb') as f:
    data4 = pickle.load(f) # 단 한줄씩 읽어옴

total_result_list = []

total_result_list.extend(data1)
total_result_list.extend(data2)
total_result_list.extend(data3)
total_result_list.extend(data4)

with open('/home/hyeyoung/dataset/data/total_result_list.txt', 'wb') as f:
    pickle.dump(total_result_list, f)


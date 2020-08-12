#-*- coding: utf-8 -*-
import pickle

with open('/home/hyeyoung/dataset/data/result_list1_1.txt', 'rb') as f:
    data1_1 = pickle.load(f) # 단 한줄씩 읽어옴

with open('/home/hyeyoung/dataset/data/result_list1_2.txt', 'rb') as f:
    data1_2 = pickle.load(f) # 단 한줄씩 읽어옴

with open('/home/hyeyoung/dataset/data/result_list1_3.txt', 'rb') as f:
    data1_3 = pickle.load(f) # 단 한줄씩 읽어옴

with open('/home/hyeyoung/dataset/data/result_list1_4.txt', 'rb') as f:
    data1_4 = pickle.load(f) # 단 한줄씩 읽어옴

with open('/home/hyeyoung/dataset/data/result_list1_5.txt', 'rb') as f:
    data1_5 = pickle.load(f) # 단 한줄씩 읽어옴

with open('/home/hyeyoung/dataset/data/result_list1_6.txt', 'rb') as f:
    data1_6 = pickle.load(f) # 단 한줄씩 읽어옴

with open('/home/hyeyoung/dataset/data/result_list1_7.txt', 'rb') as f:
    data1_7 = pickle.load(f) # 단 한줄씩 읽어옴

with open('/home/hyeyoung/dataset/data/result_list1_8.txt', 'rb') as f:
    data1_8 = pickle.load(f) # 단 한줄씩 읽어옴

with open('/home/hyeyoung/dataset/data/result_list2.txt', 'rb') as f:
    data2 = pickle.load(f) # 단 한줄씩 읽어옴

with open('/home/hyeyoung/dataset/data/result_list3.txt', 'rb') as f:
    data3 = pickle.load(f) # 단 한줄씩 읽어옴

with open('/home/hyeyoung/dataset/data/result_list4.txt', 'rb') as f:
    data4 = pickle.load(f) # 단 한줄씩 읽어옴

total_result_list = []

total_result_list.extend(data1_1)
total_result_list.extend(data1_2)
total_result_list.extend(data1_3)
total_result_list.extend(data1_4)
total_result_list.extend(data1_5)
total_result_list.extend(data1_6)
total_result_list.extend(data1_7)
total_result_list.extend(data1_8)
total_result_list.extend(data2)
total_result_list.extend(data3)
total_result_list.extend(data4)

with open('/home/hyeyoung/dataset/data/total_result_list.txt', 'wb') as f:
    pickle.dump(total_result_list, f)


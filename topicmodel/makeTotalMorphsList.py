#-*- coding: utf-8 -*-
import pickle

with open('/home/hyeyoung/dataset/data2/result_list1_2.txt', 'rb') as f:
    data1 = pickle.load(f) # 단 한줄씩 읽어옴

with open('/home/hyeyoung/dataset/data2/result_list2_2.txt', 'rb') as f:
    data2 = pickle.load(f) # 단 한줄씩 읽어옴

with open('/home/hyeyoung/dataset/data2/result_list3_2.txt', 'rb') as f:
    data3 = pickle.load(f) # 단 한줄씩 읽어옴

with open('/home/hyeyoung/dataset/data2/result_list4_2.txt', 'rb') as f:
    data4 = pickle.load(f) # 단 한줄씩 읽어옴

with open('/home/hyeyoung/dataset/data2/result_list5_2.txt', 'rb') as f:
    data5 = pickle.load(f) # 단 한줄씩 읽어옴

with open('/home/hyeyoung/dataset/data2/result_list6_2.txt', 'rb') as f:
    data6 = pickle.load(f) # 단 한줄씩 읽어옴

with open('/home/hyeyoung/dataset/data2/result_list7_2.txt', 'rb') as f:
    data7 = pickle.load(f) # 단 한줄씩 읽어옴

with open('/home/hyeyoung/dataset/data2/result_list8_2.txt', 'rb') as f:
    data8 = pickle.load(f) # 단 한줄씩 읽어옴

with open('/home/hyeyoung/dataset/data2/result_list9_2.txt', 'rb') as f:
    data9 = pickle.load(f)  # 단 한줄씩 읽어옴

with open('/home/hyeyoung/dataset/data2/result_list10_2.txt', 'rb') as f:
    data10 = pickle.load(f)  # 단 한줄씩 읽어옴

with open('/home/hyeyoung/dataset/data2/result_list11_2.txt', 'rb') as f:
    data11 = pickle.load(f)  # 단 한줄씩 읽어옴

with open('/home/hyeyoung/dataset/data2/result_list12_2.txt', 'rb') as f:
    data12 = pickle.load(f)  # 단 한줄씩 읽어옴

with open('/home/hyeyoung/dataset/data2/result_list13_2.txt', 'rb') as f:
    data13 = pickle.load(f)  # 단 한줄씩 읽어옴

with open('/home/hyeyoung/dataset/data2/result_list14_2.txt', 'rb') as f:
    data14 = pickle.load(f)  # 단 한줄씩 읽어옴

total_morphslist = []

total_morphslist.extend(data1)
total_morphslist.extend(data2)
total_morphslist.extend(data3)
total_morphslist.extend(data4)
total_morphslist.extend(data5)
total_morphslist.extend(data6)
total_morphslist.extend(data7)
total_morphslist.extend(data8)
total_morphslist.extend(data9)
total_morphslist.extend(data10)
total_morphslist.extend(data11)
total_morphslist.extend(data12)
total_morphslist.extend(data13)
total_morphslist.extend(data14)

print(len(total_morphslist))

with open('/home/hyeyoung/dataset/data/total_morphs_list_2.txt', 'wb') as f:
    pickle.dump(total_morphslist, f)


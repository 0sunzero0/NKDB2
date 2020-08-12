#-*- coding: utf-8 -*-

import pickle
with open('/home/hyeyoung/dataset/data/sentence_list.txt', 'rb') as f:
    sentence_list = pickle.load(f)

quarter_index = 688784
half_index = 1377567
quarter3_index = 2066351
end_index = 2755134


sentence_list1 = sentence_list[0 : quarter_index]
sentence_list2 = sentence_list[quarter_index : half_index]
sentence_list3 = sentence_list[half_index : quarter3_index]
sentence_list4 = sentence_list[quarter3_index : end_index]

with open('/home/hyeyoung/dataset/data/sentence_list1.txt', 'wb') as f:
    pickle.dump(sentence_list1, f)

with open('/home/hyeyoung/dataset/data/sentence_list2.txt', 'wb') as f:
    pickle.dump(sentence_list2, f)

with open('/home/hyeyoung/dataset/data/sentence_list3.txt', 'wb') as f:
    pickle.dump(sentence_list3, f)

with open('/home/hyeyoung/dataset/data/sentence_list4.txt', 'wb') as f:
    pickle.dump(sentence_list4, f)
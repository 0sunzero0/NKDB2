import pickle
with open('/home/hyeyoung/dataset/data/sentence_list.txt', 'rb') as f:
    sentence_list = pickle.load(f)

print(sentence_list[1455941:1455951])
print()
print()

with open('/home/hyeyoung/dataset/data/result_list3.txt', 'rb') as f:
    result_list3 = pickle.load(f)

print(result_list3[-610410:-610400])
#-*- coding: utf-8 -*-

from gensim.models import Word2Vec
from MulticoreTSNE import MulticoreTSNE as TSNE
import matplotlib.pyplot as plt
import pandas as pd

model = Word2Vec.load("/home/hyeyoung/dataset/model/CBOW_model.model")

vocab = list(model.wv.vocab)
X = model[vocab]

print(len(X))
print(X[0][:10])
tsne = TSNE(n_components=2)

# 100개의 단어에 대해서만 시각화
X_tsne = tsne.fit_transform(X[:100,:])
# X_tsne = tsne.fit_transform(X)

df = pd.DataFrame(X_tsne, index=vocab[:100], columns=['x', 'y'])
print(df.shape)

fig = plt.figure()
fig.set_size_inches(40, 20)
ax = fig.add_subplot(1, 1, 1)

ax.scatter(df['x'], df['y'])

for word, pos in df.iterrows():
    ax.annotate(word, pos, fontsize=30)
plt.show()

#
# def tsne_plot(model):
#     labels = []
#     tokens = []
#
#     for word in model.wv.vocab:
#         tokens.append(model[word])
#         labels.append(word)
#
#     tsne_model = TSNE(perplexity=40, n_components=2, n_jobs=4)
#     new_values = tsne_model.fit_transform(tokens)
#
#     x = []
#     y = []
#     for value in new_values:
#         x.append(value[0])
#         y.append(value[1])
#
#     plt.figure(figsize=(16, 16))
#     for i in range(len(x)):
#         plt.scatter(x[i], y[i])
#         plt.annotate(labels[i],
#                      xy=(x[i], y[i]),
#                      xytext=(5, 2),
#                      textcoords='offset points',
#                      ha='right',
#                      va='bottom')
#     plt.show()
#
# tsne_plot(model)

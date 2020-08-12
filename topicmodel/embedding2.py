#-*- coding: utf-8 -*-
import pandas as pd
from gensim.models import Word2Vec

word2vec_filepath = "/home/hyeyoung/dataset/model2/CBOW_model.model"
model = Word2Vec.load(word2vec_filepath)

ordered_vocab = [(term, voc.index, voc.count) for term, voc in model.wv.vocab.items()]

# sort by the term counts, so the most common terms appear first
ordered_vocab = sorted(ordered_vocab, key=lambda k: -k[2])

# unzip the terms, integer indices, and counts into separate lists
ordered_terms, term_indices, term_counts = zip(*ordered_vocab)
# print(ordered_terms)
# create a DataFrame with the food2vec vectors as data,
# and the terms as row labels
word_vectors = pd.DataFrame(model.wv.syn0[term_indices, :], index=ordered_terms)

#print(word_vectors.head(1000))


from MulticoreTSNE import MulticoreTSNE as TSNE
tsne_input = word_vectors

tsne = TSNE()
tsne_vectors = tsne.fit_transform(tsne_input.values)

import pickle
with open('/home/hyeyoung/dataset/tsne_vecs.txt', 'wb') as f:
    pickle.dump(tsne_vectors, f)

from sklearn.cluster import KMeans
import numpy as np

#Create random data
X = np.array([[1, 2], [1, 4], [1, 0],
              [10, 2], [10, 4], [10, 0]])
#Create model
kmeans = KMeans(n_clusters=2, random_state=0)

#Feed data to model
kmeans.fit(X)

#Predict the output for X
kmeans.labels_

#Predict output for unseen data
kmeans.predict([[0, 0], [12, 3]])

ac = AgglomerativeClustering()

#Feed data to model
ac.fit(X)

#Predict the output for X
ac.labels_


clustering = DBSCAN(eps=3, min_samples=2)

#Feed data to model
clustering.fit(X)

#Predict the output for X
clustering.labels_



import pandas as pd
import gensim
from gensim.parsing.preprocessing import preprocess_documents
from gensim.models.doc2vec import Doc2Vec, TaggedDocument



processed_corpus = preprocess_documents(text_corpus)
tagged_corpus = [TaggedDocument(d, [i]) for i, d in enumerate(processed_corpus)]


model = Doc2Vec(tagged_corpus, dm=0, vector_size=200, window=2, min_count=1, epochs=100, hs=1)

new_doc = gensim.parsing.preprocessing.preprocess_string(new_doc)
test_doc_vector = model.infer_vector(new_doc)
sims = model.docvecs.most_similar(positive = [test_doc_vector])
for s in sims:
    print(f"{(s[1])} | {df['Title'].iloc[s[0]]}")



import gensim
import gensim.downloader as api
dataset = api.load("text8")
data = [d for d in dataset]


def tagged_document(list_of_list_of_words):
   for i, list_of_words in enumerate(list_of_list_of_words):
      yield Gensim.models.doc2vec.TaggedDocument(list_of_words, [i])
data_training = list(tagged_document(data))


data_training [:1]

model = Gensim.models.doc2vec.Doc2Vec(vector_size=40, min_count=2, epochs=30)

model.build_vocab(data_training)


print(model.infer_vector(['violent', 'means', 'to', 'destroy', 'the','organization']))


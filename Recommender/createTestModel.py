from gensim import corpora, models, similarities


documents = ["Human machine interface for lab abc computer applications",
              "A survey of user opinion of computer system response time",
              "The EPS user interface management system",
              "System and human system engineering testing of EPS",
              "Relation of user perceived response time to error measurement",
              "The generation of random binary unordered trees",
              "The intersection graph of paths in trees",
              "Graph minors IV Widths of trees and well quasi ordering",
              "Graph minors A survey"]

stoplist = set('for a of the and to in'.split())
texts = [[word for word in document.lower().split() if word not in stoplist]
          for document in documents]

# Remove words that appear only once
from collections import defaultdict
frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1
texts = [[token for token in text if frequency[token] > 1]
          for text in texts]

# Convert Documents to vectors
dictionary = corpora.Dictionary(texts)
dictionary.save('deerwester.dict')

# Create the Corpus
corpus = [dictionary.doc2bow(text) for text in texts]
corpora.MmCorpus.serialize('deerwester.mm', corpus)

#Initialize the TFidfModel
tfidf = models.TfidfModel(corpus)

# Apply the model to the entire corpus
corpus_tfidf = tfidf[corpus]


# Use the LSI model
lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=2)
corpus_lsi = lsi[corpus_tfidf]

# Save the model
lsi.save('model.lsi')

# Load the model
lsi_model = models.LsiModel.load('model.lsi')





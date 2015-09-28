from gensim import corpora, models, similarities

# The documents
documents = ["Human machine interface for lab abc computer applications",
              "A survey of user opinion of computer system response time",
              "The EPS user interface management system",
              "System and human system engineering testing of EPS",
              "Relation of user perceived response time to error measurement",
              "The generation of random binary unordered trees",
              "The intersection graph of paths in trees",
              "Graph minors IV Widths of trees and well quasi ordering",
              "Graph minors A survey"]

# Remove common words (stop words) and tokenize documents
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

# We are now going to convert documents to vectors
# First we create a bag-of-words
dictionary = corpora.Dictionary(texts)
dictionary.save('/tmp/deerwester.dict')

# Now we create a corpus from our texts
corpus = [dictionary.doc2bow(text) for text in texts]

# Now we create a transformation or model from our corpus
tfidf = models.TfidfModel(corpus)

# Now we apply the model or the transformation to our corpus
corpus_tfidf = tfidf[corpus]

# Next use the model for LSI or LDA. Here I use lsi
lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_points=2)
corpus_lsi = lsi[corpus_tfidf]


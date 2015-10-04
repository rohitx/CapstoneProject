from gensim import corpora, models, similarities
from pprint import pprint
import pandas as pd

def toyModel(doc):
    # Get the list of original documents
    df = pd.read_csv("text.csv", names=["Documents"])
    # Load the model
    lsi_model = models.LsiModel.load('model.lsi')
    # Load the corpus
    corpus = corpora.MmCorpus('deerwester.mm')
    index = similarities.MatrixSimilarity(lsi_model[corpus])
    # Load the dictionary
    dictionary = corpora.Dictionary.load('deerwester.dict')

    vec_bow = dictionary.doc2bow(doc.lower().split())
    vec_lsi = lsi_model[vec_bow]

    sims = index[vec_lsi]

    sims_sorted = sorted(enumerate(sims), key=lambda item: -item[1])
    #print(sims_sorted)

    for val in sims_sorted[:4]:
        index, value = val[0], val[1]
        print df.Documents.loc[index], value

    return sims_sorted


doc = "Human Interaction station"
sim = toyModel(doc)






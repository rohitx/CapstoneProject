"""
This function creates a corpus of Indie games

File(s) used: None
Database(s) uses: MongoDB
                  Uses collections:
                  PopularGames
                  IndieGames
Created: September 28th, 2015
Creator: Rohit Deshpande
"""

# Import Statements
from pymongo import MongoClient
import pandas as pd
import re
from gensim import corpora, models, similarities

# Initialize Mongo Clients
client = MongoClient()

# Get Popular Games Database
db_popGames = client.Games
cursor_popGames = db_popGames.PopularGames.find()
df_popGames = pd.DataFrame(list(cursor_popGames))


# Get Indie Games Database
db_indieGames = client.Games
cursor_indieGames = db_indieGames.IndieGames.find()
df_indieGames = pd.DataFrame(list(cursor_indieGames))

#Get all summaries associated with IndieGames
all_summaries = df_indieGames.summary

# Let's work on a smaller subset
sub_docs = all_summaries

# Convert list of lists to list of strings
documents = []
for a in sub_docs:
    for word in a:
        documents.append("".join(word.encode("utf-8")))

# Clean all the summaries
summary_texts = []

for document in documents:
    # Begin by creating a lowercase of each summary
    document = document.lower()
    # Remove the "\n" from each summary
    document = document.replace("\n", "")
    # Remove alphanumeric characters from each summary
    document = re.sub('[\\@$\/\#\.\-:&\*\+\=\[\]?!\(\)\{\},\'\">\_<;%]',r'', document)
    # Remove any URLs from each summary
    document = re.sub(r'(http|https)://[^\s]*', r'httpaddr', document)
    # Remove email addresses from summary
    document = re.sub(r'[^\s]+@[^\s]+', r'emailaddr', document)
    # Replace $ symbol with text
    document = re.sub(r'[$]+', r'dollar', document)
    # Remove white space
    document = re.sub(r'\s+',r' ', document)
    # Remove additional characters
    document = re.sub(r'~',r' ', document)
    document = re.sub(r'\|',r' ', document)
    document = re.sub(r'\^',r' ', document)
    # Finally remove white space
    document = document.strip()
    summary_texts.append(document)

# Remove stop words from the summary
summary_vectors = []
stoplist = set('for a of the and to in'.split())

for summary_text in summary_texts:
    words = summary_text.split()
    split_words = [word for word in words if word.lower() not in stoplist]
    result = ' '.join(split_words)
    result = result.split()
    summary_vectors.append(result)


# Create a term-frequency table
from collections import defaultdict
frequency = defaultdict(int)
for text in summary_vectors:
    for token in text:
        frequency[token] += 1

# Remove words that have frequency token less than 1
summary_tf = [[token for token in text if frequency[token] > 1]
          for text in summary_vectors]

# Create a dictionary from all of the summaries
dictionary = corpora.Dictionary(summary_tf)
dictionary.save('IndieSummaries.dict')

# Create a corpus of all of the Indie Games
corpus = [dictionary.doc2bow(text) for text in summary_tf]
corpora.MmCorpus.serialize('IndieSummaries.mm', corpus)

if __name__ == '__main__':
    main()

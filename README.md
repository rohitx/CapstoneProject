# Indie Game Recommender

A recommendation engine to help main stream video gamers discover games created by independent individuals or small groups.
<br>
![](Late_summer.png)
<br>
Before I go into the motivation, the data, and the modeling process, I would like to explain verbally and visually the file structure of this repo.

## Repo Structure

The Capstone project repo is divided into three main directories:

```
.
|-- App
|   |___app.py
|   |___model.py
|   |   |___gensim_files
|   |___getGameName.py
|   |___static
|   |___templates
|-- GetData
|   |___getMongoDBMetacritic.py
|   |___getMongoDBIndie.py
|-- Recommender
|   |___getCorpus.py
|   |   |___IndieSummaries.dict
|   |   |___IndieSummaries.mm
|   |   |___IndieSummaries.mm.index
|   |___model.py
|   |   |___model_indie.lsi
|   |   |___model_indie.lsi.projection
```


1. **`App`**:This directory has the actual application written in Flask and Jinja that runs on www.indiegamerpro.com. This directory contains the `model.py` and `app.py` and `getGameName.py`. The `app.py` runs the Flask application. `getGameName.py` takes the user-input cleans and converts it in the same format``The `model.py` recommends a game based on user input while
2. **`GetData`**: This directory has two python files. The `getMongoDBMetacritic.py` and `getMongoDBIndiedb.py`. Both of these files are web scrapers. They scrape the www.metacritic.com and www.indiedb.com websites for game information such as summaries, genre, title, platform, and more.
3. `Recommender`: This subdirectory contains two main files, `getCorpus.py` and `model.py`. The python program `getCopus.py` creates a corpus or bag-of-words from all of the ~1500 indie games. It has other files such as the dictionary, index file and the model file.

The **`model.py`** file contains the LSI model that is created using the Latent Semantic Analysis. The LSA uses singular matrix decomposition or SVD and therefore generates two files such as `model_indie.lsi` and `model_indie.lsi.projection`.

## Motivation

Ubisoft, Activision, and Electronic Arts are few of the biggest players that dominate the video gaming scene. They have huge resources to create and develop games, deep financial pockets to support development of multiple games, and a large advertising budget to market their products. In contrast video games created by individuals or small groups, called Indie games, are often incredibly additive, visually appealing, and have great game play. However, they lack the financial support and advertisement budget to make their games popular and compete with the biggest players.

Steam, an internet-based digital distribution platform, is the most popular site to purchase video games created for PC, Mac, and Linux. They have around 2000 Indie Games. However, their recommendation engine will generally recommends games created by the same company and of the same genre. Most recommendation systems do that. However, it would be good if they could recommend games outside of the genre.

I created a recommender system to address the issue of unbalanced Indie Gaming market and create a recommender system that recommends games not just within the genre but also outside of it.

## Data Acquisition

The first steps involved acquiring data for the project. I collected ~3000 most popular games by searching online for games from 2000 to 2015. The list was created by adding the names I searched online and the games I have myself played and know of.

The next step involved finding indie games. First I searched on Steam and found ~2000 indie games. However, a search online revealed a website called www.indiedb.com. This website had 13,700 indie games. Hence, this became my source for Indie games.

Finally, I used metacritic to get summaries and other information of popular games. I used metacritic over Steam because Steam poses a challenge to scrape. I found that pagination does not work on Steam when I scraped Steam, i.e., the scrapper is unable to move to the next page. It would also return the same page. This element is set intentionally by Steam to prevent scrapping.

Metacritic also posed a challenge initially as it rejected the ping from my scrapper. The rejected was a result of anti-scrapping function set by Metacritic.com. The website recognizes python's library `urllib2` and therefore return a `forbidden error`. The work-around was fairly straight-forward. I had to set few parameters in my scrapper that help it to mask itself as a Mozilla browser. After which I was able to scrape ~3000 pages fairly easily.

Indiedb.com did not pose such a problem. It was quite easy to scrape. However, the webpages are not consistent in the their HTML structure. Furthermore, there seems a trend to embed the summary in an image. This made scrapping of the latest games quite hard. However, only handful of the cases suffered. The major hurdle was the fact that a lot of games were unrated by users. Here's a summary of what I found:

```
    13,422 games in indiedb.com
    9163   games work for either Windows, Mac, or Linux
    4353   games have at least one rating
```



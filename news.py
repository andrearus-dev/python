# libraries

from newspaper import Article
from textblob import TextBlob  # for sentiment analysis
import nltk
import tkinter as tk

nltk.download('punkt')

# get summary of article = pass in url

url = 'https://techcrunch.com/2021/05/05/cymulate-nabs-45m-to-test-and-improve-cybersecurity-defenses-via-attack-simulations/'


# create article object from newspaper library

article = Article(url)
article.download()  # download the data
article.parse()  # dissects article in the parts that it needs

article.nlp()

print(f'Title: {article.title}')
print(f'Author: {article.authors}')
print(f'Publication Date: {article.publish_date}')
print(f'Summary: {article.summary}')

# Sentiment analysis

analysis = TextBlob(article.text)
print(analysis.polarity)
print(f'Sentiment: {'positive' if analysis.polarity > 0 else 'negative' if analysis.polarity < 0 else 'neutral'}')

# Building the graphical user interface

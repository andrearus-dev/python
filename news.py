# libraries

from newspaper import Article
from textblob import TextBlob
import nltk
import tkinter as tk

# get summary of article = pass in url

url = 'https://techcrunch.com/2021/05/05/cymulate-nabs-45m-to-test-and-improve-cybersecurity-defenses-via-attack-simulations/'


# create article object from newspaper library

article = Article(url)
article.download()  # download the data
article.parse()  # dissects article in the parts that it needs

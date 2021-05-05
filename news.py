# libraries

from newspaper import Article
from textblob import TextBlob  # for sentiment analysis
import nltk
import tkinter as tk

# nltk.download('punkt')

# # get summary of article = pass in url

# url = 'https://techcrunch.com/2021/05/05/cymulate-nabs-45m-to-test-and-improve-cybersecurity-defenses-via-attack-simulations/'


# # create article object from newspaper library

# article = Article(url)
# article.download()  # download the data
# article.parse()  # dissects article in the parts that it needs

# article.nlp()

# print(f'Title: {article.title}')
# print(f'Author: {article.authors}')
# print(f'Publication Date: {article.publish_date}')
# print(f'Summary: {article.summary}')


# # Sentiment analysis

# analysis = TextBlob(article.text)
# print(analysis.polarity)
# print(f'Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')


# Building the graphical user interface

# create tkinter window screen
root = tk.Tk()
root.title("News Summarizer")
root.geometry('1200x600')

# create individual buttons/ labels/ textboxes

# title
tlabel = tk.Label(root, text="Title")
tlabel.pack()  # to see it on the screen

title = tk.Text(root, height=1, width=140)
# state disabled so the user can't go in and change it
title.config(state='disabled', bg='#dddddd')
title.pack()

# author
alabel = tk.Label(root, text="Author")
alabel.pack()

author = tk.Text(root, height=1, width=140)
author.config(state='disabled', bg='#dddddd')
author.pack()

# publication
plabel = tk.Label(root, text="Publishing Date")
plabel.pack()

publication = tk.Text(root, height=1, width=140)
publication.config(state='disabled', bg='#dddddd')
publication.pack()

# textbox - summary
slabel = tk.Label(root, text="Summary")
slabel.pack()

summary = tk.Text(root, height=20, width=140)
summary.config(state='disabled', bg='#dddddd')
summary .pack()

# URL
ulabel = tk.Label(root, text="Sentiment Analysis")
ulabel.pack()

utext = tk.Text(root, height=1, width=140)
utext.pack()

# Button
btn = tk.Button(root, text="Summarize")
btn.pack()


root.mainloop()

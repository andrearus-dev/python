# libraries

from newspaper import Article
from textblob import TextBlob  # for sentiment analysis
import nltk
import tkinter as tk


def summarize():
 # get article from the texbox
    url = utext.get('1.0', "end").strip()  # need a start and end point

    # create article object from newspaper library

    article = Article(url)
    article.download()  # download the data
    article.parse()  # dissects article in the parts that it needs

    article.nlp()

    # change content of individual text boxes

    title.config(state='normal')
    author.config(state='normal')
    publication.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')
    # we need to have the state enabled to be able to edit

    title.delete('1.0', 'end')
    title.insert('1.0', article.title)

    author.delete('1.0', 'end')
    author.insert('1.0', article.authors)

    publication.delete('1.0', 'end')
    publication.insert('1.0', article.publish_date)

    summary.delete('1.0', 'end')
    summary.insert('1.0', article.summary)

    # Sentiment analysis

    analysis = TextBlob(article.text)
    sentiment.delete('1.0', 'end')
    sentiment.insert(
        '1.0', f'Polarity: {analysis.polarity}Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')

    # disable configuration so the user can't change content

    title.config(state='disabled')
    author.config(state='disabled')
    publication.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')

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

# Sentiment Analysis
selabel = tk.Label(root, text="Summary")
selabel.pack()

sentiment = tk.Text(root, height=1, width=140)
sentiment.config(state='disabled', bg='#dddddd')
sentiment.pack()

# URL
ulabel = tk.Label(root, text="URL")
ulabel.pack()

utext = tk.Text(root, height=1, width=140)
utext.pack()

# Button
# refer to the function, not call it
btn = tk.Button(root, text="Summarize", command=summarize)
btn.pack()

root.mainloop()

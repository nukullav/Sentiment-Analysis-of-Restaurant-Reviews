# -*- coding: utf-8 -*-
"""Base_1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VH8jxT_VGaQBoyZxjjK_fjub3NryNHFy
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset=pd.read_csv('/content/Restaurant_Reviews.tsv',delimiter='\t',quoting=3)

dataset.head()

text = '''isan is a pandas DataFrame method that returns a DataFrame of the same shape as the original DataFrame,
where each element is either True if it's a missing or null value (NaN), or False if it's not.'''
dataset.isna().sum()

dataset.shape

import seaborn as sns

sns.countplot(x='Liked', data=pd.DataFrame({'Liked': [1, 0, 1, 0]}))

text = '''import re: This imports the re module, which stands for "regular expressions."
Regular expressions are a powerful tool for pattern matching and manipulation of strings in Python.
They allow you to search for specific patterns within text, extract information, or replace parts of the text based on defined patterns.'''

text = '''import nltk: This imports the nltk library, which stands for "Natural Language Toolkit."
NLTK is a popular library for natural language processing (NLP) tasks in Python.
It provides various tools and resources for tasks such as tokenization, stemming, lemmatization, part-of-speech tagging, parsing, and more.'''

text = '''nltk.download('stopwords'): This line downloads the stopwords dataset from NLTK.
Stopwords are common words (such as "and", "the", "is", etc.) that are often filtered out from text data during preprocessing,
as they typically do not carry significant meaning for many NLP tasks like text classification or sentiment analysis.
NLTK provides a list of stopwords for various languages, and downloading them makes them accessible for your NLP tasks in Python.'''


import re
import nltk
nltk.download('stopwords')

#from nltk.corpus import stopwords: This line imports the stopwords module from the NLTK corpus submodule. NLTK provides a collection of corpora, lexical resources, and datasets for various natural language processing tasks. The stopwords module contains lists of common stopwords for different languages, which are often removed from text during preprocessing to improve the performance of NLP tasks.

#from nltk.stem.porter import PorterStemmer: This line imports the PorterStemmer class from the porter module in the nltk.stem submodule. Stemming is a technique used in natural language processing and information retrieval to reduce words to their root or base form (known as the stem) by removing affixes. The Porter stemming algorithm, implemented in NLTK as PorterStemmer, is one of the most commonly used stemming algorithms.
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

#The line corpus=[] initializes an empty list named corpus in Python.

#In natural language processing (NLP) tasks, a "corpus" typically refers to a collection of text documents used for analysis, processing, or training machine learning models.
corpus=[]

dataset['Review'][0]

text = '''This line iterates through each word in the review list, applies stemming using the PorterStemmer,
and filters out any words that are in the list of English stopwords.
The list of stopwords is obtained from the NLTK stopwords module for the English language.
The result is a list of processed words for the current review.'''
for i in range(0,1000):
  review = re.sub('[^a-zA-Z]', ' ',dataset['Review'][i])
  review = review.lower()
  review = review.split()
  ps=PorterStemmer()
  review=[ps.stem(word) for word in review if not word in stopwords.words('english')]

review

for i in range(0,1000):
  review = re.sub('[^a-zA-Z]', ' ',dataset['Review'][i])
  review = review.lower()
  review = review.split()
  ps=PorterStemmer()
  review=[ps.stem(word) for word in review if not word in set(stopwords.words('english'))]

review

for i in range(0,1000):
  review = re.sub('[^a-zA-Z]', ' ',dataset['Review'][i])
  review = review.lower()
  review = review.split()
  ps=PorterStemmer()
  review=[ps.stem(word) for word in review if not word in stopwords.words('english')]
  review = ''.join(review)

review

for i in range(0,1000):
  review = re.sub('[^a-zA-Z]', ' ',dataset['Review'][i])
  review = review.lower()
  review = review.split()
  ps=PorterStemmer()
  review=[ps.stem(word) for word in review if not word in stopwords.words('english')]
  review = ' '.join(review)

review

for i in range(0,1000):
  review = re.sub('[^a-zA-Z]', ' ',dataset['Review'][i])
  review = review.lower()
  review = review.split()
  ps=PorterStemmer()
  review=[ps.stem(word) for word in review if not word in stopwords.words('english')]
  review = ' '.join(review)
  corpus.append(review)

corpus

#Running these lines of code, X will contain the numerical representation of the text data, and y will contain the target variable values from the dataset, suitable for use in machine learning models. Typically, X would be used as the input features, and y would be used as the target variable for training and evaluation.
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus).toarray()
y=dataset.iloc[: , -1].values

X

y

text = '''By using the above commands we'll have separate arrays (X_train, X_test, y_train, y_test) containing the training and testing data,
which you can then use to train and evaluate machine learning models.Typically,
you would use the training data (X_train and y_train) to train the model and the testing data (X_test and y_test) to evaluate its performance.'''
from sklearn.model_selection import train_test_split
X_train, X_test ,y_train ,y_test=train_test_split(X,y,test_size=0.2,random_state=0)

from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)

"""GaussianNB()
In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.
"""

y_pred = classifier.predict(X_test)

from sklearn.metrics import confusion_matrix , accuracy_score
cm = confusion_matrix(y_test , y_pred)
sns.heatmap(cm , annot=True)

cm

accuracy_score(y_test , y_pred)

X_pred = np.array(['The food was delicious'])
X_pred = vectorizer.transform(X_pred).toarray()
classifier.predict(X_pred)

X_pred = np.array(['Asha is bad girl'])
X_pred = vectorizer.transform(X_pred).toarray()
classifier.predict(X_pred)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 09:39:50 2018

@author: linguista
"""

import nltk
#nltk.download()
from nltk.book import *

# Que texto é este?
print(text1.name)

# Vejamos quantas palavras:
print(str(len(text1)));

# Vejamos quantos termos diferentes:
print(str(len(set(text1))));

# Vejamos a presença destas palavras (“big” e “monstrous”)
text1.concordance("monstrous")
text1.concordance("big")

text1.dispersion_plot(["monstrous", "animal", "big", "terrible", "dangerous"])


# ---------------------------------------------------------

data = [];
y = [];
file = open('spam.txt', 'r')
text_full = file.read().lower();
text = text_full.split('\n');

for row in text:
	if(row[:3]=='ham'):
		classe = 'ham';
		content = row[4:]
		y.append(0);
	else:
		classe = 'spam';
		content = row[5:]
		y.append(1);
	data.append([classe, content])
file.close();

# Mais loads
from nltk.corpus import stopwords
porter = nltk.PorterStemmer()
stopWords = set(stopwords.words('english'))
from nltk.corpus import wordnet

import numpy as np

attributes = [];

vocab = set(nltk.word_tokenize(text_full));
print('Vocabulario inicial dos emails: '+str(len(vocab)));


# Uso de tokenizers
for token in vocab:    
	if(not(token in stopWords) and len(wordnet.synsets(token))>0):
        	token = porter.stem(token); 
	if(not(token in attributes)):
        	attributes.append(token);

print('Vocabulario final dos emails: '+str(len(attributes)));


# --------------------------------------------------
# Bag-of-word
bow = np.zeros([len(data), len(attributes)]);
i = 0;
for row in data:
	row = nltk.word_tokenize(row[1]);
    
	for word in row:
		word = porter.stem(word);
		if(word in attributes):
        		indice = attributes.index(word);
        		bow[i][indice] += 1;       	 
	i+=1;
X = bow;

# MNB - treinamento
from sklearn.naive_bayes import MultinomialNB
gnb = MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)
gnb_trained = gnb.fit(X[:4000], y[:4000])
y_pred = gnb_trained.predict(X[4000:])

print('Taxa de acerto de: '+str(sum(y_pred == y[4000:])/len(y_pred)))
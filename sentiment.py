#!/bin/python
# coding: utf-8

from nltk.tokenize import word_tokenize
from nltk import pos_tag, download
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
from nltk.corpus import sentiwordnet as swn
import string

lemmatizer = WordNetLemmatizer()


def remove_punctuation(text):
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)


def transform_tag(tag):
    if tag.startswith('J'):
        return wn.ADJ
    elif tag.startswith('N'):
        return wn.NOUN
    elif tag.startswith('R'):
        return wn.ADV
    elif tag.startswith('V'):
        return wn.VERB
    return None


# In[16]:


def get_synsets(word, tag):
    tags = ['NN', 'VB', 'JJ', 'RB']
    if (tag in tags):
        tag = transform_tag(tag)
        lemma = lemmatizer.lemmatize(word, pos=tag)
        synsets = wn.synsets(lemma, pos=tag)
        if (synsets):
            return synsets[0]
        else:
            return None
    else:
        return None


def get_score(review):
    text = remove_punctuation(review)
    words = word_tokenize(text)
    tagged = pos_tag(words)
    pos = neg = obj = count = 0
    for word, tag in tagged:
        synset = get_synsets(word, tag)
        if synset:
            swn_synset = swn.senti_synset(synset.name())
            pos = pos + swn_synset.pos_score()
            neg = neg + swn_synset.neg_score()
            obj = obj + swn_synset.obj_score()
            count += 1
    final_score = pos - neg
    return round(final_score, 2)


def get_score_label(value):
    if (value > 0):
        return 'positivo'
    elif(value < 0):
        return 'negativo'
    else:
        return 'neutro'


def get_score_label(value):
    if (value > 0):
        return 'positivo'
    if(value < 0):
        return 'negativo'
    return 'neutro'


phrase_pos = 'Barack Obama was a good president'
phrase_neg = 'this car is bad'
phrase_neu = 'I lost my book'

score = get_score(phrase_pos)
print('{0} => {1} '.format(phrase_pos, get_score_label(score)))
score = get_score(phrase_neg)
print('{0} => {1}'.format(phrase_neg, get_score_label(score)))
score = get_score(phrase_neu)
print('{0} => {1}'.format(phrase_neu, get_score_label(score)))

import pandas as pd
import numpy as np
import glob
import docx

from sklearn.feature_extraction.text import TfidfVectorizer
from operator import itemgetter
from string import digits

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import word_tokenize
from nltk import tokenize
from nltk.util import ngrams

def SentimentScore(paragraph, weight=1.5):
    sentences = []
    lines_list = tokenize.sent_tokenize(paragraph)
    sentences.extend(lines_list)
    sid = SentimentIntensityAnalyzer()
    sentiment = 0
    for sentence in sentences:
        ss = sid.polarity_scores(sentence)
        score = ss['compound']
        if score < 0:
            sentiment += score*weight
        else:
            sentiment += score
    return round(sentiment/len(sentences),2)

def neg(bucket):
    if bucket < 4:
        return bucket + 4
    else:
        return bucket - 4
    
def remove_nan(l):
    return [x for x in l if not pd.isnull(x)]

def bin_of_words(filename):
    df = pd.read_excel(filename)
    return [sorted(list(set(remove_nan(df[col].values)))) for col in df.columns]

negators = ['no', 'not', 'lack', 'never', 'none', 'neither', 'nobody', 'few', 'hardly',\
            'little', 'rarely', 'scarcely', 'seldom']

def main(text):
	remove_digits = str.maketrans('', '', digits)
	text = text.lower().translate(remove_digits)
	vader_score = SentimentScore(text)
	

if __name__ == "__main__":
    
    main()

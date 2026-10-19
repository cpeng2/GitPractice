import nltk
from nltk.corpus import stopwords
from collections import Counter

with open('romeojuliet.txt', 'r') as file:
    wc = Counter()
    stop_words = set(stopwords.words('english'))
    punctuation = set('!()-[]{};:\'"\\,<>./?@#$%^&*_-~`')
    for line in file:
        words = line.split()
        for word in words:
            word = word.lower()
            for char in punctuation:
                word = word.replace(char, '')
            if word not in stop_words:
                wc[word] += 1
    print(wc.most_common(10))
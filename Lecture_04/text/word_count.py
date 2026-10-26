from collections import Counter

with open('romeojuliet.txt', 'r') as file:
    wc = Counter()
    for line in file:
        words = line.split()
        for word in words:
            wc[word.lower()] += 1
    print(wc.most_common(5))
        

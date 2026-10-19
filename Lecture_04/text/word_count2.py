wc = {}

with open('romeojuliet.txt', 'r') as file:
    for line in file:
        words = line.split()
        for word in words:
            word = word.lower()
            if word in wc:
                wc[word] += 1
            else:
                wc[word] = 1
    sorted_wc = sorted(wc.items(), key=lambda x: x[1], reverse=True)
    print(sorted_wc[:10])
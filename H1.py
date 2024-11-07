from collections import Counter
with open("Text.txt", "r")as file:
    words = file.read().lower().replace(".","").replace(",","").split()
word_count = Counter(words)
for word, count in word_count.most_common(7):
    print(word,":", count)
import random

# Read in all the words in one go
with open("input.txt") as f:
    text = f.read()

# TODO: analyze which words can follow other words
words = text.split()
cache = {}
for item in range(len(words) - 1):
    word = words[item]
    if word in cache:
        cache[word].append(words[item + 1])
    else:
        cache[word] = [words[item + 1]]
print(cache)

# TODO: construct 5 random sentences
# Your code here


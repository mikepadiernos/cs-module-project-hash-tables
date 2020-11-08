def histo(s):
    filtered = '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'
    cache = {}
    words = s.split()
    # print(words)
    for word in words:
        word = word.strip(filtered).lower()
        # print(word)
        if word in cache:
            cache[word] += 1
        else:
            cache[word] = 1
    sort_words = sorted(cache.items(), key=lambda x: x[1], reverse=True)
    for word in sort_words:
        print(word[0] + (' ' * (17 - len(word[0]))) + ('#' * int(word[1])))


if __name__ == "__main__":
    f = open("robin.txt", 'r')
    text = f.read()
    print(histo(text))

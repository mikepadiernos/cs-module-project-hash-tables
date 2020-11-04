

def word_count(s):
    filtered = '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'
    string = s.split()
    cache = {}
    for word in string:
        word = word.strip(filtered).lower()
        if not word:
            break
        if word in cache:
            cache[word] += 1
        else:
            cache[word] = 1
    return cache


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))

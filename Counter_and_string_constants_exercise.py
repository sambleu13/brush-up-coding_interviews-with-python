from collections import Counter
import string

words = "if there was there was if there was not there was not".split()
print(words)
counts = Counter(words)
print(counts)
print(counts.most_common(2))

def is_lower(word):
    for letter in word:
        if letter not in string.ascii_lowercase:
            return False
        return True
        
print({word: is_lower(word) for word in counts})

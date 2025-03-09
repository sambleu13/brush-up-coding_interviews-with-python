import re
from collections import defaultdict

def rare_words_finder(text):
    # implement this
    rare_words = defaultdict(int)
    least_common = []
    if text != '':
        lower_text = text.lower()
        words = lower_text.split()
        for word in words:
            if word in words:
                rare_words[word] += 1
            else:
                rare_words[word] = 1
        least_common = sorted(rare_words.items(), key= lambda x:x[1])
        return least_common[0:5]
    else:
        return least_common

print(rare_words_finder("Hey there hot shot Are you ready for a challenge This might be trickier than it looks")) # Expected Output: [('hey', 1), ('there', 1), ('hot', 1), ('shot', 1), ('are', 1)]

print(rare_words_finder("The quick brown fox jumps over the lazy dog The fox is quick but the dog is lazy")) # Expected Output: [('brown', 1), ('jumps', 1), ('over', 1), ('but', 1), ('quick', 2)]

print(rare_words_finder("")) # Expected Output: []

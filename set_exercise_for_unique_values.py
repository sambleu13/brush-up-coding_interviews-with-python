#Call get_random_word() repeatedly to get 1000 random words 
#and then return a data structure containing every unique word. 

import random

all_words = "all the words in the world".split()

def get_random_word():
    return random.choice(all_words)

# solution 

def get_unique_words():
    uniqueWords = set()
    for _ in range(1000):
        uniqueWords.add(get_random_word())

    return uniqueWords
    
print(get_unique_words())

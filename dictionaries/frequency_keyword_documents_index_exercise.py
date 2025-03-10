# we got gazillion documents in the universe, each represented as a string in a list. 
# Your task is to whip up an index that's as nifty as a dictionary which logs in every 
# unique word from these documents. Now, don't forget, each unique word is a key, 
# mapping to another dictionary where the key is the document index and the value 
# is how many times that word appeared in the document. 
# It's sure gonna make searching a lot quicker, kinda like quantum speed, eh? Let's get rollin'!

# Ensure that your code handles all the edge cases. The input would be a list, 
# where each string inside the list is a document. And every string is just 
# a regular english text, easy peasy.

# The output should be a dictionary, where each unique word is a key, and the mapped value 
# should be another dictionary, having document index as the key and its corresponding word 
# count as the value.



from collections import defaultdict

def keyword_index(docs):
    # implement this
    key_index = defaultdict(lambda: defaultdict(int))
    empty_docs = 0
    if len(docs) != 0:
        for i, doc in enumerate(docs):
            if doc:
                doc_words = doc.split()
                for word in doc_words:
                    if word in key_index:
                        key_index[word][i] += 1
                        print("new doc", key_index[word])
                    else:
                        key_index[word][i] = 1
                        dict(key_index[word])
                        print("new word",word,i,1)
    return dict(key_index)

docs = ["Hello world", "world of python", "python is a snake"]
print(keyword_index(docs))  # Expected output: {'Hello': {0: 1}, 'world': {0: 1, 1: 1}, 'of': {1: 1}, 'python': {1: 1, 2: 1}, 'is': {2: 1}, 'a': {2: 1}, 'snake': {2: 1}}

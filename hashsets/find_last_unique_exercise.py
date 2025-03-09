def find_unique_string(words):
    # implement this
    uniques = set()
    duplicates = set()
    last_i = 0
    words = [word.strip() for word in words]
    if words != []:
        for i, word in enumerate(words):
            if word not in uniques:
                uniques.add(word)
                last_i = i
            else:
                duplicates.add(word)
        if uniques != {}:
            if words[last_i] not in duplicates:
                return words[last_i]
            else:
                return ''
        else:
            return ''
    else:
        return ''
    

print(find_unique_string(['apple', 'banana', 'apple', 'mango', 'banana']))  # It should print: 'mango'
print(find_unique_string(['hello', 'world', 'hello']))  # It should print: 'world'
print(find_unique_string(['hello', 'world', 'hello', 'world']))  # It should print: ''
print(find_unique_string([]))  # It should print: ''

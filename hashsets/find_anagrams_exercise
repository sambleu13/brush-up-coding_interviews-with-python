def find_anagram_words(list_1, list_2):
    # implement this
    output = []
    if list_1 != []:
        sorted_list1_tuple = set(tuple(sorted(word)) for word in list_1)
        sorted_list2_tuple = set(tuple(sorted(word)) for word in list_2)
        common_tuple = sorted_list1_tuple & sorted_list2_tuple
        list_1_out = [word for word in list_1 if tuple(sorted(word)) in common_tuple]
    return list_1_out


print(find_anagram_words(['cinema', 'iceman'], ['iceman', 'cinema'])) # should return ['cinema', 'iceman']
print(find_anagram_words(['test', 'stet'], ['tent', 'nett'])) # should return []
print(find_anagram_words(['hello', 'world'], ['dolly', 'sir'])) # should return []

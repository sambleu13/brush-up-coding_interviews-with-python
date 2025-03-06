#double each letter of a word

#define a function
def doublechar(word):
    #create new word as strings are inmutable
    newword = ''
    for i, char in enumerate(word):
        newword +=char+char
        #add the double letter to the end of the string
    return newword

print(doublechar('Samantha'))

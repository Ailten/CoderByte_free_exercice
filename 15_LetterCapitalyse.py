
# Letter Capitalyse (Easy).
# (?)

# take a sentence in string, and return same, but eatch word in sentence has the first lettre in upper case.



def capitalyse(sentence):

    return ' '.join([ word[0].upper() + word[1:] for word in sentence.split()])



print(capitalyse('hello word'))
print(capitalyse('good morning'))
print(capitalyse('how are you ?'))
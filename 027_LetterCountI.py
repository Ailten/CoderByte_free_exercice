
# Letter Count I (Easy).
# (?)

# find the first word in a line string who has the bigest amount of letter repetition. if there are no word with repetition, return -1.


def letterCountI(line):

    words = line.split()
    word_find = None
    amount_of_repetition = 0
    for w in words:

        current_amount_of_repetition = howManyRepetition(w)
        if current_amount_of_repetition > amount_of_repetition:
            word_find = w
            amount_of_repetition = current_amount_of_repetition

    if amount_of_repetition == 0:
        return -1
    return word_find


def howManyRepetition(word):
    dico = dict()
    for char in word:
        if char in dico:
            dico[char] += 1
            continue
        dico.update({char: 1})

    arr = [ (k, v) for k,v in dico.items() ]
    arr.sort(key=lambda e: e[1], reverse=True)

    return arr[0][1] if arr[0][1] > 1 else -1


print(letterCountI('abc'))
print(letterCountI('abc aabc'))
print(letterCountI('abc aabc aaabc'))
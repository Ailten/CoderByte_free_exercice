
# Text Justification.
# https://leetcode.com/problems/text-justification/


def txtJustification(words: list[str], max_width: int) -> list[str]:

    if len(words) == 0:
        return []

    output = []

    index_first_word_taken = 0
    index_last_word_taken = 1
    char_size = len(words[0])
    words_taken_count = 1
    while index_last_word_taken < len(words):
        current_word = words[index_last_word_taken]
        len_word = len(current_word)
        words_taken_back = words_taken_count - 1

        # make a new line without current word.
        if char_size + words_taken_back + len_word > max_width:
            dif_space = max_width - char_size
            space_add_between_all = dif_space // words_taken_back
            space_add_between_first = dif_space % words_taken_back
            # append the new line.
            output.append((' '*space_add_between_all).join([ (
                words[i] +
                (' '*space_add_between_first if i == index_first_word_taken else '')
            ) for i in range(index_first_word_taken, index_last_word_taken) ]))
            # re ajust double index.
            char_size = len_word
            index_first_word_taken = index_last_word_taken
            index_last_word_taken += 1
            words_taken_count = 1
            continue

        # update index and size for current line eval.
        char_size += len(current_word)
        index_last_word_taken += 1
        words_taken_count += 1

    # add the last line.
    output.append(''.join([ (
        words[i] +
        (' ' if i != len(words) -1 else '')
    ) for i in range(index_first_word_taken, len(words)) ]).ljust(max_width, ' '))

    return output


max_width_param = 16
result = txtJustification([
    "This", "is", "an", "example", "of", "text", "justification."
], max_width_param)
print(
    '╔'+('═'*(max_width_param+2))+'╗\n║ ' + 
    ' ║\n║ '.join(result) + 
    ' ║\n╚'+('═'*(max_width_param+2))+'╝'
)
# result expected
#   "This    is    an",
#   "example  of text",
#   "justification.  "

#  ╔══════════════════╗
#  ║ This    is    an ║
#  ║ example  of text ║
#  ║ justification.   ║
#  ╚══════════════════╝
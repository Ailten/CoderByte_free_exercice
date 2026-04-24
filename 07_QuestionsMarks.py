
# Questions Marks (easy).
# https://coderbyte.com/information/Questions%20Marks

def QuestionsMarks(strParam):

  is_pair_num_found = False

  for i in range(len(strParam)):
    char_start = strParam[i]

    if not is_a_num(char_start):
      continue

    first_num = int(char_start)

    question_mark_count = 0
    for j in range(i + 1, len(strParam)):
      char_end = strParam[j]

      if char_end == '?':
        question_mark_count += 1
        continue

      if not is_a_num(char_end):
        continue

      second_num = int(char_end)
      if first_num + second_num == 10:
        is_pair_num_found = True
        if question_mark_count != 3:
          return False
        break

  return is_pair_num_found





def is_a_num(char):
  return char in '123456789'


# keep this function call here 
print(QuestionsMarks('---4abc??-?z6---'))
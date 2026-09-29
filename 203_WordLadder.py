
# Word Ladder
# https://leetcode.com/problems/word-ladder/


def ladderLength(begin_word: str, end_word: str, word_list: list[str]) -> int:

    def charDifCount(word_a: str, word_b: str) -> int:
        count_dif = 0
        for i in range(len(word_a)):
            if word_a[i] != word_b[i]:
                count_dif += 1
        return count_dif
    
    word_reach: list[int] = [ w for w in word_list if charDifCount(begin_word, w) == 1 ]
    if len(word_reach) == 0:
        return 0
    
    # optimise, by poping word reach from list (no need to reach many time the same).
    for w in word_reach:
        word_list.remove(w)
    
    count_word = 2

    while True:
        new_word_reach: list[int] = []
        for w in word_reach:

            if w == end_word:  # end loop.
                return count_word
            
            for new_w_id in range(len(word_list) -1, -1, -1):
                new_w = word_list[new_w_id]
                if charDifCount(new_w, w) == 1:
                    new_word_reach.append(new_w)
                    word_list.pop(new_w_id)
        
        word_reach = new_word_reach
        count_word += 1

        if len(word_reach) == 0:  # no path valid.
            return 0
        

print(ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))  # 5.
print(ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]))  # 0.
            

            


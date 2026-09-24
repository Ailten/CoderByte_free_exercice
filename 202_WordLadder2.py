
# word ladder 2
# https://leetcode.com/problems/word-ladder-ii/


def findLadders(begin_word: str, end_word: str, word_list: list[str]) -> list[list[str]]:

    def charDifCount(word_a: str, word_b: str) -> int:
        count_dif = 0
        for i in range(len(word_a)):
            if word_a[i] != word_b[i]:
                count_dif += 1
        return count_dif
    
    paths = [[begin_word]]
    is_match_end = False

    while not is_match_end:

        new_paths = []
        for path in paths:
            last_word_path = path[len(path)-1]

            for word in word_list:
                if charDifCount(last_word_path, word) != 1:
                    continue
                if word in path:  # skip loop or back path.
                    continue

                new_paths.append(path + [word])

                if word == end_word:
                    is_match_end = True

        if len(new_paths) == 0:  # no path found.
            return []

        paths = new_paths

    paths = [p for p in paths if p[len(p)-1] == end_word]

    return paths


print(findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"]))  # 2 results.
#  "hit" -> "hot" -> "dot" -> "dog" -> "cog"
#  "hit" -> "hot" -> "lot" -> "log" -> "cog"
print(findLadders("hit", "cog", ["hot","dot","dog","lot","log"]))  # 0 result.


# Word break.
# https://leetcode.com/problems/word-break/


def wordBreak(s: str, wordDict: list[str]) -> bool:

    # return every word who can start by.
    def getWordsStarting(s: str, wordDict: list[str]) -> list[str]:
        return [wd for wd in wordDict if s.startswith(wd)]
    
    # block of data for one node of path word.
    class wordPath:
        def __init__(self, words_allow: list[str]):
            self.words_allow = words_allow
            self.current_id = 0

    path: list[wordPath] = []
    index_s = 0
    while index_s < len(s):

        s_crop = s[index_s:]
        
        words_can_start = getWordsStarting(s_crop, wordDict)  # get all next word allow.

        if len(words_can_start) > 0:  # if found at least one.
            path.append(wordPath(words_can_start))
            index_s += len(words_can_start[0])
            continue

        # if no word allow next in the path, back track.
        while True:

            if len(path) == 0:  # back track at the start.
                return False

            last_word = path[len(path)-1]
            index_s -= len(last_word.words_allow[last_word.current_id])

            # if there is other word to try at this node, try next one.
            if last_word.current_id < len(last_word.words_allow) -1:
                last_word.current_id += 1
                index_s += len(last_word.words_allow[last_word.current_id])
                break

            # if every word at this node is try, move to previous node.
            path.pop()

    # debug.
    print([n.words_allow[n.current_id] for n in path])

    return True  # all string completed.


print(wordBreak("leetcode", ["leet","code"]))  # True.
print(wordBreak("applepenapple", ["apple","pen"]))  # True.
print(wordBreak("catsandog", ["cats","dog","sand","and","cat"]))  # False.

print(wordBreak("aabba", ["a","ba","aab"]))  # True.

 
 
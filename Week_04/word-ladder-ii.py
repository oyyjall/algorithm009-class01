from collections import defaultdict
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if not wordList or not beginWord or not endWord or endWord not in wordList:
            return []
        wordSet = set(wordList)
        layer = {}
        layer[beginWord] = [[beginWord]]

        while layer:
            newlayer = defaultdict(list)
            for curWord in layer:
                if curWord == endWord:
                    return layer[curWord]
                for i in range(len(curWord)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        nextWord = curWord[:i] + c + curWord[i+1:]
                        if nextWord in wordSet:
                            newlayer[nextWord] += [j + [nextWord] for j in layer[curWord]]
            wordSet -= set(newlayer.keys())
            layer = newlayer
        return []
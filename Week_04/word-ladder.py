from collections import defaultdict
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not wordList or not beginWord or not endWord or endWord not in wordList:
            return 0
        wordDict = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                temp = word[:i] + '_' + word[i+1:]
                wordDict[temp].append(word)
        # print(wordDict)
        
        queue, visited = deque([(beginWord, 1)]), set()
        while queue:
            curWord, step = queue.popleft()
            if curWord not in visited:
                visited.add(curWord)
                if curWord == endWord:
                    return step
                for i in range(len(curWord)):
                    tmp = curWord[:i] + '_' + curWord[i+1:]
                    for nextWord in wordDict[tmp]:
                        if nextWord not in visited:
                            queue.append((nextWord, step + 1))
        return 0
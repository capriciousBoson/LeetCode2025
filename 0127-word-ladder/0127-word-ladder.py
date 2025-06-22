from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        
        words = set(wordList)
        k = len(endWord)
        chars = defaultdict(set)

        for word in wordList:
            for i in range(k):
                chars[i].add(word[i])

        print(chars)

        Q = deque()
        Q.append((1,beginWord))

        while Q:
            l,word = Q.popleft()

            for i in range(k):
                for char in chars[i]:
                    newWord = word[:i]+char+word[i+1:]
                    if newWord==endWord : return l+1
                    if newWord in words:
                        Q.append((l+1, newWord))
                        words.remove(newWord)
        return 0
                    
                        

            
            
        
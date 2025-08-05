class Solution:
    def findLadders(self, beginWord: str, endOfWord: str, wordList: List[str]) -> List[List[str]]:
        word_set = set(wordList)
        if endOfWord not in word_set: 
            return []

        level = {beginWord}
        visited = set()
        found = False
        parents = defaultdict(set)
        while level and not found: 
            next_level = set()
            for word in level: 
                visited.add(word)
            for word in level: 
                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        new_word = word[:i] + c + word[i + 1:]
                        if new_word in word_set and new_word not in visited:
                            if new_word == endOfWord: 
                                found = True 
                            next_level.add(new_word)
                            parents[new_word].add(word)
            level = next_level

        res = []
        def dfs(word, path):
            if word == beginWord:
                res.append(path[::-1])
                return 

            for p in parents[word]:
                dfs(p, path + [p])

        if found: 
            dfs(endOfWord, [endOfWord])

        return res
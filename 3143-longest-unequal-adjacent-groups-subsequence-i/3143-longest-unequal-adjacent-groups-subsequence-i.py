class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        ans = [words[0]]
        last = groups[0]
        for i in range(1, len(groups)): 
            if groups[i] != last: 
                ans.append(words[i])
            last = groups[i]

        return ans
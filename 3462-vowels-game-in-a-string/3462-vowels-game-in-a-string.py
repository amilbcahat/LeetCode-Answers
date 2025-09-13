class Solution:
    def doesAliceWin(self, s: str) -> bool:
        #Editorial - https://leetcode.com/problems/vowels-game-in-a-string/editorial/?envType=daily-question&envId=2025-09-12
        return any(c in 'aeiou' for c in s)
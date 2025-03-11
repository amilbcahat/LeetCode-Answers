class Solution:
    def countOfSubstrings(self, s: str, n: int) -> int:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        #consonants are not vowels 

        def atLeastK(k):
            vowelMap = {}
            l = 0 
            res = 0 
            con = 0

            for r in range(len(s)):
                if s[r] in vowels:
                    vowelMap[s[r]] = 1 + vowelMap.get(s[r], 0)
                else: 
                    con += 1

                while len(vowelMap) == 5 and con >= k:
                    res += (len(s) - r) 
                    if s[l] in vowelMap:
                        vowelMap[s[l]] -= 1
                        if vowelMap[s[l]] == 0:
                            del vowelMap[s[l]]
                    else:
                        con -= 1
                    l += 1

            return res

        return atLeastK(n) - atLeastK(n + 1)

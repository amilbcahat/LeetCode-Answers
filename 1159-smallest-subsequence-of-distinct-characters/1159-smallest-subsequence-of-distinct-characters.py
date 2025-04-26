class Solution:
    def smallestSubsequence(self, s: str) -> str:
        #https://leetcode.com/submissions/detail/1618683706/ <- Explanation here 
        countMap = Counter(s)
        countMap[s[0]] -= 1 
        stack = [s[0]]
        seen = set()

        for c in s[1:]: 
            if c not in seen: 
                while stack and stack[-1] >= c and countMap[stack[-1]] > 0:
                    if stack[-1] in seen: 
                        seen.remove(stack[-1])
                    stack.pop()

                if stack: 
                    seen.add(stack[-1])

                stack.append(c)
            countMap[c] -= 1

        return "".join(stack)
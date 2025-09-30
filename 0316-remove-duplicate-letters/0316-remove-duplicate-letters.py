class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        countMap = Counter(s)
        # countMap[s[0]] -= 1
        seen = set()
        stack = [s[0]]
        for c in s: 
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
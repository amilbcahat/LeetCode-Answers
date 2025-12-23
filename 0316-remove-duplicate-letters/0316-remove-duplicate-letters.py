class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = Counter(s)
        seen = set()
        stack = []

        for c in s: 
            if c not in seen: 
                while stack and stack[-1] > c and count[stack[-1]] > 0: 
                    elem = stack.pop()
                    seen.remove(elem)

                stack.append(c)
                seen.add(c)
            count[c] -= 1

        return "".join(stack)
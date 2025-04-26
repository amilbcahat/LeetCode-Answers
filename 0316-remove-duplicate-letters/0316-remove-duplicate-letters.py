class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        

        countMap = Counter(s)
        fix = set()
        stack = [s[0]]
        countMap[s[0]] -= 1
        totalKeys = len(countMap.keys())
        for c in s[1:]: 
            if c not in fix: 
                while stack and stack[-1] >= c and countMap[stack[-1]] > 0:
                    if stack[-1] in fix: 
                        fix.remove(stack[-1])
                    stack.pop()
                
                if stack: 
                    fix.add(stack[-1])
                stack.append(c)
            countMap[c] -= 1
        
        return "".join(stack)
        
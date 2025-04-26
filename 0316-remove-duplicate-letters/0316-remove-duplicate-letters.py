class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # Intuition:
        # Use monotonic stack to maintain lexicographically smallest result
        # while ensuring each letter appears exactly once
        
        # 1. If we have more occurrences of a character later in the string,
        #    and we find a smaller character now, we can pop the larger character
        #    from our stack and use its later occurrence instead
        
        # 2. 'seen' set tracks characters currently in our stack to avoid duplicates
        #    If a character is already in our result, we skip it even if it would
        #    normally improve the lexicographical order
        
        countMap = Counter(s)
        seen = set()
        stack = []
        
        for c in s:
            # Decrease the counter for this character
            countMap[c] -= 1
            
            # Skip if we've already used this character in our result
            if c in seen:
                continue
                
            # If current character is smaller than the last character in stack,
            # and that last character still has occurrences later in the string,
            # we can safely remove it and use a later occurrence
            while stack and stack[-1] > c and countMap[stack[-1]] > 0:
                # Remove from seen set and stack
                seen.remove(stack[-1])
                stack.pop()
                
            # Add current character to our result
            stack.append(c)
            seen.add(c)
            
        return "".join(stack)
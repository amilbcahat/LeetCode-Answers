class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()  # Initialize a set to keep track of unique characters in the current window
        l = 0  # Left pointer of the sliding window
        res = 0  # Result variable to store the maximum length of substring found

        for r in range(len(s)):  # Right pointer of the sliding window
            while s[r] in charSet:  # If the character at right pointer is already in the set
                charSet.remove(s[l])  # Remove the character at left pointer from the set
                l += 1  # Move the left pointer to the right

            charSet.add(s[r])  # Add the character at right pointer to the set
            res = max(res, r - l + 1)  # Update the result with the maximum length of the current substring

        return res  # Return the maximum length of substring found

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        def rev_str(l):
            nonlocal s
            r = n - l - 1

            if l >= r: 
                return 

            s[l], s[r] = s[r], s[l]

            rev_str(l + 1)

            return s

        return rev_str(0)

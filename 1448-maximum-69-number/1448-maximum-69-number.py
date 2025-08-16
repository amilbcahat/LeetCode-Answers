class Solution:
    def maximum69Number (self, num: int) -> int:
        st = list(str(num))

        for i in range(len(st)): 
            if st[i] != "9": 
                st[i] = "9"
                break 

        return int("".join(st)) 

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        arr = list(s)
        res = set()
        def backtrack(i, curArr): 
            nonlocal res
            print(curArr)
            if i >= len(arr):
                res.add(''.join(curArr))
                return

            if ord('a') <= ord(curArr[i]) <= ord('z') or ord('A') <= ord(curArr[i]) <= ord('Z'):
                #Change to lowercase 
                curArr[i] = chr(ord(curArr[i]) & ord('_'))
                backtrack(i + 1, curArr)
                #change to uppercase
                curArr[i] = chr(ord(curArr[i]) | ord(' '))
                backtrack(i + 1, curArr)
            else: 
                backtrack(i + 1, curArr)

        backtrack(0, arr)
        return list(res)
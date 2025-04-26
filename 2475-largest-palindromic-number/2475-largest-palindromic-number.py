class Solution:
    def largestPalindromic(self, num: str) -> str:
        countMap = Counter(num)

        if countMap["0"] == len(num): 
            return "0"

        even = []
        odd = []
        zero = 0 
        length = 0
        for key in countMap: 
            if countMap[key] >= 2: 
                mod = countMap[key] % 2
                even.append((key, countMap[key] - mod))
                if mod == 1:
                    odd.append(key)
                length += countMap[key]
            elif countMap[key] == 1: 
                odd.append(key)

        odd.sort()
        even.sort()
        print(odd)
        if odd: 
            length += 1
        res = [""] * length


        if (len(even) == 1 and even[0][0] == "0") or len(even) == 0: 
            if len(odd): 
                return odd[-1]

        #populate
        if odd:
            mid = length // 2
            res[mid] = odd[-1]

        # print(even, countMap)
        i = 0
        for n in even[::-1]:
            num, count = n
            while count != 0: 
                res[i] = res[length - i - 1] = num
                count -= 2  
                i += 1

        return "".join(res)
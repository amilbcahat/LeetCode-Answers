class Solution:
    def sortVowels(self, s: str) -> str:
        #Counting sort
        count = [0] * 58
        s = list(s)
        for i, c in enumerate(s):
            if c in 'aeiouAEIOU':
                count[ord(c) - ord('A')] += 1
                s[i] = ""

        p = 0
        for i, c in enumerate(s):
            if s[i] == "":
                while p < len(count) and count[p] == 0:
                    p += 1

                s[i] = chr(p + ord('A'))
                count[p] -= 1

        return "".join(s)

        # arr = list(s)
        # minHeap = []
        # for i,c in enumerate(s): 
        #     if c in "aeiouAEIOU": 
        #         arr[i] = ""
        #         heapq.heappush(minHeap, c)

        # for i in range(len(s)): 
        #     if arr[i] == "":
        #         arr[i] = heapq.heappop(minHeap)

        # return "".join(arr)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #to maintain char to their freq
        count = {}
        #To maintain freq(used as index) to list of char with that freq
        freq = [[] for i in range(len(nums)+1)]

        for n in nums : 
            count[n] = 1 + count.get(n , 0)

        for n , c in count.items():
            #Maintains Freq to Character 
            #For eg. if somebody has 2 freq 
            #Then it will be append to 2 index list ! 
            freq[c].append(n)

        res = []

        for i in range(len(freq) - 1 , 0 , -1):
            #We iterate till 1 and skip 0 , because freq[0] means appears just 0 times 
            #Traverse from behind (For max freq)
            for n in freq[i]:
                #Append them to res 
                res.append(n)
                if len(res) == k :
                    return res 
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        #With Counting Sort Pattern
        freq_map = defaultdict(int)
        for n in arr: 
            freq_map[n] += 1
        
        n = len(arr)
        count_of_freq = [0] * (n + 1)

        for count in freq_map.values(): 
            count_of_freq[count] += 1

        remaining_unique_elem = len(freq_map)

        for f in range(1, n + 1): 
            num_to_remove = min(k // f, count_of_freq[f])

            k -= (f * num_to_remove)

            remaining_unique_elem -= num_to_remove

            if k < f: 
                return remaining_unique_elem

        return 0
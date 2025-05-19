class Solution:
   def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
       #With Counting Sort Pattern
       
       # Create a frequency map to count occurrences of each number
       freq_map = defaultdict(int)
       for n in arr:
           freq_map[n] += 1
           
       n = len(arr)
       # Array to count how many unique elements have each frequency
       # Index = frequency, Value = count of elements with that frequency
       count_of_freq = [0] * (n + 1)
       
       # Populate count_of_freq
       # For example, if 3 unique elements each appear 2 times, 
       # then count_of_freq[2] = 3
       for count in freq_map.values():
           count_of_freq[count] += 1
       
       # Track the remaining number of unique elements
       remaining_unique_elem = len(freq_map)
       
       # Process frequencies in ascending order (greedy approach)
       for f in range(1, n + 1):
           # Calculate how many unique elements with frequency f we can remove
           # We can remove at most k//f elements with frequency f
           # But we can't remove more than what exists (count_of_freq[f])
           num_to_remove = min(k // f, count_of_freq[f])
           
           # Update our remaining k budget
           # We remove num_to_remove unique elements, each appearing f times
           k -= (f * num_to_remove)
           
           # Update count of remaining unique elements
           remaining_unique_elem -= num_to_remove
           
           # If we can't remove any more complete groups of elements
           # (i.e., k is less than the next frequency we'd consider)
           # then we're done and can return the answer
           if k < f:
               return remaining_unique_elem
       
       # If we've removed all elements, return 0
       return 0
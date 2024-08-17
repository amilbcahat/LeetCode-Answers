# LeetCode-Answers

## Trees -> 
1. House Robber 3 (Return two values , in each recursive call)
2. Unique Binary Search Trees (catlan number C(i - 1)(n - i))
3. Smallest String Starting From Leaf (Take out path for each branch , reverse it , see if lexo is smaller than prev path , track it )

## Stack -> 
1. Valid Parenthesis String (Take two stacks left and ast , pop when matched with Right parentheses , then match left and ast)
2. Traverse from left , remove extra ) . Traverse from right , filter extra ( 

# Graph -> 
1.Find the Safest Path in a Grid -> Multisource BFS ,then Djikshtra to find the maximum safeness factor path and the minimum distance along it .

## Daily -> 
1. Word Search -> dfs(r , c , i)
2. Add one row to Tree -> cur.right , cur.left manipulation
3. Find the Safest Path in a Grid -> Multisource BFS ,then Djikshtra to find the maximum safeness factor path and the minimum distance along it .

## Insane Problems -> 
1. Find the Safest Path in a Grid -> Multisource BFS ,then Djikshtra to find the maximum safeness factor path and the minimum distance along it .
2. Find number of Beautiful Subsets 
3. Student Attendance Record 1 -> Pure Maths and DP 

## TCS Prime Practice -> 

### Matrices -> 

#### Day 1 

1. Zig Zag Conversion 
2. Text Justification
3. Longest Palindromic Substring
4. Pow(x ,n)
5. Tranpose Matrix
6. Diagonal Sum
7. Larget Odd Number in a string
8. Image Smoother
9. Largest Local Values in a Matrix
10. Rotate Image
11. Spiral Matrix
12. Spiral Matrix 2 (Reverse of Spiral Matrix 1)
13. Set Matrix Zeroes
14. Shift 2D -> valToPos (v // N , v % N) , posToVal (r * N +  c) [Convert 2D to 1D then rotate and get targetIndex] 
15. Largest Submatrix With Rearrangements

### Strings / Arrays / Complex DP Problems on Same -> 

#### Day 3 

1. Group Anagrams
2. Merge Sorted Array
3. Remove Element
4. Remove Duplicates from Sorted Array
5. Remove Duplicates from Sorted Array II
6. Majority Element -> Booye - Moore Algo 
7. Rotate Array -> (i - k) % len(nums) [Inspired from Shift 1D]
8. Best Time to Buy and Sell Stock -> update buyPrice , with every price to find max profit (Kadane algo)
9. Best Time to Buy and Sell Stock II -> Sell whenever see a dip , buy when see a raise , (Can use Neetcode DFS template as well)
10. Jump Game -> DP (Try the DP memo way , with False and last pos True ) . Greedy -> Move goal as you iterate backwards , on successful reachs , if goal reaches 0 then Return True else False

#### Day 4 
1. Jump Game II -> BFS , Top Down DP , Bottoms Up DP
2. Insert Delete GetRandom O(1) -> Use List + HashMap
3. Product of Array Except Self -> Prefix , Postfix
4. Gas Station -> Greeding , Eliminate Wrong cases , Then look for the Unique SOlution and use Kadane's Algo
5. Candy -> Prefix and Postfix Logic
6. Trapping Rain Water -> Two Pointer O(1) memory leftMax , rightMax on ends , leftMax of heights so far in O(n) memory.
7. Roman to Integer -> Do as told
8. Integer to Roman -> Build Own Roman List
9. Length of Last Word -> Use Pointers Efficiently
10. Length of Last Word -> Use nested loops to match prefix validity with each string in strs
11. Reverse Words in a String -> Make a function to handle moving index to skip spaces , rest would be easy
12. Find the Index of the First Occurrence in a String

#### Day 5 (Recommended)
1. Factorial Trailing Zeroes -> Divide and find the total factors of the multiples of 5 within that digit range
2. Fibonacci Number
3. Maximum Subarray -> Kadane's Algorithm
4. Reverse String
5. Valid Palindrome -> Check for isalpha by using ord(ch)
6. Linked List Cycle
7. Middle Element of Linked List
8. Merge Two Sorted Lists
9. Squares of a Sorted Array -> Two pointer at both end (neg and pos can have greatest values , so consider small of them and move pointer like that)
10. Valid Perfect Square -> Binary Search to get , mid * mid == num 
11. Sqrt(x) -> Binary Search to get mid ** 2 == x , elif mid ** 2 < x , both can have answer
12. Sort an Array -> Merge Sort , Insertion sort and Quick Sort
13. Sort Colors -> Bucket sort
14. Reverse a Linked List -> Recursive and iterative

#### Day 6 (SubArray , Substrings etc)
1. Maximum Product Subarray -> Kadane Algo , but keep mind of curMin , curMax and zero element in array
2. Palindromic Substrings -> count for even and odd Pali
3. Longest Increasing Subsequence -> dp[i] = max(dp[i] , 1 + dp[j]) if condition met 
4. LCS -> dp[i][j] = dp[i + 1][j + 1] , dp[i]j] = max(dp[i + 1][j] , dp[i][j + 1] , for specific condition
5. Longest Palindromic Subsequence -> expand outward then use LCS logic , Find LCS of s and s[::-1]
6. Longest Substring Without Repeating Characters -> Use Sliding Window
7. Minimum Size Subarray Sum -> Sliding Window
8. Subarray sum Equals K -> Calculate prefixSum and their count , see if chop = curSum - k , is available in hashmap , if yes , add to res
9. Binary Subarrays With Sum-> Sliding window can be used to calculate atmost cases , use this to calculate sum to exact goal helper(goal) - helper(goal - 1)
10. Subarray Product Less Than K -> Sliding window but with Division
11. Subarrays with K Different Integers -> Count of SubArrays with K Distinct Elements = Count of SubArrays with At Most K Distinct Elements - Count of SubArrays with At Most K-1 Distinct Elements

#### Day 8 (SubArray , Substrings etc)
1. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold -> Use Sliding Window (L : k + 1) etc logic
2. Get Equal Substrings Within Budget -> Sliding Window Basic
3. Count Number of Nice Subarrays -> No. of subarrays with exactly k odd = No. of subarrays with at most k odd - No. of subarrays with at most k-1 odd.
4. Count Number of Homogenous Substrings -> aa can be counted from res += (r - l + 1)
5. Count Subarrays With Fixed Bounds -> Algo
6. Largest Substring Between Two Equal Characters
7. Append Characters to String to Make Subsequence
8. Is Subsequence
9. Maximum Number of Vowels in a Substring of Given Length -> Sliding Window on length
10. Count Subarrays Where Max Element Appears at Least K Times . Atleast = (Total no. of possible arrays - less than k subarrays )

#### Day 12 (Rest of the questions)  
1. Count Primes -> Sieve of Eratosthenes
2. GCD
3. Decimal to Octal
4. Leap Year
5. LCM
6. Dec to Binary and Vice Versa
7. Count Primes -> Sieve of Eratosthenes

#### Day Untracked - 
1. Stacks using Queues -> Uses 2 Queues
2. Queues using Stacks -> Uses 2 Stacks
3. Special Positions in a Binary Matrix -> getColSum == 1 and sum(row) == 1
4. Maximum Odd Binary Number -> Count - 1 of 1 + count of zero  + 1
5. Pascal Triangle
6. Pascal Triangle 2 

<!---LeetCode Topics Start-->
# LeetCode Topics
## Array
|  |
| ------- |
| [0015-3sum](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0015-3sum) |
| [0036-valid-sudoku](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0036-valid-sudoku) |
| [0039-combination-sum](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0039-combination-sum) |
| [0040-combination-sum-ii](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0040-combination-sum-ii) |
| [0046-permutations](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0046-permutations) |
| [0078-subsets](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0078-subsets) |
| [0090-subsets-ii](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0090-subsets-ii) |
| [0128-longest-consecutive-sequence](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0128-longest-consecutive-sequence) |
| [0130-surrounded-regions](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0130-surrounded-regions) |
| [0152-maximum-product-subarray](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0152-maximum-product-subarray) |
| [0167-two-sum-ii-input-array-is-sorted](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0167-two-sum-ii-input-array-is-sorted) |
| [0198-house-robber](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0198-house-robber) |
| [0200-number-of-islands](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0200-number-of-islands) |
| [0213-house-robber-ii](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0213-house-robber-ii) |
| [0238-product-of-array-except-self](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0238-product-of-array-except-self) |
| [0300-longest-increasing-subsequence](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0300-longest-increasing-subsequence) |
| [0309-best-time-to-buy-and-sell-stock-with-cooldown](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0309-best-time-to-buy-and-sell-stock-with-cooldown) |
| [0322-coin-change](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0322-coin-change) |
| [0347-top-k-frequent-elements](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0347-top-k-frequent-elements) |
| [0416-partition-equal-subset-sum](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0416-partition-equal-subset-sum) |
| [0417-pacific-atlantic-water-flow](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0417-pacific-atlantic-water-flow) |
| [0494-target-sum](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0494-target-sum) |
| [0518-coin-change-ii](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0518-coin-change-ii) |
| [0695-max-area-of-island](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0695-max-area-of-island) |
| [0747-min-cost-climbing-stairs](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0747-min-cost-climbing-stairs) |
| [1036-rotting-oranges](https://github.com/amilbcahat/LeetCode-Answers/tree/master/1036-rotting-oranges) |
| [1293-three-consecutive-odds](https://github.com/amilbcahat/LeetCode-Answers/tree/master/1293-three-consecutive-odds) |
| [1706-min-cost-to-connect-all-points](https://github.com/amilbcahat/LeetCode-Answers/tree/master/1706-min-cost-to-connect-all-points) |
## Linked List
|  |
| ------- |
| [2299-merge-nodes-in-between-zeros](https://github.com/amilbcahat/LeetCode-Answers/tree/master/2299-merge-nodes-in-between-zeros) |
## Simulation
|  |
| ------- |
| [2299-merge-nodes-in-between-zeros](https://github.com/amilbcahat/LeetCode-Answers/tree/master/2299-merge-nodes-in-between-zeros) |
## Backtracking
|  |
| ------- |
| [0039-combination-sum](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0039-combination-sum) |
| [0040-combination-sum-ii](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0040-combination-sum-ii) |
| [0046-permutations](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0046-permutations) |
| [0078-subsets](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0078-subsets) |
| [0090-subsets-ii](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0090-subsets-ii) |
| [0494-target-sum](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0494-target-sum) |
## Bit Manipulation
|  |
| ------- |
| [0078-subsets](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0078-subsets) |
| [0090-subsets-ii](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0090-subsets-ii) |
## Depth-First Search
|  |
| ------- |
| [0130-surrounded-regions](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0130-surrounded-regions) |
| [0133-clone-graph](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0133-clone-graph) |
| [0200-number-of-islands](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0200-number-of-islands) |
| [0417-pacific-atlantic-water-flow](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0417-pacific-atlantic-water-flow) |
| [0695-max-area-of-island](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0695-max-area-of-island) |
| [0744-network-delay-time](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0744-network-delay-time) |
## Breadth-First Search
|  |
| ------- |
| [0130-surrounded-regions](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0130-surrounded-regions) |
| [0133-clone-graph](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0133-clone-graph) |
| [0200-number-of-islands](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0200-number-of-islands) |
| [0322-coin-change](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0322-coin-change) |
| [0417-pacific-atlantic-water-flow](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0417-pacific-atlantic-water-flow) |
| [0695-max-area-of-island](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0695-max-area-of-island) |
| [0744-network-delay-time](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0744-network-delay-time) |
| [1036-rotting-oranges](https://github.com/amilbcahat/LeetCode-Answers/tree/master/1036-rotting-oranges) |
## Union Find
|  |
| ------- |
| [0128-longest-consecutive-sequence](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0128-longest-consecutive-sequence) |
| [0130-surrounded-regions](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0130-surrounded-regions) |
| [0200-number-of-islands](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0200-number-of-islands) |
| [0695-max-area-of-island](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0695-max-area-of-island) |
| [1706-min-cost-to-connect-all-points](https://github.com/amilbcahat/LeetCode-Answers/tree/master/1706-min-cost-to-connect-all-points) |
## Matrix
|  |
| ------- |
| [0036-valid-sudoku](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0036-valid-sudoku) |
| [0130-surrounded-regions](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0130-surrounded-regions) |
| [0200-number-of-islands](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0200-number-of-islands) |
| [0417-pacific-atlantic-water-flow](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0417-pacific-atlantic-water-flow) |
| [0695-max-area-of-island](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0695-max-area-of-island) |
| [1036-rotting-oranges](https://github.com/amilbcahat/LeetCode-Answers/tree/master/1036-rotting-oranges) |
## Hash Table
|  |
| ------- |
| [0036-valid-sudoku](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0036-valid-sudoku) |
| [0128-longest-consecutive-sequence](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0128-longest-consecutive-sequence) |
| [0133-clone-graph](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0133-clone-graph) |
| [0347-top-k-frequent-elements](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0347-top-k-frequent-elements) |
## Graph
|  |
| ------- |
| [0133-clone-graph](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0133-clone-graph) |
| [0744-network-delay-time](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0744-network-delay-time) |
| [1706-min-cost-to-connect-all-points](https://github.com/amilbcahat/LeetCode-Answers/tree/master/1706-min-cost-to-connect-all-points) |
## Minimum Spanning Tree
|  |
| ------- |
| [1706-min-cost-to-connect-all-points](https://github.com/amilbcahat/LeetCode-Answers/tree/master/1706-min-cost-to-connect-all-points) |
## Heap (Priority Queue)
|  |
| ------- |
| [0347-top-k-frequent-elements](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0347-top-k-frequent-elements) |
| [0744-network-delay-time](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0744-network-delay-time) |
## Shortest Path
|  |
| ------- |
| [0744-network-delay-time](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0744-network-delay-time) |
## Math
|  |
| ------- |
| [0062-unique-paths](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0062-unique-paths) |
| [0070-climbing-stairs](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0070-climbing-stairs) |
## Dynamic Programming
|  |
| ------- |
| [0062-unique-paths](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0062-unique-paths) |
| [0070-climbing-stairs](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0070-climbing-stairs) |
| [0152-maximum-product-subarray](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0152-maximum-product-subarray) |
| [0198-house-robber](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0198-house-robber) |
| [0213-house-robber-ii](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0213-house-robber-ii) |
| [0300-longest-increasing-subsequence](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0300-longest-increasing-subsequence) |
| [0309-best-time-to-buy-and-sell-stock-with-cooldown](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0309-best-time-to-buy-and-sell-stock-with-cooldown) |
| [0322-coin-change](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0322-coin-change) |
| [0416-partition-equal-subset-sum](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0416-partition-equal-subset-sum) |
| [0494-target-sum](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0494-target-sum) |
| [0518-coin-change-ii](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0518-coin-change-ii) |
| [0747-min-cost-climbing-stairs](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0747-min-cost-climbing-stairs) |
## Memoization
|  |
| ------- |
| [0070-climbing-stairs](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0070-climbing-stairs) |
## Combinatorics
|  |
| ------- |
| [0062-unique-paths](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0062-unique-paths) |
## Binary Search
|  |
| ------- |
| [0167-two-sum-ii-input-array-is-sorted](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0167-two-sum-ii-input-array-is-sorted) |
| [0300-longest-increasing-subsequence](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0300-longest-increasing-subsequence) |
## Divide and Conquer
|  |
| ------- |
| [0347-top-k-frequent-elements](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0347-top-k-frequent-elements) |
## Sorting
|  |
| ------- |
| [0015-3sum](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0015-3sum) |
| [0347-top-k-frequent-elements](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0347-top-k-frequent-elements) |
## Bucket Sort
|  |
| ------- |
| [0347-top-k-frequent-elements](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0347-top-k-frequent-elements) |
## Counting
|  |
| ------- |
| [0347-top-k-frequent-elements](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0347-top-k-frequent-elements) |
## Quickselect
|  |
| ------- |
| [0347-top-k-frequent-elements](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0347-top-k-frequent-elements) |
## Prefix Sum
|  |
| ------- |
| [0238-product-of-array-except-self](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0238-product-of-array-except-self) |
## Two Pointers
|  |
| ------- |
| [0015-3sum](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0015-3sum) |
| [0167-two-sum-ii-input-array-is-sorted](https://github.com/amilbcahat/LeetCode-Answers/tree/master/0167-two-sum-ii-input-array-is-sorted) |
<!---LeetCode Topics End-->
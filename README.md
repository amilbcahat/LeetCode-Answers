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

#### Day 6
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

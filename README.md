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

#### Day 1 

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

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        #Monotonic Queue 
        MOD = 10 ** 9 + 7
        n = len(arr)
        result = 0  # Final sum of subarray minimums
        stack = []

        # Iterate through the array plus one extra iteration for a sentinel.
        for currentIndex in range(n + 1):
            # If we reached the end, use 0 as a sentinel value; otherwise, use the current element.
            # It helps to process all remaining elements in the stack.
            currentElement = 0 if currentIndex == n else arr[currentIndex]

            # Process elements in the stack while the current element is smaller than the element at the top.
            # Here, we maintain monotonic increasing stack.
            while stack and arr[stack[-1]] > currentElement:
                # Pop the index whose corresponding element is greater than currentElement.
                minIndex = stack.pop()
                # Determine the previous index from the stack; if the stack is empty, use -1.
                previousIndex = -1 if not stack else stack[-1]

                # Calculate the number of subarrays where arr[minIndex] is the minimum:
                # (minIndex - previousIndex) gives the count of subarrays ending at minIndex,
                # and (currentIndex - minIndex) gives the count of subarrays starting at minIndex
                # that can extend until currentIndex.
                countSubarrays = (minIndex - previousIndex) * (currentIndex - minIndex)

                # Add the contribution of arr[minIndex] for these subarrays to the result.
                result += (arr[minIndex] * countSubarrays % MOD) % MOD

            # Push the current index onto the stack for further processing.
            stack.append(currentIndex)

        return result % MOD


        #Reference - https://leetcode.com/problems/apply-operations-to-maximize-score/
        # MOD = 10 ** 9 + 7
        # leftBound = [-1] * len(arr)
        # rightBound = [len(arr)] * len(arr)
        # stack = []
        # for i, n in enumerate(arr): 
        #     # print(i, n)
        #     while stack and stack[-1][0] > n: 
        #         popElem, popIndex = stack.pop()
        #         rightBound[popIndex] = i 
        #     if stack: 
        #         leftBound[i] = stack[-1][1]
        #     stack.append((n, i))

        # res = 0
        # for i, n in enumerate(arr): 
        #     no_of_right_sub = rightBound[i] - i
        #     no_of_left_sub = i - leftBound[i]
        #     res += (no_of_right_sub * no_of_left_sub * arr[i]) 

        # return res % MOD




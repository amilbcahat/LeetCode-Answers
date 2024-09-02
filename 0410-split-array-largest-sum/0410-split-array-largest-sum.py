class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        if k > len(nums) : 
            return -1 

        #Exactly same intuition as Book Allocation Problem of Binary search 
        #Intuition for that problem is given below for better understanding 
        def countSplits(maxSplitSum) : 
            #Seeing if this maxSplitSum satisifies the number of splits , that we require 
            curSplits = 1
            curSplitSum = 0 
            for i in range(len(nums)) : 
                if curSplitSum + nums[i] <= maxSplitSum : 
                    curSplitSum += nums[i]
                else : 
                    curSplits += 1 
                    curSplitSum = nums[i]
            return curSplits 

        l = max(nums)
        r = sum(nums)

        while l <= r : 
            mid = (l + r) // 2 
            if countSplits(mid) > k : 
                l = mid + 1 
            else : 
                #Look for more minimum answer 
                #this is the polarity which contains the answer 
                r = mid - 1 

        return l #l moves to answer polarity side 

# Book Allocation Problem (https://www.naukri.com/code360/problems/allocate-books_1090540)
# def findPages(arr: [int], n: int, m: int) -> int:
    # if m > len(arr) : 
    # #When no. of students required is greater than books to be alloted 
    #     return -1 
    
    # # Write your code here
    # # Return the minimum number of pages
    # def countStudent(pages):
    #     #Allocate the pages , contigiously , as asked by the 
    #     curStudents = 1 
    #     pagesOfStudent = 0
    #     for i in range(len(arr)):
    #         if pagesOfStudent + arr[i] <= pages : 
    #             pagesOfStudent += arr[i]
    #         else : 
    #             pagesOfStudent = arr[i]
    #             curStudents += 1 

    #     return curStudents
        

    # l = max(arr) #Max pages of book a student cant hold on lower range (to allow other students to also hold , as it 
    # # it is the minimum most maximum page , here , no. of students can be larger than the no. of students required)
    # r = sum(arr) #Max pages of book that a student can hold , here the no. of students is one 

    # #Greater No. of student <= Our answer lies here <= Minimum no. of students

    # while l <= r : 
    #     curPages = (l + r) // 2 
    #     if countStudent(curPages) > m:
    #         #Find for more minimum answer 
    #         l = curPages + 1
    #     else : 
    #         #Look for answer 
    #         r = curPages - 1 

    # return l #Goes to opposite polarity and hence to answer destination
class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        #We will run Binary Search on A , because we consider that it is always smaller 
        if len(B) < len(A) : 
            A , B  = B , A 

        total = len(A) + len(B)
        half = total // 2 

        #Remember , we run binary search to do partition to find median , and for that we look over to left partition 
        l , r = 0 , len(A) - 1
        while True  : 
            i = (l + r) // 2 
            j = half - i - 2 # minus 2 is for handling 0 index cases 

            #Cases 
            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i + 1] if i + 1 < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if j + 1 < len(B) else float("inf")

            #Cross checking for lesser values 
            if Aleft <= Bright and Bleft <= Aright : 
                if total % 2 : #Odd length 

                # Why the median lies in the right partition: When the total number of elements is odd, the right partition will have one more element than the left partition, making the first element of the right partition the median.
                    return min(Aright , Bright)

                #For even case its clear 
                return (max(Aleft , Bleft) + min(Aright , Bright)) / 2 

            elif Aleft > Bright : 
                #Since Aleft is more than Bright 
                #We need choose less of A array 
                #Choosing less , ensures getting a lesser value , because arrays are sorted 
                r = i - 1
            else : 
                l = i + 1


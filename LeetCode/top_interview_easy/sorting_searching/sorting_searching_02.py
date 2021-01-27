# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        mid = left + (right - left) // 2
        
        
        # Binary search 
        while left <= right:
        
            print (left, right)
            
            if isBadVersion(mid):
                right = mid -1
                mid = (left + right) // 2
                
            # cannot find bad version    
            else:
                left = mid +1
                mid = (left + right) // 2
        
        return left
        

        

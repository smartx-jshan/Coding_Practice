class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums2:
            return nums1
        
        # nums pointer
        nums1_p = 0
        nums2_p = 0
        
        # repeat until checking all of elements in nums2
        while nums2_p != n:
            if nums2[nums2_p] <= nums1[nums1_p]:
                nums1.insert(nums1_p, nums2[nums2_p])
                nums1.pop()
                nums1_p +=1
                nums2_p +=1
            # if we searched all of elements in nums1 
            elif nums1_p == m + nums2_p:
                nums1.insert(nums1_p, nums2[nums2_p])
                nums1.pop()
                nums1_p +=1
                nums2_p +=1
            else:
                nums1_p +=1
            
                
        

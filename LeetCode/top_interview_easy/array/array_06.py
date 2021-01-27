class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # sort first!
        nums1.sort()
        nums2.sort()
        
        # nums1 --> minimize
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        size = len(nums1)
        index = 0
        while index < size:
            # nums1 not in nums2, then remove nums1 value
            if not nums1[index] in nums2:
                nums1.remove(nums1[index])
                size -=1
            # nums1 in nums2, then remove nums2 value
            else:
                nums2.remove(nums1[index])
                index +=1
            
        # remaining nums1 is intersection
        return nums1

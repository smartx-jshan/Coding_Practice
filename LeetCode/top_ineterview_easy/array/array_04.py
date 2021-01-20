class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # use dict
        a = collections.Counter(nums)
        
        for i in a:
            if a[i] >=2:
                return True
        
        return False
        

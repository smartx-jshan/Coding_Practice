class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # use hashtable
        dict = {}
        
        
        for i in range(len(nums)):
            if target - nums[i] in dict:
                return dict[target-nums[i]], i
        
            # add elements in hash table
            dict[nums[i]] = i
        

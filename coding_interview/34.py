class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        prev_elements = []
        

        def dfs (elements):
            
            if len(prev_elements) == len(nums):
                result.append(prev_elements[:])
            
            for i in elements:
                new_element = elements[:]
                new_element.remove(i)
                
                prev_elements.append(i)
                dfs (new_element)
                prev_elements.pop()
        
        dfs (nums)
        return result
        

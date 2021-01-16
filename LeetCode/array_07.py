class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        # 
        reminder = 1
        
        # calculate in reverse order
        for i in range (len(digits)-1, -1, -1):
            
            # if reminder is 0, break loop
            if reminder == 0:
                break
            
            # calculate element
            number = int(digits[i]) + reminder
            
            # if reminder == 1
            if number == 10:
                digits[i] = 0
                reminder = 1
        
            else:
                digits[i] = number
                reminder = 0
        
        # first element has reminder (ex., a = [9] --> a = [1,0])
        if reminder == 1:
            digits.insert(0, 1)
        
        return digits
            
            
            

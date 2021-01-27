class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows <=0:
            return []
        
        # initialization: a1, a2
        result = []
        a1 = [1]
        a2 = [1,1]
        result.append(a1)
        
        if numRows == 1:
            return result
        
        result.append(a2)
        if numRows == 2:
            return result
        
        # from numRows 3 to numRows
        for i in range(3, numRows+1):
            
            # first
            layer = [1]
            
            # middle
            for j in range (len(result[i-2])-1):
                layer.append(result[i-2][j]+result[i-2][j+1])
            
            # last
            layer.append(1)
            
            # append to result
            result.append(layer)
        
        return result
            

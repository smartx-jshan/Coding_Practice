class Solution:
    def reverseBits(self, n: int) -> int:
        #MASK = 0xFFFFFFF
        
        # int --> binary 
        n_bin = bin(n)[2:].zfill(32)
        #print (n_bin)
        
        # binary -> dec
        number = 0
        
        # 32 bit
        for i in range(32):
            if n_bin[i] == '1':
                number = number+ 2**i  
        
        
        return number

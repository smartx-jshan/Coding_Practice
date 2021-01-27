class Solution:
    def countAndSay(self, n: int) -> str:
    
        if n == 1:
            return "1"
        
        # temp value
        temp = "1"
        
        for i in range (2,n+1):
            # initialization
            word  = []
            count = 0
            char = '-1'
            for j in range (len(temp)):
                if temp[j] == char:
                    count +=1
                # prev_elem != current_elem
                else:
                    # register sotred element
                    if char != '-1':
                        word.append(str(count))
                        word.append(str(char))
                        count = 0
                    
                    # new element
                    char = temp[j]
                    count = 1
            # finish inner loop but count is more than one
            if count > 0:
                word.append(str(count))
                word.append(str(char))
            #print (word)
            temp = ''.join(word)
            #print (result[i])
        
        return temp

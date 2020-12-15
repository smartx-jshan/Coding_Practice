class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        
        answer = [0] * len(T)
        stack = [] # Index 
        for i in range(len(T)):
            
            while stack and T[stack[-1]] < T[i]:
                last = stack.pop()
                answer[last] = i - last
            
            stack.append(i)
        
        return answer
               

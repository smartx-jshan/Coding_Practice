class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = 0
        
        queue = collections.Counter(tasks)
        #print (queue)
        while True:
            sub_count = 0
            
            for task, _ in queue.most_common(n+1):
                sub_count +=1
                count+=1
                
                queue.subtract(task)
                queue += collections.Counter()
                
            if not queue:
                break
            
            count += n - sub_count + 1
        
        return count
            
    

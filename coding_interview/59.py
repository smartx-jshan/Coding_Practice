
        intervals.sort()
        #print (intervals)
        
        result = []
        
        first = intervals.pop(0)
        
        prev_start = first[0]
        prev_end = first[1]
        
        
        for value in intervals:
            if prev_end >= value[0] and prev_end < value[1]:
                prev_end = value[1]
            elif prev_end >= value[0] and prev_end >= value[1]:
                continue
            else:
                result.append([prev_start, prev_end])
                prev_start = value[0]
                prev_end = value[1]
        
        result.append([prev_start, prev_end])
        
        return result

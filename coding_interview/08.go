func trap(height []int) int {
    
    //예외 처리
    if len(height) == 0{
        return 0
    }
    
    var volume = 0
    var left = 0
    var right = len(height)-1
    var left_max = height[left]
    var right_max = height[right]
    
    for {
        
        if left < right {
            
            // left 맥스 갱신
            if height[left] > left_max{
                left_max = height[left]
            }
            // right 맥스 갱신
            if height[right] > right_max{
                right_max = height[right]
            }
            
            if left_max <= right_max{
                volume += left_max - height[left]
                left+=1
            }else{
                volume += right_max - height[right]
                right-=1
            }
            
        } else{
            break
        }
        
    }
    
    return volume
}

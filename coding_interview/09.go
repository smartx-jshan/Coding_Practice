import "fmt"
import "sort"

func threeSum(nums []int) [][]int {
    
    sort.Ints(nums)
    
    var result = [][]int{}
    
    for i:=0; i<len(nums)-2; i++{
        
        if i>0 && nums[i] == nums[i-1]{
            continue
        } //중복을 없애자
        
        // 간격을 좁혀가며 계산하기
        var left = i +1
        var right = len(nums)-1
        
        for left< right{
            var sum = nums[i] + nums[left] + nums[right]
            
            if sum <0{
                left +=1
            } else if sum > 0{
                right -=1
            } else{
                var temp = []int{nums[i], nums[left], nums[right]}
                
                //fmt.Println(temp)
                result = append(result, temp)
                
                for left < right && nums[left] == nums[left+1]{
                    left +=1
                }
                for left < right && nums[right] == nums[right-1]{
                    right -=1
                }
                //다 정리된 후 포인터 움직이기
                left +=1
                right -=1
            }
        }
    }
        
 
    return result
}

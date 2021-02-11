import "fmt"


func twoSum(nums []int, target int) []int {
    
    var hash = map[int]int{}
    
    for i:=0; i<len(nums); i++{
        
        value, ok:= hash[target-nums[i]]
        if ok{
            return []int{value,i}
        }
        hash[nums[i]] = i
    }
    
   
    
    //var result = []int{5,6}
    //return result
    return []int{}
}

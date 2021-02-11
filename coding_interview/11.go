import "fmt"

func productExceptSelf(nums []int) []int {
    
    var p = []int{}
    var temp = 1
    for i:=0; i< len(nums); i++{
        p = append(p, temp)
        temp = temp * nums[i]
    }
    //fmt.Println(p)
    
    var out = []int{}
    temp = 1
    for i:=len(nums)-1; i>=0; i--{
        out = append(out, temp)
        temp = temp * nums[i]
    }
    
    //fmt.Println(out)
    
    var result = []int{}
    for i:=0; i<len(nums); i++{
        var sum = p[i] * out[len(nums)-i-1]
        result = append(result, sum)
    }
    
    return result
}

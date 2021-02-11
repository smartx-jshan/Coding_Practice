import "sort"

func arrayPairSum(nums []int) int {
    
    //먼저 정렬을 해보자
    sort.Ints(nums)
    var sum = 0
    for i:=0; i< len(nums); i+=2{
        sum = sum + nums[i]
    }
    
    return sum
}

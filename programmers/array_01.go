import "sort"

func solution(array []int, commands [][]int) []int {
    
    var result = []int{}
    
    for i:= 0; i < len(commands); i++{
        
        temp := array[commands[i][0]-1:commands[i][1]] // 참조가 되기 때문에 카피로 복사해야함
        var copy_temp = make([]int, len(temp)) // 초기화를 해야함
        
        copy(copy_temp, temp) // copy_temp로 복사
        sort.Ints(copy_temp) // 정렬
        
        result = append(result, copy_temp[commands[i][2]-1])
        
    }
    
    
    return result
}

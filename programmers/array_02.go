//import "fmt"
import "sort"
import "strconv"


func solution(numbers []int) string {
    
    //비교 연산자를 통한 정렬 nlogn
    sort.Slice(numbers, func(i,j int) bool{
        var s1 = strconv.Itoa(numbers[i]) + strconv.Itoa(numbers[j])
        var s2 = strconv.Itoa(numbers[j]) + strconv.Itoa(numbers[i])
        return s1 > s2
    })
    
    var answer = ""
    for i:= 0; i< len(numbers); i++{
        answer = answer + strconv.Itoa(numbers[i])
    }
    // 첫째자리가 0이면 0으로 ex) 0000일수 있으므로
    if answer[0] == '0'{
        return "0"
    }
    return answer
}

import "fmt"
import "sort"

func solution(citations []int) int {
    
    
    // 정렬로 nlogn을 썼음
    sort.Slice(citations, func(a,b int) bool{
        return citations[a] > citations[b]
    })
    
    var h_index = 0
    var cite = 0
    
    for i:= 0; i<len(citations); i++{
        
        // 임시 H 인덱스를 만들고
        var temp_index = citations[i]
        
        if citations[i] > 0{
            cite +=1
        }
        // 참조된것보다 임시 인덱스가 높으면 참조로 임시 인덱스를 줄이고
        if temp_index > cite {
            temp_index = cite
        }
        
        // H 인덱스의 맥스값을 갱신
        if temp_index > h_index{
            h_index = temp_index
        }
    }
   
    
    return h_index
}

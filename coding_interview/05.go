import "fmt"
import "sort"

func groupAnagrams(strs []string) [][]string {
    
    //2차원 배열 선언
    var hash map[string] []string
    hash = make(map[string][]string)
    
    
    //먼저 각 스트링을 정렬해서 표현해보자
    for i:= 0; i<len(strs); i++{
        
        s := strings.Split(strs[i], "")
        sort.Strings(s)
        var sort_s = strings.Join(s, "")
        //fmt.Println(sort_s)
        hash[sort_s] = append(hash[sort_s], strs[i])
    }
    
    var result = [][] string{}
    
    // 해쉬값을 결과값에 넣는다
    for _, value := range hash {
        result = append(result, value)
    }
    
    
    return result
}

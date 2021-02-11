import "strings"
//import "fmt"
import "unicode"
import "sort"

func reorderLogFiles(logs []string) []string {
    
    var letter = []string {}
    var digit = [] string {}
    
    // 각각의 로그가 레터인디 디짓인지 먼저 판별하자
    
    
    for i:=0; i< len(logs); i++{
        var arr_split = strings.Split(logs[i], " ")
        if unicode.IsDigit(rune(arr_split[1][0])){
            //숫자 로그에 넣는다
            digit = append(digit, logs[i])
        } else{
            letter = append(letter, logs[i])
        }
    }    
    
    
    // 레터 로그 정렬
    sort.Slice(letter, func (i, j int) bool{
        var split_i = strings.Split(letter[i], " ")
        var total_i = ""
        for i:=1; i<len(split_i); i++{
            total_i = total_i + split_i[i] + " "
        }
        
        var split_j = strings.Split(letter[j], " ")
        
        var total_j = ""
        for i:=1; i<len(split_j); i++{
            total_j = total_j + split_j[i] + " "
        }
        
        if total_i < total_j{
            return true
        } else if total_i == total_j { //뒤에 문자가 동일하면 식별자 순으로 처리해야함
            return split_i[0] < split_j[0]
        } else{
            return false
        }
        
    })
    
    
    // 레터 뒤에 숫자로그 합치기
    for i:=0; i <len(digit); i++{
        letter = append(letter, digit[i])
    }
    //fmt.Println(digit)
    //fmt.Println(letter)
    
    return letter
}

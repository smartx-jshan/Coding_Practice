//import "fmt"
//import "unicode"
import "strings"

func mostCommonWord(paragraph string, banned []string) string {
    // 우선은 문자열만 전처리해보자
    
    paragraph = strings.Replace(paragraph, ",", " ", -1)
    paragraph = strings.Replace(paragraph, "?", " ", -1)
    paragraph = strings.Replace(paragraph, ";", " ", -1)
    paragraph = strings.Replace(paragraph, ".", " ", -1)
    paragraph = strings.Replace(paragraph, "!", " ", -1)
    paragraph = strings.Replace(paragraph, "'", " ", -1)
    //fmt.Println(paragraph)
    
    
    /*
    var arr = ""
    for i:=0; i<len(paragraph); i++{
        if unicode.IsLower(rune(paragraph[i])){
            arr = arr + string(paragraph[i])
        }
        if unicode.IsUpper(rune(paragraph[i])){
            arr = arr + string(paragraph[i])
        }
        if paragraph[i]== ' '{
            arr = arr + string(paragraph[i])
        }
    }*/
    
    var arr = strings.ToLower(paragraph) //.과 , ! ? 처리 후, 대소문자를 소문자로 통일하였음
    //fmt.Println(arr)
    
    // 해쉬 테이블 초기화
    var hash map[string]int
    hash = make(map[string]int)
    
    var split = strings.Split(arr, " ") // 먼저 배열에 단어들을 쪼개서 담은후
    
    for i:=0; i<len(split); i++{
        
        if split[i] == "" { //빈 공간이 split으로 들어갈수 있다 이 부분을 예외 처리 해야함
            continue
        }
        
        //금지어 리스트에 있는지 먼저 확인
        var flag = 0
        for j:=0; j<len(banned); j++{
            if split[i] == banned[j]{
                flag = 1
                continue
            }
        }
        if flag == 1{
            continue // 다음 문자로 스킵
        }
        
        
        // 해쉬 테이블에 넣기
        _, ok := hash[split[i]]
        
        if ok{
            hash[split[i]] += 1
        } else{
            hash[split[i]] = 1
        }
    }
    fmt.Println(hash)
    
    var result ="" // 정답
    var max = 0 // 카운터 수
    for key, value := range hash{
        if value > max{
            result = key
            max = value
        }
    }
    
    
    return result
}

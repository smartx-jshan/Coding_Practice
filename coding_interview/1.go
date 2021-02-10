import "regexp"
import "strings"
import "fmt"

func isPalindrome(s string) bool {
    
    //먼저 소문자로 변경
    s = strings.ToLower(s)
    
    var arr = []string{}
    
    for i:=0; i<len(s); i++{
        matched, _ := regexp.MatchString("[a-z0-9]",string(s[i]))
        if matched{
            arr = append(arr, string(s[i]))
        }
    }
    // 소문자로 변경후 필요한 영문 숫자만 어레이로 등록
    
    
    //팰린드롬 체크
    var left = 0
    var right = len(arr) -1
    
    for {
        if left >= right{
            break // 모든 것을 탐색하면 종료
        }
        if arr[left] != arr[right]{
            return false
        }
        left +=1
        right -=1
    }
    //여기까지 왔으면 정상인것이다
    return true
}

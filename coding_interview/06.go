import "fmt"

func expand(left, right int, s string) string{
    
    for {
        if left >=0 && right <=len(s) && s[left] == s[right-1]{
            left -=1
            right +=1
        } else {
            break
        }
        
    }
    return s[left+1:right-1]
}

func longestPalindrome(s string) string {
    
    var result = ""
    
    if len(s) <2{
        return s
    }
    
    for i:=0; i<len(s)-1; i++{
        
        var temp1 = expand(i, i+1,s)
        var temp2 = expand(i, i+2,s)
        
        if len(result) < len(temp1){
            result = temp1
        }
        if len(result) < len(temp2){
            result = temp2
        }
    }
    
    //fmt.Println(result)
    return result
}

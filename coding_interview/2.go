func reverseString(s []byte)  {
    
    var left =0
    var right = len(s)-1
    
    for {
        if left >= right{
            break
        }
        
        s[left], s[right] = s[right], s[left]
        left +=1
        right -=1
    }
}

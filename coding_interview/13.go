/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func isPalindrome(head *ListNode) bool {
    //런너를 이용해서 해보자
    
    var rev *ListNode
    var slow *ListNode
    var fast *ListNode
    
    slow = head
    fast = head

    
    for fast != nil && fast.Next != nil{
        fast = fast.Next.Next
        var temp = rev
        rev = slow
        slow = slow.Next
        rev.Next = temp
       
    }
    if fast != nil{
        slow = slow.Next
    }
    
    
    for rev != nil && rev.Val == slow.Val{
        slow = slow.Next
        rev = rev.Next
    }
    if rev == nil{
        return true
    }else{
        return false
    }
}

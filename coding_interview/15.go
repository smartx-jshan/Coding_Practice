/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reverseList(head *ListNode) *ListNode {
    
    var rev *ListNode //역순을 저장할 리스트 노드 선언
    
    for head != nil{
        var next = head.Next
        head.Next= rev
        rev = head
        head = next
        
    }
    
    return rev
}

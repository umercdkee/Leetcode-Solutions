/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var deleteDuplicates = function(head) {
    original = head;
    previous = null;
    while (head && head.next != null){
        if (head.val === head.next.val){
            while (head && head.next && head.val === head.next.val)
                head.next = head.next.next;
            if (previous){
                previous.next = head.next;
                head = head.next;
            }
            else{
                head = head.next;
                original = head;
            }
        }

        else {
            previous = head;
            head = head.next;
        }
    }
    return original;
};
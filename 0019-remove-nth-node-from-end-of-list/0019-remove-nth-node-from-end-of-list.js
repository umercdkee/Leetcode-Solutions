/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function(head, n) {
    num_nodes = 0;
    count_head = head;
    original = head;
    while (count_head){
        num_nodes += 1;
        count_head = count_head.next
    }
    target = num_nodes - n;
    if (target === 0)
        return head.next;
    count = 0;
    if (target)
    while (head){
        if (head.next && count + 1 === target){
            head.next = head.next.next
            return original;
        }
        else{
            count += 1;
            head = head.next;
        }

    }
};
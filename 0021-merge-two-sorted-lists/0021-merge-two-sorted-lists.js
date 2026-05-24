/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function(list1, list2) {
    head = null
    if (list1 && list2 && list1.val >= list2.val){
        head = list2;
        list2 = list2.next;
    }
    else if (list1){
        head = list1;
        list1 = list1.next;
    }
    else if (list2){
        head = list2;
        list2 = list2.next;
    }
    original = head;
    while (list1 && list2){
        console.log(list1,list2);
        if (list1.val >= list2.val){
            head.next = list2;
            list2 = list2.next;
        }
        else{
            head.next = list1;
            list1 = list1.next;
        }
        head = head.next
    }
    while (list1 && head){
        head.next = list1;
        list1 = list1.next;
        head = head.next;
    }
    while (list2 && head){
        head.next = list2;
        list2 = list2.next;
        head = head.next;
    }
    return original;
        
};
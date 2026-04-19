# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        n1, n2 = head, head.next
        node = head

        while n2 and n2.next:
            n1 = n1.next
            n2 = n2.next.next

        second = self.reverse(n1.next)
        n1.next = None

        first = head
        while second:
            tmp1, tmp2 = first.next, second.next

            first.next = second
            second.next = tmp1

            first, second = tmp1, tmp2


        # dummyNode = ListNode(0)
        # node, n1 = dummyNode, head
        # i = 0
        # while n1 or n2:
        #     if i%2 == 0:
        #         node.next, n1 = n1, n1.next
        #     else:
        #         node.next, n2 = n2, n2.next          
        #     node = node.next
        #     i += 1
        # return dummyNode.next
            
        
    def reverse(self, node):
        cur, prev = node, None

        while cur:
            nxt_node = cur.next
            cur.next = prev
            prev = cur
            cur = nxt_node
        return prev



        
        
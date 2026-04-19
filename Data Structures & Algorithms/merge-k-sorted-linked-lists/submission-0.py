# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []

        # push all linked list nodes to min_heap
        for node in lists:
            while node:
                heapq.heappush(min_heap, node.val)
                node = node.next

        # lets pop all nodes off from min_heap & them to our new ll
        dummyNode  = ListNode(0)
        cur = dummyNode
        while min_heap:
            new_node = ListNode(heapq.heappop(min_heap))
            cur.next = new_node
            cur = cur.next

        return dummyNode.next


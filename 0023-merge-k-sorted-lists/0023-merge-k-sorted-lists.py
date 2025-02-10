# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class HeapNode: 
    def __init__(self, node): 
        self.node = node
    
    def __gt__(self, other):
        return self.node.val > other.node.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        for i in range(len(lists)): 
            #Push to heap 
            l = lists[i]
            # print(head.next.val)
            if l:
                heapq.heappush(minHeap, HeapNode(l))

        dummy = ListNode(0)
        cur = dummy 
        while minHeap: 
            heap_node = heapq.heappop(minHeap)
            node = heap_node.node

            cur.next = node
            cur = cur.next
            if node.next: 
                heapq.heappush(minHeap, HeapNode(node.next))

        return dummy.next


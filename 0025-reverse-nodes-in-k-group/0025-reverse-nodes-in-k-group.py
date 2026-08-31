# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def hasKNodes(node,k):
            count=0
            while node and count<k:
                node=node.next
                count+=1
            return count==k
        dummy=ListNode(0)
        dummy.next=head
        groupPrev=dummy
        while True:
            if not hasKNodes(groupPrev.next,k):
                break
            prev,curr=None,groupPrev.next
            groupstart=curr
            for _ in range(k):
                nxt=curr.next
                curr.next=prev
                prev=curr
                curr=nxt
            tail=groupPrev.next
            groupPrev.next=prev
            groupstart.next=curr
            groupPrev=groupstart
        return dummy.next
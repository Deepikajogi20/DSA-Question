# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values=[]
        current=head
        while current:
            values.append(current.val)
            current=current.next
        values.sort()
        current=head
        i=0
        while current:
            current.val=values[i]
            i+=1
            current=current.next
        return head
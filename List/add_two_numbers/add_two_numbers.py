# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        root=n=ListNode(0)
        carry=0
        while l1 or l2 or carry:
            if l1:
                val1=l1.val
                l1=l1.next
            else: 
                val1=0
            if l2:
                val2=l2.val
                l2=l2.next
            else:
                val2=0
            carry,val=divmod(val1+val2+carry,10)
            n.next=ListNode(val)
            n=n.next

        return root.next
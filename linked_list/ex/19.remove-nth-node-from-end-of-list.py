#
# @lc app=leetcode id=19 lang=python
#
# [19] Remove Nth Node From End of List

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        p = ListNode(-1)
        #------------------------------
        # Dont forget the dummy head!!!
        #------------------------------
        p.next = head
        pfast = p
        pslow = p
        for _ in range(n):
            pfast = pfast.next
        while pfast.next:
            pfast = pfast.next
            pslow = pslow.next
        pslow.next = pslow.next.next
        return p.next
            
        
# @lc code=end


#
# @lc app=leetcode id=142 lang=python
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pfast = head
        pslow = head
        while pfast and pfast.next:
            pfast = pfast.next.next
            pslow = pslow.next
            if pfast == pslow:
                break
        if pfast is None or pfast.next is None:
            return None
        pslow = head
        while pfast!=pslow:
            pfast = pfast.next
            pslow = pslow.next
        return pslow
        
# @lc code=end


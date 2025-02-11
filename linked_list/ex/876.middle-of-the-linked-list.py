#
# @lc app=leetcode id=876 lang=python
#
# [876] Middle of the Linked List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        p = ListNode(-1)
        p.next = head
        pfast = p
        pslow = p
        while pfast and pfast.next:
            pfast = pfast.next.next
            if pfast is None:
                break
            pslow = pslow.next
        return pslow.next
        
# @lc code=end


#
# @lc app=leetcode id=160 lang=python
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # p1遍历完表1遍历表2， p2遍历完表2遍历表1， 在交点相遇
        p1, p2 = headA, headB
        while p1!=p2:
            p1 = headB if p1 is None else p1.next
            p2 = headA if p2 is None else p2.next
        return p1
                
        
# @lc code=end


#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        head1 = ListNode(-1)
        head2 = ListNode(-1)
        p1 = head1
        p2 = head2
        p = head
        while p:
            if p.val < x:
                p1.next = p
                p1 = p1.next
            else:
                p2.next = p
                p2 = p2.next
            # p = p.next # WRONG!!
            # break the connection, otherwise there would be a cycle
            temp = p.next
            p.next = None 
            p = temp           
        p1.next = head2.next
        return head1.next
        
        
        
        
# @lc code=end


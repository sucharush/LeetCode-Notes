#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
import heapq
class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        if not lists:
            return None
        main_head = ListNode(-1)
        p = main_head
        pq = []
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(pq, (head.val, i, head))
        while pq:
            _, i, node = heapq.heappop(pq)
            p.next = node
            if node.next:
                heapq.heappush(pq, (node.next.val, i, node.next))
            p = p.next
        return main_head.next
# @lc code=end


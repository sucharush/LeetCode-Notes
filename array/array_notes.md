### List

| No. | - | link | - | tag |
|------|----------|------|------|------|
| 26  | Remove Duplicates from Sorted Array | [LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | ✅ | 快慢指针 |
| 83  | Remove Duplicates from Sorted List | [LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-list/) | ✅ | 快慢指针（链表） |
| 27  | Remove Element | [LeetCode](https://leetcode.com/problems/remove-element/) | ✅ | 快慢指针 |
| 283 | Move Zeroes | [LeetCode](https://leetcode.com/problems/move-zeroes/) | ✅ | 快慢指针 |
| 344 | Reverse String | [LeetCode](https://leetcode.com/problems/reverse-string/) | ✅ | 左右指针 |
| 167 | Two Sum II - Input Array Is Sorted | [LeetCode](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | ✅ | 左右指针 |
| 5   | Longest Palindromic Substring | [LeetCode](https://leetcode.com/problems/longest-palindromic-substring/) | ⭕️ | 双指针（中心扩展， 空间O(1)）/ dp(空间O(n^2)) |

---

### Notes

1. **双指针**：
   - **有序数组操作**：  
     适用于两数之和、去重、移除元素、移动零、反转字符串等问题。  
     时间复杂度：O(n)，空间复杂度：O(1)。
   - **链表操作**：  
     使用快慢指针处理链表去重（如题83），需注意指针移动边界条件。

2. **最长回文子串（题5）**：
   - 从每个字符或每对相邻字符向两侧扩展，判断是否为回文。  
     时间复杂度：O(n²)，空间复杂度：O(1)。  
     或dp：`dp[i][j] = (s[i] == s[j]) && dp[i+1][j-1]`。

     


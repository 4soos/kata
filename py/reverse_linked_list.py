class Solution:
    """
    遍历:
    存入数组，反转数组

    时间复杂度：O(n)O(n)，reverse()reverse() 的时间复杂度为 O(n)O(n)，遍历了一遍数组，复杂度也为 O(n)O(n)。
    空间复杂度：O(n)O(n)，使用了额外的 res。
    """
    def reversePrint(self, head: ListNode) -> List[int]:
        res = []

        while head:
            res.append(head.val)
            head = head.next
        return res[::-1]

    """
    递归:
    假设 head.next 已经排好序，那么只需将 head 添加到末尾即可。
    其中，head.next 部分可以使用递归来实现，递归的终止条件为 head 为空。

    时间复杂度：O(n)O(n)，递归 nn 次，时间间复杂度为 O(n)O(n)，递归函数中的操作时间复杂度为 O(1)O(1)，总时间复杂度为 O(n)\times O(1)=O(n)O(n)×O(1)=O(n)。
    空间复杂度：O(n)O(n)，递归将占用链表长度的栈空间。

    """
    def reversePrint2(self, head: ListNode) -> List[int]:
        if not head: return []
        return self.reversePrint2(head.next) + [head.val]

    """
    堆栈
    利用堆栈先进后出的特点，先依次将元素压入堆栈中，然后将所有元素从堆栈中弹出，即可实现反转
    
    时间复杂度：O(n)O(n)，pushpush 的间复杂度为 O(n)O(n)，poppop 的间复杂度为 O(n)O(n)。
    空间复杂度：O(n)O(n)，使用了额外的 res 和 堆栈。
    """
    def reversePrint3(self, head: ListNode) -> List[int]:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next

        res = []
        while stack:
            res.append(stack.pop())
            
        return res
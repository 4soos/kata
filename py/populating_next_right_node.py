from collections import deque


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect_bfs(self, root: 'Node') -> 'Node':
        
        if not root:
            return root
        
        # 初始化队列同时将第一层节点加入队列中，即根节点
        Q = deque([root])
        
        # 外层的 while 循环迭代的是层数
        while Q:
            
            # 记录当前队列大小
            size = len(Q)
            
            # 遍历这一层的所有节点
            for i in range(size):
                
                # 从队首取出元素
                node = Q.popleft()
                
                # 连接
                if i < size - 1:
                    node.next = Q[0]
                
                # 拓展下一层节点
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
        
        # 返回根节点
        return root

    def connect_pointer(self, root: 'Node') -> 'Node':

        if not root: return root

        # 根节点开始
        leftmost = root

        while leftmost.left:
            
            # 遍历当前层节点组织成的链表, 为下一层的节点更新next节点
            head = leftmost

            while head:

                
                head.left.next = head.right

                if head.next:
                    head.right.next = head.next.left

                # 指针后移
                head = head.next

            # 去下一层的最左节点
            leftmost = leftmost.left



        return root

    def connect_iter(self, root: 'Node') -> 'Node':
        """
        纵向是二叉树，横向是链表，两层嵌套循环，主循环处理各层，子循环处理每层节点的各子节点。
        定义 3 个变量，分别标记：下一层头节点 head，下一层已遍历到的前置节点 pre，
        以及当前层处理的游标 cur：

            * 总初始化：下一层要处理的头节点 head=root
            
            * 各层初始化：当前层处理游标节点 cur 用head更新赋值，而后 pre=head=None，
            表示下一层尚未找到前置和头节点
            
            * 对当前层游标节点 cur 进行处理，对左右子节点分别判断：
                
                * 如果下一层尚未找到前置节点，则意味着该左/右子节点就是下一层的头节点，
                于是更新 pre=head=该子节点

                * 如果pre已赋值，则直接更新 pre 的 next 到当前的左/右子节点，
                然后 pre 更新到其 next 值
                
                * cur 游标更新到下一个值
            
            * 根据更新后的 head，处理下一层


        """
        head = root

        while head:
            cur = head
            pre = head = None

            while cur:
                if cur.left:
                    if not pre:
                        pre = head = cur.left
                    else:
                        pre.next = cur.left
                        pre = pre.next

                if cur.right:
                    if not pre:
                        pre = head = cur.right

                    else:
                        pre.next = cur.right
                        pre = pre.next
                cur = cur.next

        return root

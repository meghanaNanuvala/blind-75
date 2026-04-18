class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # if we take inorder (left, root, right)
        n = 0
        stack = []
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            n += 1

            if n == k:
                return cur.val

            cur = cur.right
'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def isBalanced(self, root):
        # code here
        def check(node):
            if not node:
                return 0
            left = check(node.left)
            if left == -1:
                return -1
            right = check(node.right)
            if right == -1:
                return -1
            if abs(left-right) > 1:
                return -1
            return 1 + max(left,right)
        return check(root) != -1
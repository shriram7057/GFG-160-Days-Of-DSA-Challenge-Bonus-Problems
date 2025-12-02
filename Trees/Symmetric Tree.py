'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def isSymmetric(self, root):
        # code here
        def isMirror(a,b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            return (a.data == b.data
                    and isMirror(a.left,b.right)
                    and isMirror(a.right,b.left))
        return isMirror(root.left,root.right) if root else True
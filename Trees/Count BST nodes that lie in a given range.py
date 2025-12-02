'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    def getCount(self, root, l, h):
        # Your code here
        if not root:
            return 0
        
        if  l <= root.data <= h:
            return 1 + self.getCount(root.left,l,h) + self.getCount(root.right,l,h)
        if root.data < l:
            return self.getCount(root.right,l,h)
        return self.getCount(root.left,l,h)
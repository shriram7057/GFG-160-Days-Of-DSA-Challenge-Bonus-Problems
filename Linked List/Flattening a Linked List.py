'''
class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''

class Solution:
    def merge(self, a,b):
        # code here
        if not a:
            return b
        if not b:
            return a
        if a.data < b.data:
            result = a
            result.bottom = self.merge(a.bottom,b)
        else:
            result = b
            result.bottom = self.merge(a, b.bottom)
            
        result.next = None
        return result
    def flatten(self,root):
        if not root or not root.next:
            return root
        right = self.flatten(root.next)
        root.next = None
        
        root = self.merge(root,right)
        
        return root
'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    def balanceBST(self,root):
        #code here
        arr = []
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            arr.append(node.data)
            inorder(node.right)
            
        inorder(root)
        
        def build(l,r):
            if l > r:
                return None
            mid = (l+r)//2
            node=Node(arr[mid])
            node.left=build(l,mid-1)
            node.right=build(mid+1,r)
            return node
        return build(0,len(arr)-1)
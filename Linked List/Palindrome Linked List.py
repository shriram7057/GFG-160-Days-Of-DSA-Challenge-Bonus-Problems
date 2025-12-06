'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

class Solution:
    def isPalindrome(self, head):
        # code here
        if not head or not head.next:
            return True
        slow = fast = head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            
        prev=None
        curr=slow
        
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        
        left = head
        right = prev
        while right:
            if left.data != right.data:
                return False
            left = left.next
            right= right.next
            
        return True
        
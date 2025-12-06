'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

class Solution:
    def intersectPoint(self, head1, head2):
        # code here
        if not head1 or not head2:
            return None
        a=head1
        b=head2
        
        while a is not b:
            a=a.next if a else head2
            b=b.next if b else head1
        return a
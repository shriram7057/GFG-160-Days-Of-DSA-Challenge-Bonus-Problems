#User function Template for python3
class Solution:

	def findMaximum(self, arr):
		# code here
		l,r=0,len(arr)-1
		
		while l < r:
		    mid=(l+r)//2
		    
		    if arr[mid]<arr[mid+1]:
		        l=mid+1
		    else:
		        r=mid
		return arr[l]
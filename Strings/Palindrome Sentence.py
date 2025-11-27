class Solution:
	def isPalinSent(self, s):
		# code here
		t = "".join(c.lower() for c in s if c.isalnum())
		return 1 if t == t[::-1] else 0 
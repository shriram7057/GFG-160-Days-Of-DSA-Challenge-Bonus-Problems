class Solution:
    def medianOf2(self, a, b):
        # code here
        if len(a)>len(b):
            return self.medianOf2(b,a)
        n,m=len(a),len(b)
        l,r=0,n
        
        while l<= r:
            cut1=(l+r)//2
            cut2=(n+m+1)//2 - cut1 
            
            left1=float('-inf') if cut1 == 0 else a[cut1-1]
            left2=float('-inf') if cut2 == 0 else b[cut2-1]
            
            right1=float('inf') if cut1 == n else a[cut1]
            right2=float('-inf') if cut2 == m else b[cut2]
                
            if left1 <= right2 and left2 <= right1:
                if (n+m) % 2 == 0:
                    return (max(left1,left2)+min(right1,right2))/2
                else:
                    return max(left1,left2)
            elif left1 > right2:
                r=cut1 - 1
            else:
                l=cut1+1
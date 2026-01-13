class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if x==0 or x==1:
            return x
        l,r=1,x
        while(l<=r):
            mid=l+(r-l)/2
            s=mid*mid
            if s==x:
                return mid
            elif s<=x:
                l=mid+1
            else:
                r=mid-1
        return r

        
        



        
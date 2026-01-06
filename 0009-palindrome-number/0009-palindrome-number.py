class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        s=str(x)
        #return x[::]==x[::-1]
       
        # l = 0
        # r = len(s) - 1

        # while l < r:
        #     if s[l] != s[r]:
        #         return False
        #     l += 1
        #     r -= 1

        # return True

        org=x
        rev=0
        while(x>0):
            last=x%10
            rev=(rev*10)+last
            x=x//10
        return org == rev

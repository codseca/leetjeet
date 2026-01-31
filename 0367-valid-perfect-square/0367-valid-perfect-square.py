class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<2:
            return True

        s,e=2,num//2
        while s<=e:
            mid=s+(e-s)//2

            se=mid*mid
            if se==num:
                return True
            elif se<num:
                s=mid+1
            else:
                e=mid-1

        return False
        
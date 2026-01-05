class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        start=1
        end=max(piles)
        ans=end
        while(start<=end):
            mid=start+(end-start)//2

            hours = 0

            for pile in piles:
                hours += (pile + mid - 1) // mid

            if hours <= h:
                ans = mid
                end = mid - 1     
            else:
                start = mid + 1   

        return ans
            
     
        
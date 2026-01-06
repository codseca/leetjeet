class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        # n = len(height)
        # maxLeft, maxRight = [0] * n, [0] * n
        
        # for i in range(1, n):
        #     maxLeft[i] = max(height[i-1], maxLeft[i-1])
        # for i in range(n-2, -1, -1):
        #     maxRight[i] = max(height[i+1], maxRight[i+1])
            
        # ans = 0
        # for i in range(n):
        #     waterLevel = min(maxLeft[i], maxRight[i])
        #     if waterLevel >= height[i]:
        #         ans += waterLevel - height[i]
        # return ans
        n=len(height)
        left_max = [0]*n
        right_max=[0]*n
        left_max[0]=height[0]
        right_max[n-1]=height[n-1]

        for i in range(1,n):
            left_max[i]=max(left_max[i-1],height[i])

        for i in range(n-2,-1,-1):
            right_max[i]=max(height[i],right_max[i+1])
        
        tot_water=0

        for i in range(n):
            tot_water+=min(left_max[i],right_max[i])-height[i]
        
        return tot_water
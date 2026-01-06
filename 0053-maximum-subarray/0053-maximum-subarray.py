class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        curr_sum=nums[0]
        ms=nums[0]
        for i in range(1,n):
            curr_sum = max(curr_sum + nums[i] , nums[i])
            ms=max(ms,curr_sum)
        return ms